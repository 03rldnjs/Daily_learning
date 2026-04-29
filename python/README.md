# PYTHON Daily learning lab

파이썬을 공부하며 작성한 코드와 얻은 정보를 누적하는 폴더입니다.
This folder is an archive that collect the codes that I write and informations that I got. 

1. [student_management.py](./student_management.py)
   - 학생 관리 프로그램(student supervising/managing program)
   - 학생 추가, 성적 조회, 통계(총점, 평균, 최고점자) 기능 제공(you can use this program for insert student information, searching student's grade,and access to some statistics(total, avg, top scorer))
   - 활용 기술(used skills) : list, dictionary, while & for loop

   주요 학습 내용(key learning contents)
   - 파이썬의 기본 자료형 이해(Ex: 리스트, 딕셔너리) / (understanding python's basic data types (Ex: list, dictionary))
   - 사용자 입력 처리 및 예외 처리 방법 / processing user's input and ways to process exceptional user's input

2. [student_management_advanced.py](./student_management_advanced.py)
   - [student_management.py]의 발전, 완성 버전 (advanced version of [student_managemet.py])
   - 함수 분리, 파이썬 스타일 for문 활용, bool형 변수 활용 추가 (Modularizing code, pythonic for loop usage, use bool type variable)
   - 활용 기술(used skills) : list, dictionary, while & for loop, bool type, function, for loop generator expression

   주요 학습 내용(key learning contents)
   - 함수 분리를 통한 역할 분담, 가독성 향상 / enhanced readability and readability by Modularizing code
   - for문 제너레이터 표현식 (total_grade = sum(s['grade'] for s in stu_grade_list)) / for loop Generator Expression
   - bool형 변수의 활용 / usage of bool type variables

advanced version(powered by Gemini)
# 🐍 Python Learning Lab

파이썬을 공부하며 작성한 코드와 얻은 정보를 누적하는 폴더입니다.
This folder is an archive of the code I've written and the information I've gathered while studying Python.

---

## 📂 주요 프로젝트 (Main Projects)

### 1. 학생 관리 프로그램 (`student_management.py`)
학생 정보를 효율적으로 관리하고 통계를 산출하는 프로그램입니다.
A student supervising/managing program that provides features for information entry and statistics.

#### ✨ 주요 기능 (Key Features)
- **학생 추가 (Insert Student Info)**: 학생의 학번, 이름, 성적을 입력받아 저장합니다.
- **성적 조회 (Search Grade)**: 특정 학번을 입력하여 해당 학생의 성적을 확인합니다.
- **통계 출력 (Statistics)**: 전체 학생의 총점, 평균, 최고 득점자를 출력합니다.

#### 🛠 활용 기술 (Used Skills)
- **Data Structures**: `List`, `Dictionary`
- **Control Flow**: `while` & `for` loops, `if-elif-else`
- **Advanced**: `try-except` (Exception Handling), `lambda` expressions

#### 💡 주요 학습 내용 (Key Learning Contents)
- **파이썬 기본 자료형 이해**: 리스트와 딕셔너리의 구조 및 활용법 학습.
- **사용자 입력 및 예외 처리**: 숫자가 아닌 값 등 잘못된 사용자 입력에 대비한 프로그램의 견고성 확보.
- **C vs Python**: 인덱스 기반 접근과 파이썬의 언패킹(Unpacking) 방식 차이 인지.

---

### 2. 학생 관리 프로그램 - 모듈화 버전 (`student_manage_modular.py`)
기존 코드를 함수 단위로 분리하여 가독성과 재사용성을 높인 업그레이드 버전입니다.

#### 🛠 Refactoring Points (개선 사항)
- **Function Decomposition**: 검색 로직과 통계 계산 로직을 별도의 함수(`grade_search`, `sum_avg`)로 추출(Extract Method).
- **Efficiency**: `break`문을 적절히 사용하여 불필요한 반복(Unnecessary iteration)을 제거하고 효율성을 높임.
- **Robustness**: 데이터가 비어있을 경우 발생할 수 있는 `ZeroDivisionError`를 사전에 방지하는 로직 추가.
- **Readable Comments**: 한/영 주석을 병기하여 코드의 의도를 명확히 설명함.

---

## 🚀 To be continued...
학습 내용이 추가될 때마다 업데이트될 예정입니다.
This repository will be updated as my learning progresses.

