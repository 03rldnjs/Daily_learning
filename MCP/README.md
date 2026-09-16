# 🛠️ Claude Desktop Custom MCP Server

# project 1: System Monitor & Calculator
Anthropic의 **MCP(Model Context Protocol)** 표준을 활용하여, Claude Desktop 앱이 내 로컬 컴퓨터의 시스템 리소스(CPU, RAM, Disk)를 실시간으로 모니터링하고 계산 연산을 수행할 수 있도록 연동한 커스텀 MCP 서버 프로젝트입니다.

---

## 🌟 주요 기능 (Provided Tools)

- **🖥️ System Monitoring (`psutil` 활용)**
  - `get_cpu_usage`: 전체 및 코어별 CPU 사용률(%) 조회
  - `get_memory_status`: RAM 전체/사용/잔여 용량(GB) 및 사용률 조회
  - `get_disk_status`: C드라이브 등 지정한 디스크 드라이브 잔여 용량 조회
- **🔢 Calculator Operations**
  - 기본적인 사칙연산 처리

---

## 🏗️ 시스템 구조 (Architecture)

```text
[User] ──(자연어 요청)──> [Claude Desktop App (MCP Client)]
                                    │
                                    │ (MCP Protocol / STDIN-STDOUT)
                                    ▼
                        [Python MCPserver Server (server.py)]
                                    │
                         (psutil / System APIs)
                                    ▼
                         [Local Hardware Resources]
```

---

## 🚀 시작하기 (Quick Start)

### 1. 전제 조건 (Prerequisites)
- Python 3.10 이상
- [uv](https://github.com/astral-sh/uv) (Fast Python package installer)
- [Claude Desktop App](https://claude.ai/download)


### 2. Claude Desktop 연동 설정 (`claude_desktop_config.json`)
Claude Desktop의 설정 파일에 아래와 같이 등록합니다.
*(윈도우 경로: `%APPDATA%\Claude\claude_desktop_config.json`-> 해당 경로는 경우에 따라 달라질 수 있음(폴더 이름이 Claude 자체가 아니라 Claude로 시작하는 이름을 가진 폴더일 가능성 존재)*

```json
{
  "mcpServers": {
    "my-system-monitor": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/YOUR_PROJECT_PATH/mcp-system-monitor",
        "run",
        "server.py"
      ]
    }
  }
}
```

---

## 실행 예시

> Claude Desktop에 "지금 내 메모리 잔여 용량이랑 C드라이브 상태 확인해 줘"라고 요청
> 답변 예시

메모리 상태

전체 용량: 31.14GB
사용 중: 16.52GB
잔여 용량: 14.62GB
사용률: 53.1%

C드라이브 상태입니다.

전체 용량: 474.53GB
사용 중: 204.72GB
남은 용량: 269.81GB
사용률: 43.1%

---

## 🛠️ 기술 스택 (Tech Stack)
- **Protocol:** Model Context Protocol (MCP)
- **Language:** Python 3.13
- **Framework:** `mcp` (FastMCP)
- **Package Manager:** `uv`
- **Libraries:** `psutil`


# Project 2: Log & File Analyzer MCP Server

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Server-green.svg)](https://modelcontextprotocol.io/)

LLM(Claude 등)이 로컬 파일 시스템의 디렉토리를 탐색하고 로그 파일을 안전하게 분석할 수 있도록 지원하는 **보안 강화형 Model Context Protocol (MCP) 서버**입니다.

보안이 고려되지 않은 파일 시스템 접근 도구는 Path Traversal, OS 장치 바인딩 Hang, DoS(서비스 거부) 공격 위험에 노출될 수 있습니다. 본 프로젝트는 **샌드박스(Sandbox) 격리 및 인포메이션 디스클로저 방지** 패턴을 적용하여 안전한 파일 처리 환경을 제공합니다.

---

## 🛠️ 주요 기능 (Tools)

| Tool 이름 | 설명 | 주요 보안 & 안정성 특징 |
| :--- | :--- | :--- |
| `list_directory` | 지정한 디렉토리 내 파일/폴더 목록 및 용량 조회 | 샌드박스 이탈 검증, 존재 유무 은닉 처리 |
| `read_last_logs` | 로그 파일의 마지막 N개 행 추출 | 50MB 대용량 파일 메모리 보호, Non-UTF8 인코딩 예외 무시 |
| `search_log_errors` | 키워드(ERROR, FAILED 등) 포함 로그 행 검색 | 스트리밍 읽기, 최대 출력 개수(Limit) 제한으로 토큰 폭탄 방지 |

---

## 🔒 보안 설계 및 취약점 방어 구조 (Security Architecture)

### 1. Path Traversal & 샌드박스 영역 격리
* `Path.resolve()`와 `.relative_to()`를 조합하여 상위 디렉토리 탈출 시도(`../`)를 정규화하여 완전히 차단합니다.
* 허용된 기본 작업 디렉토리(`ALLOWED_BASE_DIR`) 하위 경로만 접근을 승인합니다.

### 2. Windows 시스템 예약 장치 이름 접근 차단
* `CON`, `PRN`, `AUX`, `NUL`, `COM1~9`, `LPT1~9` 등 윈도우 OS 특수 장치명으로의 접근을 사전 검증(`WINDOWS_RESERVED_NAMES`)하여 무한 대기(Block/Hang)로 인한 DoS 공격을 방지합니다.

### 3. 정보 노출 방지 (Information Disclosure Avoidance)
* 경로 탈출이나 파일 읽기 예외 발생 시, 구체적인 내부 서버 경로나 트레이스백(Traceback)을 외부로 내보내지 않고 일반화된 에러 메시지(`PermissionError`)만 반환합니다.
* 파일 존재 여부와 디렉토리 여부 검사에 동일한 에러 응답을 사용하여 공격자의 디렉토리 구조 정찰을 차단합니다.

### 4. 자원 고갈 및 Context Limit 방어 (DoS Protection)
* **파일 용량 제한:** 50MB를 초과하는 대용량 파일에 대한 읽기 요청은 즉시 거부합니다.
* **결과 제한 (Max Results):** 로그 검색 결과가 설정값(기본 100개)을 초과할 경우 탐색을 즉시 중단하여 LLM Context Window의 토큰 오버플로우를 방지합니다.

---

## 🚀 시작하기

### Prerequisites
* Python 3.10 이상
* `mcp` 파이썬 패키지
