# C language Daily learning lab

C언어를 공부하며 작성한 코드와 얻은 정보를 누적하는 폴더입니다.
This folder is an archive that collect the codes that I write and informations that I got while learning C language.

1. [scientific_calculator.c](./scientific_calculator.c)
   - math.h 파일을 활용한 공학용 계산기 프로그램 (scientific calculator program using math.h headerfile)
   - 팩토리얼, 사인, 상용로그, 제곱근, 순열, 조합 기능 제공(this program is provides factorial, sin, log(base10), square root, permutation, combination calculating function)
   - 활용 기술(used skills) : factorial Algorithm, sin(), sqrt() based on math.h
  
   주요 학습 내용(key learning contents)
   - C언어의 math.h 헤더파일 활용 / using math.h header file
   - 사용자 입력 예외 처리 방법 / processing user's exceptional input using while(1) infinite loop
   - 모듈화를 위한 함수 분리 / Separation of functions for modularization
  
2. [scientific_calculator_advanced.c](./scientific_calculator_advanced.c)
   - [scientific_calculator.c]의 발전, 완성 버전 (advanced version of [scientific_calculator.c])
   - 기호 상수 활용, sin() 함수 라디안 변환 로직, 함수 재사용(순열, 조합에서의 팩토리얼 계산), 수학적 엄밀성 향상(log함수 0 입력 배제, sqrt 0 입력 포함 등) ( using symbolic constants, sin() function radian traslation logic, improved function reusablity(factorial calculation in permutation, combination), Handling mathmatical edge cases(rule out input 0 in log, include input 0 in sqrt etc.)
  
   주요 학습 내용(key learning contents)
   - 출력, 계산 함수의 분리를 통한 함수 재사용성 향상 / enhanced function reusablity by seperate print function and calculate function + DRY(Don't repear yourself)
   - 기호 상수 활용을 통한 유연성 향상 / enhanced flexablity by using symbolic constants
   - 여러 입력 오류 방지 / prevent various input error program quit

3. [seat_reserv_plus.c](./seat_reserv_plus.c)
   - 배열을 활용한 미니 좌석 예약 시스템 (mini seat reservation system using arrangement)
   - 기본적인 좌석 예약 시스템에 여러 입력 오류 방지 로직 추가 (add several input error prevention logic in the basic seat reservation system)
   - 예약되지 않은 좌석은 0, 예약된 좌석은 1로 처리, 모든 좌석이 예약된 경우 프로그램 종료

   주요 학습 내용(key learning contents)
   - c언어에서의 배열 활용 / using c language arrangement for the first time
   - 나타날 수 있는 입력 오류(ex. 범위 밖 숫자 입력, 문자 입력, 예약된 좌석 입력 등) 방지 로직 형성 / create preventing input error logic(ex. input the number that is out of the range, input character, input the seat that is already reserved)
   - 모든 좌석이 예약된 경우 프로그램을 종료시키는 로직 형성 / create the logic that can exit the program when all the seats are reserved
  
To be continued...

// advanced version(powered by Gemini)
# 💻 C Language Daily Learning Lab

C언어를 공부하며 작성한 코드와 얻은 정보를 누적하는 폴더입니다.
This folder is an archive of the code I've written and the information I've gathered while learning the C language.

---

## 📂 주요 프로젝트 (Main Projects)

### 1. 공학용 계산기 (`scientific_calculator.c`)
`math.h` 헤더 파일을 활용하여 다양한 수학적 연산을 수행하는 CLI 프로그램입니다.
A scientific calculator program using the `math.h` header file for various mathematical operations.

#### ✨ 주요 기능 (Key Features)
- **수학 연산 (Mathematical Ops)**: 팩토리얼(Factorial), 사인(Sin), 상용로그(Log base 10), 제곱근(Square Root) 제공.
- **확률과 통계 (Probability)**: 순열(Permutation, nPr) 및 조합(Combination, nCr) 계산 기능 제공.

#### 🛠 활용 기술 (Used Skills)
- **Library**: `math.h` (`sin()`, `log10()`, `sqrt()`)
- **Algorithms**: Factorial Calculation, Permutation & Combination logic.
- **Data Types**: `long long` (To handle large numbers in factorial calculation).

#### 💡 주요 학습 내용 (Key Learning Contents)
- **헤더 파일 활용**: C언어 표준 라이브러리(`math.h`)의 수학 함수 사용법 숙지.
- **예외 처리 (Exception Handling)**: `while(1)` 무한 루프를 활용하여 잘못된 사용자 입력(음수 입력 등) 시 프로그램 종료 방지.
- **코드 모듈화 (Modularization)**: 각 기능을 독립적인 함수로 분리하여 코드 가독성과 유지보수성 향상.

---

### 2. [scientific_calculator_advanced.c](./scientific_calculator_advanced.c)
- **논리적 정확도와 코드 재사용성을 극대화한 최종 완성본**
- **Advanced Features**:
  - **Function Reusability**: `calc_fact()` 함수를 별도로 정의하여 순열(nPr) 및 조합(nCr) 계산 시 코드 중복을 제거함.
  - **Mathematical Accuracy**: 
    - `sin()` 함수 호출 시 Degree 단위를 Radian 단위로 변환하는 기호 상수(`PI`) 로직 적용.
    - 로그 및 제곱근 함수의 정의역(Domain)에 따른 정교한 입력값 검증 수행.
    - 오버플로우 방지를 위한 입력 제어 수행(팩토리얼 long long형 오버플로우)
  - **Modular Architecture**: 계산 로직(반환형 함수)과 출력 로직(void형 함수)을 분리하여 프로그램 구조를 최적화함.

### 3. 미니 좌석 예약 시스템 (`seat_reserv_plus.c`)
배열을 활용하여 좌석 상태를 관리하고, 다양한 사용자 입력 오류를 견고하게 방지하는 예약 프로그램입니다.  
A mini seat reservation system using arrays, featuring robust error-prevention logic for various user inputs.

#### ✨ 주요 기능 (Key Features)
- **좌석 상태 관리 (Seat Tracking)**: 예약되지 않은 좌석은 `0`, 예약된 좌석은 `1`로 이진 처리하여 실시간 상태를 관리합니다.
- **실시간 만석 감지**: 모든 좌석이 예약되는 즉시 가용 좌석이 없음을 인지하고 프로그램을 자동으로 종료합니다.
- **철저한 예외 처리**: 범위 밖의 숫자 입력, 이미 예약된 좌석 선택, 그리고 문자열 입력으로 인한 무한 루프 오류를 방지합니다.

#### 🛠 활용 기술 (Used Skills)
- **Data Structures**: 1차원 배열(Array)을 활용한 상태 데이터 매핑
- **Control Flow**: `while(1)` 무한 루프 및 조건문 기반의 상태 플래그(Flag) 제어
- **Buffer Management**: `scanf` 입력 오류 시 입력 버퍼를 비워주는 예외 처리 로직

#### 💡 주요 학습 내용 (Key Learning Contents)
- **배열 구조의 이해**: C언어에서 연속된 메모리 공간(배열)을 선언하고 인덱스를 제어하는 방법 숙지.
- **방어적 코드 설계 (Defensive Coding)**: 잘못된 입력(범위 초과, 문자 입력 등)이 시스템에 미치는 영향을 파악하고, 이를 필터링하는 방어 로직 형성.
- **자동 종료 메커니즘 (Exit Logic)**: 배열의 모든 요소를 순회하여 특정 조건(만석)을 만족할 때 안전하게 탈출하는 제어 흐름 구현.

## 🚀 To be continued...
학습 내용이 추가될 때마다 업데이트될 예정입니다.
This repository will be updated as my learning progresses.
