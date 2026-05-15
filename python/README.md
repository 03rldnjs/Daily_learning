# PYTHON Daily learning lab

파이썬을 공부하며 작성한 코드와 얻은 정보를 누적하는 폴더입니다.
This folder is an archive that collect the codes that I write and informations that I got. 

1. [student_management.py](./student_management.py)
   - 학생 관리 프로그램(student supervising/managing program)
   - 학생 추가, 성적 조회, 통계(총점, 평균, 최고점자) 기능 제공(you can use this program for insert student information, searching student's grade,and access to some statistics(total, avg, top scorer))
   - 활용 기술(used skills) : list, dictionary, while & for loop

   주요 학습 내용(key learning contents)
   - 파이썬의 기본 자료형 이해(Ex: 리스트, 딕셔너리) / understanding python's basic data types (Ex: list, dictionary)
   - 사용자 입력 처리 및 예외 처리 방법 / processing user's input and ways to process exceptional user's input

2. [student_management_advanced.py](./student_management_advanced.py)
   - [student_management.py]의 발전, 완성 버전 (advanced version of [student_managemet.py])
   - 함수 분리, 파이썬 스타일 for문 활용, bool형 변수 활용 추가 (Modularizing code, pythonic for loop usage, use bool type variable)
   - 활용 기술(used skills) : list, dictionary, while & for loop, bool type, function, for loop generator expression

   주요 학습 내용(key learning contents)
   - 함수 분리를 통한 역할 분담, 가독성 향상 / distributing the role and improving readablity by modulizing the code
   - for문 제너레이터 표현식 (total_grade = sum(s['grade'] for s in stu_grade_list)) / for loop Generator Expression
   - bool형 변수의 활용 / usage of bool type variables
  
3. [asset_manager.py](./asset_manager.py)
   - 자산 관리 프로그램의 초안(draft of asset managing program)
   - 수입/ 지출 내역 추가, 전체 내역 조회, 자산 현황 및 통계 조회 기능 제공(you can use this program for add income/expence details, view all details, view asset status and asset statistics
   - 활용 기술(used skills) : dictionary, while infinite loop, function, try - except, if-elif-else
  
   주요 학습 내용(key learning contents)
   - 1, 2에서의 주요 학습내용 복습
  
4. [asset_manager_advanced.py](./asset_manager_advanced.py)
   - [asset_manager.py]의 발전, 완성 버전 (advanced version of [asset_manager.py])
   - 파일 입출력 기능, class와 __init__함수 활용, key 중복으로 인한 덮어쓰기 문제 방지를 위한 리스트 내의 딕셔너리 활용, 초기 자본 재입력 방지를 위한 조건문 추가 등 기능 및 안정성 향상( improve functinality and stability by add file i/o function, using class and __init_ function, Dictionary within a list to prevent overwrite problem, add conditional statement to prevent reinput of first asset)
   - 활용 기술(used skills) : class and __init__function, dictionary within a list, file i/o funtion, csv module
  
   주요 학습 내용(key learning contents)
   - csv 모듈을 활용한 파일 입출력 기능 / file i/o funcion by csv module
   - 리스트 내부의 딕셔너리 / dictionary within a list
   - class와 __init__함수 / class and __init__function
  
To be continued...
  
// advanced version(powered by Gemini)
# 🐍 Python Daliy Learning Lab

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

### 3. 자산 관리 프로그램 (`asset_manager.py`)
개인의 수입과 지출을 기록하고 자산 현황을 체계적으로 분석하는 프로그램입니다.  
A personal asset management program designed to track income/expenses and analyze financial status.

#### ✨ 주요 기능 (Key Features)
- **내역 추가 (Add Transactions)**: 수입 및 지출 내역을 구분하여 금액과 상세 내용을 저장합니다.
- **전체 조회 (View All Details)**: 현재까지 기록된 모든 입출력 히스토리를 리스트 형태로 확인합니다.
- **자산 통계 (Asset Statistics)**: 현재 잔액, 총 수입/지출 합계 등 자산 현황에 대한 통계 데이터를 산출합니다.

#### 🛠 활용 기술 (Used Skills)
- **Data Structures**: `Dictionary`를 활용한 체계적인 데이터 구조 설계
- **Control Flow**: `while` 무한 루프와 `if-elif-else`를 통한 사용자 대화형 UI 구현
- **Error Handling**: `try-except` 구문을 활용하여 문자열 입력 등 잘못된 입력값에 대한 예외 처리

#### 💡 주요 학습 내용 (Key Learning Contents)
- **종합 복습 (Comprehensive Review)**: 이전 프로젝트들(1, 2)에서 익힌 자료 구조와 제어문의 실전 응용 능력을 배양함.
- **수학적 엄밀함 (Mathematical Rigor)**: 자산 계산 시 발생할 수 있는 논리적 오류를 방지하고, 정확한 통계 수치를 산출하기 위한 검증 로직 적용.
- **기능 모듈화 (Modularization)**: 수입, 지출, 통계 등 각 기능을 독립된 함수로 분리하여 코드의 가독성과 유지보수성을 극대화함.

### 4. 자산 관리 프로그램 완성판 (`asset_manager_advanced.py`)
클래스와 파일 입출력을 도입하여 데이터 영속성과 프로그램 안정성을 극대화한 최종 버전입니다.  
An advanced version of the asset manager, enhancing functionality and stability through OOP and File I/O.

#### ✨ 주요 기능 (Key Features)
- **파일 영구 저장 (File I/O)**: `csv` 모듈을 활용하여 프로그램 종료 후에도 자산 내역이 유지되도록 구현했습니다.
- **객체 지향 프로그래밍 (OOP)**: `class`와 `__init__` 함수를 사용하여 자산 관리 시스템을 구조화했습니다.
- **데이터 무결성 확보**: 리스트 내 딕셔너리 구조를 채택하여 Key 중복으로 인한 데이터 유실(Overwrite) 문제를 완벽히 해결했습니다.
- **초기 자본 보호**: 조건문을 추가하여 프로그램 재실행 시 초기 자본이 중복 입력되는 오류를 방지했습니다.

#### 🛠 활용 기술 (Used Skills)
- **Object-Oriented**: `class`, `__init__`, Methods
- **Data Structures**: `List` of `Dictionaries` (Advanced Data Handling)
- **File Management**: `csv` module, File Open/Write/Read
- **Logic**: Conditional statements for state management

#### 💡 주요 학습 내용 (Key Learning Contents)
- **객체 지향의 이해**: 클래스를 통한 데이터와 기능의 결합, 인스턴스화 과정 습득.
- **영속적 데이터 관리**: 메모리 내 휘발성 데이터를 물리 파일(`csv`)로 저장하고 불러오는 전체 프로세스 이해.
- **복합 자료구조 활용**: 리스트와 딕셔너리를 중첩하여 대량의 데이터를 효율적으로 관리하는 설계 능력 배양.
- **예외 상황 대응**: 초기화 로직 및 데이터 중복 등 실제 사용 시 발생할 수 있는 논리적 엣지 케이스(Edge Case) 처리.

## 🚀 To be continued...
학습 내용이 추가될 때마다 업데이트될 예정입니다.
This repository will be updated as my learning progresses.

