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


advanced version(powered by Gemini)
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

## 🚀 To be continued...
학습 내용이 추가될 때마다 업데이트될 예정입니다.
This repository will be updated as my learning progresses.
