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
| [**🎨 python_GUI**](./) | `Python`, GUI Library | *(To be updated)* 파이썬 기반 그래픽 사용자 인터페이스 연구 공간 |

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
    * 수학적 정의역 조건(로그의 진수 조건 $a > 0$, 제곱근 범위 $a \ge 0$) 및 오버플로우 방지 경계 조건($0 \le n \le 20$)을 코드 레벨에서 엄격히 검증하여 시스템 다운을 예방했습니다.
3.  **I/O 및 메모리 메커니즘의 이해**
    * C언어의 로우레벨 입력 스트림 버퍼와 파이썬의 영속적 파일 데이터 핸들링의 차이를 이해하고, 상황에 맞는 올바른 예외 처리 방법을 습득했습니다.

---

## 🚀 Future Roadmap: Python GUI Lab
* 현재 축적된 C언어의 엄밀한 계산 엔진 로직과 파이썬의 객체 지향 아키텍처를 바탕으로, **사용자 친화적인 그래픽 인터페이스(GUI)** 환경을 구축하는 연구를 진행할 예정입니다. (Tkinter, PyQt 등 활용 예정)

```markdown
To be continued... 학습 진행도에 따라 본 로드맵은 실시간으로 업데이트됩니다.
