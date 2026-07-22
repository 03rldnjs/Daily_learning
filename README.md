# 💻 Daily Learning Lab (C/Python)

C언어와 Python을 깊이 있게 공부하며 구현한 핵심 프로젝트와 예외 처리, 소프트웨어 아키텍처에 대한 고민을 누적하는 공간입니다.  
This repository is an archive of my journey in mastering C and Python, focusing on robust error-handling, modularization, and software engineering principles.

---

## 📂 저장소 구조 (Repository Architecture)

이 저장소는 언어 및 기술 스택에 따라 총 3개의 핵심 연구 폴더로 구성되어 있습니다. 각 폴더명을 클릭하면 해당 디렉토리의 상세 주석과 구현 코드로 이동합니다.

| 디렉토리 (Directory) | 핵심 기술 스택 (Tech Stack) | 주요 연구 및 프로젝트 내용 (Key Focus & Projects) |
| :--- | :--- | :--- |
| [**🔵 C**](./) | `C`, `math.h`, Buffer I/O | 공학용 계산기(Prime), 미니 좌석 예약 시스템 / 버퍼 제어 및 예외 처리 |
| [**🐍 python**](./) | `Python`, OOP, File I/O | 학생 관리 시스템, 영속적 자산 관리 프로그램 / 객체 지향 및 자료구조 |
| [**🎨 python_GUI**](./) | `Python`, GUI Library | 파이썬 기반 그래픽 사용자 인터페이스 연구 공간 |

---

## 🛠️ 주요 프로젝트 소개 (Featured Projects)

### 🔵 C Language Lab: 하드웨어 버퍼 통제와 엄밀한 수리 연산
> **상세 리드미 보기:** [C_Language README](./)

C언어의 표준 입출력 스트림 메커니즘을 이해하고, 방어적 코드 설계(Defensive Coding)를 통해 프로그램의 안정성을 극대화하는 연습을 진행했습니다.

* **🧮 공학용 계산기 최종 진화 버전 (`scientific_calculator_prime.c`)**
    * **핵심 설계:** 단일 책임 원칙(SRP)을 기반으로 입력 검증(`_input`)과 순수 연산 엔진을 완벽히 격리.
    * **예외 처리:** 문자가 입력되었을 때 `scanf`의 입력 버퍼 찌꺼기를 `getchar()`로 완전히 비워주는 `clear_buffer()`를 구현하여 무한 루프 원천 차단.
    * **논리 최적화:** 두 개의 매개변수($n, r$)를 하나의 정수로 결합하여 안전하게 전달하는 자릿수 인코딩 및 경계값($num \ge 1000$) 정상 복원 기법 도입.
* **💺 미니 좌석 예약 시스템 (`seat_reserv_plus.c`)**
    * 배열 인덱스 제어 및 범위 초과 입력 방어, 모든 배열 요소 순회를 통한 실시간 만석 감지 및 자동 종료 시퀀스 구현.

---

### 🐍 Python Lab: 파이썬 고유 패러다임과 데이터 무결성 확보
> **상세 리드미 보기:** [Python README](./)

파이썬의 데이터 구조적 유연성을 학습하고, 파일 영속성(File I/O)과 객체 지향 프로그래밍(OOP)을 적용하여 정교한 비즈니스 로직을 빌드했습니다.

* **💵 자산 관리 프로그램 완성판 (`asset_manager_advanced.py`)**
    * **객체 지향 설계:** `class`와 `__init__` 함수를 활용하여 데이터와 기능이 유기적으로 결합한 도메인 모델 설계.
    * **데이터 무결성:** '리스트 내부의 딕셔너리' 복합 자료구조를 채택하여, 동일 키값 중복으로 인한 데이터 덮어쓰기(Overwrite) 문제를 완벽히 방어.
    * **데이터 영속성:** `csv` 모듈 기반의 파일 입출력을 연동하여 프로그램 종료 후에도 데이터가 유지되는 파일 영구 저장 로직 구현.
* **🎓 학생 관리 프로그램 모듈화 버전 (`student_manage_modular.py`)**
    * 제너레이터 표현식(Generator Expression)을 활용한 Pythonic한 루프 구현 및 `ZeroDivisionError` 방지 로직 적용.

---

## 💡 핵심 학습 성과 (Core Engineering Skills)

1.  **단일 책임 원칙 (SRP) 체득**
    * UI 로직(입출력 및 출력)과 핵심 비즈니스 로직(연산 및 데이터 가공)을 완벽하게 분리하여 코드의 가독성과 레고 블록 같은 재사용성을 확보했습니다.
2.  **철저한 방어적 프로그래밍 (Defensive Programming)**
    * 수학적 정의역 조건(로그의 진수 조건 $a > 0$, 제곱근 범위 $a \ge 0$) 및 오버플로우 방지 경계 조건($0 \le n \le 20$), 문자 오입력 가능성 등을 코드 레벨에서 엄격히 검증하여 시스템 다운을 예방했습니다.
3.  **I/O 및 메모리 메커니즘의 이해**
    * C언어의 로우레벨 입력 스트림 버퍼와 파이썬의 영속적 파일 데이터 핸들링의 차이를 이해하고, 상황에 맞는 올바른 예외 처리 방법을 습득했습니다.

---

  ### AWS Cloud Practitioner (CLF-C02) 핵심 개념 정리 (`AWS_CLF-C02_Notes.md`)
AWS 자격증 취득 및 클라우드 인프라 이해를 위해 시험 출제 포인트, 핵심 서비스 비교, 함정 선지 분석을 정리한 학습 기록입니다.  
Core cloud architecture concepts, AWS service comparisons, and exam-focused trouble-shooting notes for AWS CLF-C02.

#### ✨ 주요 학습 서비스 및 개념 (Key Concepts & Services)
- **High Availability & Fault Tolerance**: Multi-AZ 배포를 통한 단일 장애 지점(SPOF) 제거 및 가용성 향상 메커니즘
- **Database Architecture**: RDBMS(Aurora, RDS)의 ACID 트랜잭션 vs NoSQL(DynamoDB)의 유연한 스키마 및 수평적 확장성 비교
- **Global Content Delivery**: CloudFront(CDN)의 3대 요소(Origin, Edge Location, Distribution) 및 S3 정적 웹 호스팅 가속 기법
- **Cloud Migration Strategies**: AWS MGN(서버 전체 Lift-and-Shift) vs AWS DMS(DB 데이터 이전)의 적재적소 활용법
- **Serverless Event-Driven Architecture**: AWS Lambda의 실행 시간(Duration) 및 요청 수(Requests) 기반 Pay-as-you-go 요금 측정 체계

#### 🛠 핵심 가이드 & 매칭 팁 (Quick Reference Tips)
- **Multi-AZ vs Multi-Region/CloudFront**:
  - `Multi-AZ`: 고가용성(High Availability) 및 SPOF 방지 🎯
  - `Multi-Region / CloudFront`: 글로벌 지연 시간(Latency) 감소 🎯
- **Database Selection Standard**:
  - `관계형 (RDS, Aurora)`: 트랜잭션 정확도 및 복잡한 관계가 핵심인 시스템 (금융, 주문/결제)
  - `비관계형 (DynamoDB)`: 초고속 읽기/쓰기 및 대규모 트래픽 확장이 핵심인 시스템 (게이밍, IoT, SNS)
- **Migration Services**:
  - `AWS MGN`: 온프레미스 서버(OS + 파일시스템 + 앱) 통째로 EC2 복제 🚚
  - `AWS DMS`: 데이터베이스 내 데이터(Data)만 AWS DB 서비스로 동기화/이전 📊

#### 💡 주요 학습 내용 (Key Learning Contents)
- **클라우드 아키텍처 패턴 이해**: 온프레미스 인프라와 AWS 클라우드 환경의 구조적 차이를 파악하고 고가용성 아키텍처 설계 원리를 체득함.
- **오답 노트 기반의 문제 해결력 배양**: 오답 및 함정 선지(SQS vs SNS, DAX vs CloudFront 등) 분석을 통해 각 서비스의 고유 유스케이스(Use-Case)를 엄격하게 구분함.
- **서버리스(Serverless) 및 S3 정적 호스팅의 이점 파악**: 기존 EC2 유지 비용 대비 S3 정적 호스팅 및 Lambda의 경제성(비용 절감)과 무한 자동 스케일링 특성을 구체적으로 이해함.

```markdown
To be continued... 학습 진행도에 따라 본 로드맵은 실시간으로 업데이트됩니다.
