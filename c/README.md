# C language Daily learning lab

C언어를 공부하며 작성한 코드와 얻은 정보를 누적하는 폴더입니다.
This folder is an archive that collect the codes that I write and informations that I got while learning C language.

1. [scientific_calculator.c](./scientific_calculator.c)
   - math.h 파일을 활용한 공학용 계산기 프로그램 (scientific calculator program using math.h headerfile)
   - 팩토리얼, 사인, 상용로그, 제곱근, 순열, 조합 기능 제공(this program is provides factorial, sin, log(base10), square root, permutation, combination calculating function)
   - 활용 기술(used skills) : factorial Algorithm, sin(), sqrt() based on math.h
  
   주요 학습 내용(key learning contents)
   - C언어의 math.h 헤더파일 활용 / using math.h header file
   - 사용자 입력 예외 처리 방법 / process user's exceptional input using while(1) infinite loop
   - 모듈화를 위한 함수 분리 / Separation of functions for modularization

---
  
2. [scientific_calculator_advanced.c](./scientific_calculator_advanced.c)
   - [scientific_calculator.c]의 발전, 완성 버전 (advanced version of [scientific_calculator.c])
   - 기호 상수 활용, sin() 함수 라디안 변환 로직, 함수 재사용(순열, 조합에서의 팩토리얼 계산), 수학적 엄밀성 향상(log함수 0 입력 배제, sqrt 0 입력 포함 등) ( using symbolic constants, sin() function radian traslation logic, improved function reusablity(factorial calculation in permutation, combination), Handling mathmatical edge cases(rule out input 0 in log, include input 0 in sqrt etc.)
  
   주요 학습 내용(key learning contents)
   - 출력, 계산 함수의 분리를 통한 함수 재사용성 향상 / enhanced function reusablity by seperate print function and calculate function + DRY(Don't repeat yourself)
   - 기호 상수 활용을 통한 유연성 향상 / enhanced flexablity by using symbolic constants
   - 여러 입력 오류 방지 / prevent various input error program quit

---

3. [scientific_calculator_prime.c](./scientific_calculator_prime.c)
   - [scientific_calculator_advanced.c]의 최종 진화 버전 (final evolution version of [scientific_calculator_advanced.c])
   - 함수의 단일 기능 원칙과 함수 재사용성 향상을 위한 수정 (revise the program for reusalbility of function and Single Responsibility Principle (SRP))
   - 입력 오류 시 버퍼 청소 기능 추가 (add the buffer clear function when the wrong value is entered)

   주요 학습 내용(key learning contents)
   - 1함수 1기능 원칙 준수 / conform the Single Responsibility Principle(SRP)
   - getchar()함수를 활용한 입력 버퍼 청소 / clear the input buffer using getchar() function
   - scanf와 getchar()함수의 작동 매커니즘 이해 / understand the mechanism of scanf() and getchar() function
  
---

4. [seat_reserv_plus.c](./seat_reserv_plus.c)
   - 배열을 활용한 미니 좌석 예약 시스템 (mini seat reservation system using array)
   - 기본적인 좌석 예약 시스템에 여러 입력 오류 방지 로직 추가 (add several input error prevention logic in the basic seat reservation system)
   - 예약되지 않은 좌석은 0, 예약된 좌석은 1로 처리, 모든 좌석이 예약된 경우 프로그램 종료

   주요 학습 내용(key learning contents)
   - c언어에서의 배열 활용 / using c language array for the first time
   - 나타날 수 있는 입력 오류(ex. 범위 밖 숫자 입력, 문자 입력, 예약된 좌석 입력 등) 방지 로직 형성 / create preventing input error logic(ex. input the number that is out of the range, input character, input the seat that is already reserved)
   - 모든 좌석이 예약된 경우 프로그램을 종료시키는 로직 형성 / create the logic that can exit the program when all the seats are reserved

---

5. [pointer_prac.c](./pointer_prac.c)
   - 포인터의 원리를 이해하기 위한 코드 / code for understand principle of pointer

   주요 학습 내용(key learning contents)
   - 포인터가 선언된 자료형에 따라 어떤 차이를 보이는지 확인 / check the difference of result when declared types are different
   - 포인터를 활용할 때 *과 &의 역할 이해 / understand the role of * and & when using pointer

---

6. [scientific_calculator_pointer](./scientific_calculator_pointer)
   - [scientific_calculator_prime]의 단점이었던 순열, 조합함수에서의 편법 사용을 포인터를 통해 보완 / make up the shortcoming of [scientific_calculator_prime](use expedient in permutation and combination function)
   - 포인터를 실제 프로그램에 적용 경험
  
   주요 학습 내용(key learning contents)
   - c언어의 특징 중 하나인 함수가 하나의 값만 반환할 수 있다는 점을 포인터를 활용하여 해결 / solve the problem of C language's 1 function 1 return with pointer
   - 포인터의 작동 매커니즘 이해 / understand the mechanism of pointer
   - 포인터를 활용하는데 필요한 기호의 역할 이해, 포인터 선언 방식과 스타일 습득 / understand the role of * and & when using pointer, acquire the way and style when declare the pointer variables.
  
7. [CT_lv1_videoplayer.c](./CT_lv1_videoplayer.c)
   - 코딩테스트 레벨 1 문제 풀이(PCCP 기출문제) / solve the coding test lvl.1 question(PCCP previous question)
   - 비디오 플레이어 기능 구현(10초 단위 이동(prev, next), 오프닝 건너뛰기, 예외 처리(ex. 10초 이동 후 시점이 오프닝 구간인 경우)) / realize the fuction of video player(moving 10sec, skip the opening, processing the exceptions)
   - 문자열 입력을 변환하여 계산 -> 다시 문자열로 변형하여 출력 / string input -> process and caculate, translate -> print the string

   주요 학습 내용(key learning contents)
   - 포인터 배열 활용, 문자열 읽기/쓰기, 시간 처리, 코드 모듈화, 다양한 예외 처리
   - 코드 함수 분리(모듈화), 함수 원형 정의, 비디오 플레이어에 발생할 수 있는 다양한 예외 고려 및 처리, 문자열 처리(string.h 활용)
   - 코딩 테스트 기출문제 경험을 통한 실력 파악 및 객관화

---

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

### 2. 공학용 계산기 발전 버전 (`scientific_calculator_advanced.c`)
- **논리적 정확도와 코드 재사용성을 극대화한 최종 완성본**
- **Advanced Features**:
  - **Function Reusability**: `calc_fact()` 함수를 별도로 정의하여 순열(nPr) 및 조합(nCr) 계산 시 코드 중복을 제거함.
  - **Mathematical Accuracy**: 
    - `sin()` 함수 호출 시 Degree 단위를 Radian 단위로 변환하는 기호 상수(`PI`) 로직 적용.
    - 로그 및 제곱근 함수의 정의역(Domain)에 따른 정교한 입력값 검증 수행.
    - 오버플로우 방지를 위한 입력 제어 수행(팩토리얼 long long형 오버플로우)
  - **Modular Architecture**: 계산 로직(반환형 함수)과 출력 로직(void형 함수)을 분리하여 프로그램 구조를 최적화함.

---

### 3. 공학용 계산기 고도화 버전 (`scientific_calculator_prime.c`)
단일 책임 원칙(SRP)을 기반으로 입출력 로직과 연산 엔진을 완벽히 분리하고, 버퍼 비우기를 통해 문자 입력 예외까지 통제한 공학용 계산기입니다.  
An advanced scientific calculator that completely decouples I/O from core logic using SRP, featuring robust input buffer management.

#### ✨ 주요 기능 (Key Features)
- **다기능 공학 연산**: 팩토리얼, 삼각함수($\sin$), 상용로그($\log_{10}$), 제곱근, 순열($_nP_r$), 조합($_nC_r$) 연산을 지원합니다.
- **철저한 단일 책임 원칙 (SRP)**: 각 연산마다 입력 검증 함수(`_input`)와 순수 연산 함수를 독립적으로 분리하여 모듈성을 극대화했습니다.
- **무한 루프 방지 (Buffer Cleansing)**: 사용자가 숫자가 아닌 문자를 입력했을 때 `scanf` 버퍼에 남아있는 쓰레기 값을 `clear_buffer()`로 제거하여 무한 루프 현상을 원천 차단했습니다.
- **안정적인 데이터 전송**: 두 개의 입력값($n, r$)을 연산 함수로 안전하게 전달하기 위해 조건부 자릿수 인코딩 방식을 도입했습니다.

#### 🛠 활용 기술 (Used Skills)
- **Architecture**: 단일 책임 원칙(Single Responsibility Principle)에 입각한 기능별 함수 분리
- **Input Validation**: `scanf` 반환값 검증 및 데이터 범위($0 \le n \le 20$) 제한
- **Low-level I/O**: `getchar()`를 활용한 표준 입력 버퍼(`stdin`) 초기화 로직 구현
- **Math Library**: `math.h` 라이브러리를 활용한 고차 수학 연산 및 라디안 변환 상수 적용

#### 💡 주요 학습 내용 (Key Learning Contents)
- **함수 단일 기능 원칙 (SRP) 체득**: 하나의 함수가 하나의 역할(입력 검증 또는 순수 계산)만 수행하도록 설계하여 코드의 가독성과 재사용성을 향상함.
- **I/O 스트림 및 버퍼의 이해**: C언어 입력 시스템에서 문자 입력 시 발생하는 형식 지정자 오류 메커니즘을 파악하고 해결책을 제시함.
- **수학적 엄밀함 (Mathematical Rigor)**: 순열·조합의 수학적 성립 조건($n \ge r$) 및 로그의 진수 조건 등을 코드로 엄격하게 구현하여 실행 안정성을 확보함.
- **중복 제거 (DRY 원칙)**: 복잡한 확률 연산(순열, 조합)의 하위 로직에서 기존에 구현된 `calc_fact` 함수를 재사용함으로써 코드 중복을 최소화함.

---

### 4. 미니 좌석 예약 시스템 (`seat_reserv_plus.c`)
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

---

### 5. 포인터 기초 및 원리 실습 (`pointer_prac.c`)
C언어의 핵심인 포인터의 메모리 참조 메커니즘을 이해하고, 자료형에 따른 주소 연산의 차이를 분석한 실습 코드입니다.  
A foundational practice code exploring C pointer mechanisms, address operations by data types, and reference operators.

#### ✨ 주요 기능 (Key Features)
- **주소 및 참조 연산 실습**: 주소 연산자(`&`)와 역참조 연산자(`*`)를 활용하여 변수의 메모리 주소에 직접 접근하고 값을 제어합니다.
- **자료형별 포인터 특성 비교**: `int*`, `char*`, `double*` 등 선언된 자료형에 따라 포인터가 메모리를 해석하고 이동하는 크기의 차이를 직접 확인합니다.

#### 🛠 활용 기술 (Used Skills)
- **Memory Management**: 메모리 주소(Address)와 값(Value)의 개념 분리 및 매핑
- **Operators**: 주소 추출 연산자(`&`) 및 간접 참조 연산자(`*`)의 상호작용 이해
- **Pointer Arithmetic**: 자료형 크기(Type Size)에 따른 포인터 주소 연산 원리 파악

#### 💡 주요 학습 내용 (Key Learning Contents)
- **참조와 역참조의 이해**: 변수의 메모리 공간 주소를 가리키는 포인터의 개념을 정립하고, `*` 연산자를 통해 실제 데이터에 접근하는 메커니즘을 체득함.
- **자료형(Data Type)과 포인터의 관계**: 포인터 변수 자체의 크기는 동일하더라도, 가리키는 대상의 자료형에 따라 주소 증가 단위 및 메모리 참조 범위가 달라짐을 인지함.
- **포인터 기반 리팩토링의 발판**: 이전에 복합 반환값 전송을 위해 자릿수를 인코딩했던 편법 로직을 주소 참조 방식(Call by Reference)으로 개선할 수 있는 이론적 기반을 마련함.

---

### 6. 포인터 기반 공학용 계산기 (`scientific_calculator_pointer.c`)
포인터 메커니즘을 실제 프로그램에 적용하여, 기존 버전의 한계였던 다중 반환값 전송 문제를 주소 참조 방식으로 완벽히 보완한 고도화 버전입니다.  
An upgraded scientific calculator that replaces previous encoding expedients with pointer-based Call-by-Reference to handle multiple inputs effectively.

#### ✨ 주요 기능 (Key Features)
- **주소 참조 기반 입력 시스템 (Call by Reference)**: 순열과 조합 함수에서 $n$과 $r$ 두 개의 입력값을 포인터 매개변수를 통해 안전하고 직관적으로 메인 로직에 전달합니다.
- **구조적 결함 보완**: 임시 자릿수 인코딩 방식을 제거하고 C언어 표준 패러다임에 맞는 포인터 제어를 도입하여 잠재적 엣지 케이스(Overflow 및 데이터 유실)를 원천 차단했습니다.

#### 🛠 활용 기술 (Used Skills)
- **Memory Address Mapping**: 포인터 변수 선언 및 메모리 주소 상호작용 활용
- **Parameter Passing**: 주소 전달 방식을 통한 다중 데이터 참조 및 수정
- **Code Refactoring**: 기존 편법 로직을 표준 객체 지향 및 구조적 코드로 개선

#### 💡 주요 학습 내용 (Key Learning Contents)
- **C언어 반환 제약 극복**: "함수는 오직 하나의 값만 반환할 수 있다"는 C언어의 구조적 특징을 포인터 주소 참조 방식을 통해 우아하게 해결함.
- **포인터 작동 메커니즘의 실전 적용**: 이론으로만 배웠던 주소 연산자(`&`)와 역참조 연산자(`*`)를 실제 복잡한 프로그램 로직에 적용하며 구체적인 구동 원리를 체득함.
- **안정적인 코딩 스타일 정립**: 포인터 변수의 선언 방식과 참조 스타일을 올바르게 습득하여, 메모리에 안전하게 접근하고 가독성을 높이는 방어적 코딩 습관을 형성함.
- **지속 가능한 소프트웨어 개발**: 기술적 부채(Technical Debt)였던 과거의 임시 코드를 새로운 기술을 통해 스스로 리팩토링함으로써 소프트웨어의 점진적 발전 과정을 경험함.

### 7. PCCP 기출문제: 동영상 재생기 (`CT_lv1_videoplayer.c`)
문자열 형식의 시간 데이터를 파싱 및 연산하고, 오프닝 건너뛰기 등 복잡한 조건문과 예외 처리를 구현한 코딩테스트 레벨 1 풀이 소스코드입니다.  
A solution for the PCCP Level 1 coding test question, featuring string-to-time conversion, video control logic, and meticulous exception handling.

#### ✨ 주요 기능 (Key Features)
- **시간 데이터 포맷 변환**: `mm:ss` 형태의 문자열 입력을 초(Second) 단위 정수로 변환하여 계산한 뒤, 출력 시 다시 문자열 포맷으로 재변환합니다.
- **비디오 컨트롤 로직**: 10초 앞/뒤 이동(`prev`, `next`) 및 가용 범위를 벗어날 시의 타임라인 제한 기능을 제공합니다.
- **오프닝 자동 건너뛰기**: 이동 후의 시점이나 초기 시점이 오프닝 구간(`op_start` ~ `op_end`) 내에 위치할 경우, 오프닝이 끝나는 시점으로 자동 점프하는 예외 처리를 수행합니다.

#### 🛠 활용 기술 (Used Skills)
- **String Manipulation**: `string.h` 라이브러리를 활용한 문자열 읽기/쓰기 및 파싱
- **Pointer Array**: 문자열 명령어 배열 처리를 위한 포인터 배열 활용
- **Code Architecture**: 함수 원형(Prototype) 정의 및 기능별 함수 분리(모듈화)
- **Time Arithmetic**: 분/초 단위를 단일 기준(초)으로 통합하여 연산하는 로직 설계

#### 💡 주요 학습 내용 (Key Learning Contents)
- **문자열 처리 능력 향상**: C언어에서 가장 까다로운 영역 중 하나인 문자열 데이터를 정수형 데이터로 변환하고, 포인터 배열을 제어하는 실전 감각을 익힘.
- **철저한 예외 상황 시뮬레이션**: 10초 이동 후의 시점이 오프닝 구간에 걸치는 경우, 동영상 시작/종료 지점을 이탈하는 경우 등 발생 가능한 모든 엣지 케이스(Edge Case)를 고려한 방어적 흐름 설계.
- **구조적 모듈화 프로그래밍**: 코딩테스트 환경에서도 스파게티 코드를 지양하고, 함수 원형 선언과 기능별 분리를 통해 가독성과 구조적 완성도를 높임.
- **객관적 실력 점검 및 피드백**: 실제 공인 코딩테스트(PCCP) 기출문제를 제한된 조건 속에서 해결해 보며, 현재 나의 구현 능력을 객관적으로 파악하고 향후 학습 방향성을 설정함.

---

## 🚀 To be continued...
학습 내용이 추가될 때마다 업데이트될 예정입니다.
This repository will be updated as my learning progresses.
