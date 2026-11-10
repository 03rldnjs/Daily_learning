# 💻 Daily Learning Lab (C/Python/AWS Certificate / MCP)

C언어와 Python, AWS 자격증(CLF-C02, SAA-C03) 및 LLM MCP 서버 연동 등 깊이 있는 엔지니어링을 공부하며 구현한 핵심 프로젝트와 아키텍처 고민을 누적하는 공간입니다.  
This repository is an archive of my journey in mastering C, Python, AWS cloud architecture, and MCP server development, focusing on robust error-handling and software engineering principles.

---

## 📂 저장소 구조 (Repository Architecture)

이 저장소는 언어 및 기술 스택에 따라 총 6개의 핵심 연구 폴더로 구성되어 있습니다. 각 폴더명을 클릭하면 해당 디렉토리의 상세 주석과 구현 코드로 이동합니다.

| 디렉토리 (Directory) | 핵심 기술 스택 (Tech Stack) | 주요 연구 및 프로젝트 내용 (Key Focus & Projects) |
| :--- | :--- | :--- |
| [**`c`**](./c) | `C`, `math.h`, Buffer I/O, Pointers | 공학용 계산기, 미니 좌석 예약 시스템, 동적 메모리 기반 Auto Scaling 시뮬레이터 |
| [**`python`**](./python) | `Python`, OOP, File I/O | 학생 관리 시스템, 영속적 자산 관리 프로그램 (`csv`, `class`) |
| [**`python_GUI`**](./python_GUI) | `Python`, GUI Library | 파이썬 기반 그래픽 사용자 인터페이스 연구 공간 |
| [**`AWS CLF-C02`**](./AWS%20CLF-C02) | `AWS Cloud Practitioner` | CLF-C02 자격증 취득을 위한 핵심 개념, 오답 노트, 서비스 비교 노트 |
| [**`AWS SAA-C03`**](./AWS%20SAA-C03) | `AWS Solutions Architect` | SAA-C03 취득을 위한 고가용성 아키텍처 및 클라우드 설계 심화 학습 |
| [**`MCP`**](./MCP) | `MCP (Model Context Protocol)`, `Claude` | Claude AI와 연동하기 위한 커스텀 MCP 서버 제작 및 외부 도구 통합 연구 |

---

## 🛠️ 주요 프로젝트 소개 (Featured Projects)

### 🔵 C Language Lab: 하드웨어 메모리 제어와 아키텍처 시뮬레이션
> **상세 리드미 보기:** [C_Language README](./c)

C언어의 표준 입출력 스트림, 포인터, 그리고 힙 메모리 동적 할당을 활용해 시스템의 안정성을 극대화하고 클라우드 인프라의 원리를 코드로 구현했습니다.

- **📊 AWS EC2 Auto Scaling 시뮬레이터 (`auto_scaling_sim.c`)**
    * **동적 메모리 제어:** `malloc`과 `realloc`을 활용하여 CPU 평균 사용량 임계치에 따라 EC2 인스턴스를 가변적으로 확장(`Scale Out`) 및 축소(`Scale In`)하는 로직 구현.
    * **방어적 프로그래밍:** `temp` 포인터 패턴을 통한 `realloc` 주소 유실(Memory Leak) 방지 및 최대/최소 인스턴스 개수(`MAX_CAPACITY`, `MIN_CAPACITY`) 제한.
- **🧮 포인터 기반 공학용 계산기 고도화 버전 (`scientific_calculator_pointer.c`)**
    * 단일 책임 원칙(SRP) 적용 및 C언어의 '1개 값 반환' 제약을 포인터 주소 참조 방식(`Call by Reference`)으로 극복.

---

### 🐍 Python Lab: 파이썬 고유 패러다임과 데이터 무결성 확보
> **상세 리드미 보기:** [Python README](./python)

파이썬의 데이터 구조적 유연성을 학습하고, 파일 영속성(File I/O)과 객체 지향 프로그래밍(OOP)을 적용하여 정교한 비즈니스 로직을 빌드했습니다.

- **💵 자산 관리 프로그램 완성판 (`asset_manager_advanced.py`)**
    * **객체 지향 설계:** `class`와 `__init__` 함수를 활용한 도메인 모델 설계.
    * **데이터 무결성:** '리스트 내부의 딕셔너리' 복합 자료구조를 채택하여 동일 키값 중복으로 인한 덮어쓰기(Overwrite) 방지.
    * **영속적 데이터:** `csv` 모듈 기반 파일 입출력을 연동하여 프로그램 종료 후에도 데이터가 유지되는 구조 구현.

---

### ☁️ AWS & MCP Lab: 클라우드 인프라 심화 및 AI 연동 에코시스템

- **AWS 자격증 정복 로드맵 (`AWS CLF-C02` & `AWS SAA-C03`)**
    * **CLF-C02:** AWS 리소스와 서비스에 대하 기본기 체득. 2026년 8월 자격증 취득.
    * **SAA-C03:** 실무 중심의 아키텍처 설계 패턴, VPC 네트워킹, 로드 밸런싱(ALB/NLB), 스토리지 최적화 전략 등 심화 학습 진행 중.
- **Model Context Protocol (MCP) 서버 개발 (`MCP/`)**
    * LLM(Claude)이 로컬 시스템 및 외부 데이터 소스와 안전하게 상호작용할 수 있도록 커스텀 MCP 서버를 설계 및 구현하여 AI 에이전트 확장성 연구 수행.

---

## 💡 핵심 학습 성과 (Core Engineering Skills)

1. **단일 책임 원칙 (SRP) 및 모듈화 체득**
    * UI 로직과 핵심 비즈니스 로직(연산, 메모리 제어)을 철저히 격리하여 재사용성과 확장성을 확보했습니다.
2. **로우레벨 메모리 관리 및 방어적 코드 설계**
    * C언어 포인터와 동적 할당 라이프사이클을 정확히 이해하고, 예외 상황(버퍼 오버플로우, 메모리 할당 실패)을 통제하는 방어적 프로그래밍을 실천했습니다.
3. **클라우드 아키텍처와 AI 생태계의 융합**
    * 이론으로 접한 AWS 클라우드 인프라 설계 패턴(Auto Scaling, Multi-AZ)을 코드로 직접 구현하고, 최신 AI 연동 기술인 MCP까지 폭넓게 탐구했습니다.

---

To be continued... 학습 진행도에 따라 본 로드맵은 실시간으로 업데이트됩니다.
