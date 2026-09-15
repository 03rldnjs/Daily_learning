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
*(윈도우 경로: `%APPDATA%\Claude\claude_desktop_config.json`)*

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
