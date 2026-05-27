#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#define PI 3.14159265   // sin()함수에서 입력받은 각을 라디안으로 바꾸기 위한 기호 상수 선언 declare symbolic constants to translate angle into radian

void clear_buffer() {  // 문자 입력 시 발생할 무한 루프 오류를 방지하기 위한 함수
	while (getchar() != '\n');
}

// 메뉴 출력 함수
void print_menu() {
	printf("1. 팩토리얼\n");
	printf("2. 싸인\n");
	printf("3. 로그(base 10)\n");
	printf("4. 제곱근\n");
	printf("5. 순열(nPr)\n");
	printf("6. 조합(nCr)\n");
	printf("7. 종료\n");
}

// 메뉴 입력 함수
int menu_input() {
	int n;
	printf("메뉴를 선택하세요: ");
	if (scanf("%d", &n) != 1) {
		clear_buffer();

		return -1;
	}
	if (n > 7 || n < 1) {
		return -1;  // 범위 내에 존재하지 않는 정수가 들어와도 -1을 반환 return -1 when entered number is not in the menu range
	}
	// 따라서 잘못된 입력은 모두 -1이 반환되도록 설계됨 / so every exceptional input will return -1
	return n;
}

// 팩토리얼 계산 함수
long long calc_fact(int n) {   // 팩토리얼 계산 전용 함수 생성(매개변수 포함, long long형 반환) create function only for calculate factorial(include parameter, return long long type)
	long long result = 1;      // 팩토리얼의 계산 결과는 매우 클 수 있으므로 long long으로 선언하는 것이 안전함
	// declare by long long for result because result of factorial can be huge
	if (n > 20)
		printf("결과값이 너무 커서 정확하지 않을 수 있습니다.\n");
	for (int i = 1; i <= n; i++)
		result *= i;
	return result;             // 출력이 아닌 반환 return, not print
}

// 팩토리얼 입력 함수
int fact_input() {
	int n;
	while (1) {
		printf("정수를 입력하세요(0 ~ 20): ");   // 오버플로우를 방지하기 위해 입력할 수 있는 정수를 0부터 20 사이로 제한
		// restrict input in range 0 to 20 to avoid overflow (cause 21! is bigger than long long type max value)
		if (scanf("%d", &n) != 1) {
			printf("숫자만 입력할 수 있습니다. 다시 입력하세요.\n");

			clear_buffer();

			continue;
		}
		if (n < 0)
			printf("음수는 입력할 수 없습니다. 다시 입력하세요.\n");
		else if (n > 20)
			printf("21 이상의 정수는 오버플로우가 발생할 수 있습니다. 다시 입력하세요.\n");
		else
			break;
	}
	return n;
}

// 사인 입력 함수
double sine_input() {
	double a;
	while (1) {
		printf("각도를 입력하세요(0도~360도): ");
		if (scanf("%lf", &a) != 1) {
			printf("숫자만 입력할 수 있습니다. 다시 입력하세요.\n");
			clear_buffer();

			continue;
		}
		else if (a < 0.0 || a > 360.0) {
			printf("0도에서 360도 사이의 각을 입력해야 합니다. 다시 입력하세요.\n");
		}
		else
			break;
	}

	return a;
}

// 사인 계산 함수
double sine(double a) {
	double result; //sin()함수는 라디안을 기준으로 계산하므로 각도를 입력받은 경우 a * pi / 180을 해줘야 함.
	result = sin(a * PI / 180.0);  // 수정 사항 - sin()함수는 라디안을 기준으로 계산, 따라서 입력받은 각을 라디안으로 변환해주어야함.
	// adjustment - sin() function calculate base on radian, so we should translate angle to radian
	return result;
}

// 로그 입력 함수
double log_input() {
	double a;
	while (1) {
		printf("실수값을 입력하시오: ");
		if (scanf("%lf", &a) != 1) {
			printf("숫자만 입력할 수 있습니다. 다시 입력하세요.\n");
			clear_buffer();

			continue;
		}
		if (a <= 0.0)  // 수정 사항 - log는 진수가 0보다 클 때 정의되므로 0도 입력 오류에 포함됨.
			// adjustment - log funtion's value should be bigger than 0. so 0 for input number should be included in wrong input
			printf("입력 오류\n");  // means wrong input
		else {
			break;
		}
	}
	return a;
}

// 로그 계산 함수
double logBase10(double a) {
	double result;
	result = log10(a);

	return result;
}

// 제곱근 입력 함수
double root_input() {
	double a;
	while (1) {
		printf("실수를 입력하시오: ");
		if (scanf("%lf", &a) != 1) {
			printf("숫자만 입력할 수 있습니다. 다시 입력하세요.\n");
			clear_buffer();

			continue;
		}
		if (a < 0.0)  // 수정 사항 - 제곱근은 0보다 크거나 같을 때 정의되므로 0이 입력되어도 오류가 아님.
			// adjustment - square root is defined in 0 and bigger. so 0 for input number is not an wrong input
			printf("제곱근이므로 0이상의 실수를 입력해주세요.\n");
		else {
			break;
		}
	}
	return a;
}

// 제곱근 계산 함수
double root(double a) {
	double result;
	result = sqrt(a);

	return result;
}

// 순열 입력 함수
int permu_input(int *p_n, int *p_r) { // 포인터를 활용하는 방식으로 변경 change the code to use pointer
	while (1) {
		printf("n과 r을 입력하시오: ");
		if (scanf("%d %d", p_n, p_r) != 2) {
			printf("숫자만 입력할 수 있습니다. 다시 입력하세요.\n");
			clear_buffer();

			continue;
		}
		if (*p_n <= 0 || *p_r <= 0) 
			printf("0 이하의 수를 입력하면 안됩니다. 자연수를 입력하세요.\n");
		else if (*p_n > 20)
			printf("21 이상의 수는 오버플로우가 발생할 수 있습니다. 20 이하의 수를 입력해주세요.\n");
		else if (*p_n < *p_r)   // 순열 공식에 (n - r)!가 포함되므로 n이 반드시 r보다 커야함.
			// permutation formular includes (n -r)!. so n should be bigger than r
			printf("n이 r보다 작으면 안됩니다.다시 입력하세요.\n");
		else
			break;
	}
	return 1;
}

// 순열 계산 함수(팩토리얼 계산 함수 활용)
long long permutation(int n, int r) {
	long long result;

	result = calc_fact(n) / calc_fact(n - r);  // 수정 사항 -  동일한 계산을 함수에서 반복하는 것이 아닌 팩토리얼 계산 함수 활용
	// adjustment - not iterate same calculation in function, use factorial function / 중복 제거(DRY: Don't Repeat Yourself)
	return result;
}

// 조합 입력 함수
int combi_input(int *p_n, int *p_r) {
	while (1) {
		printf("n과 r을 입력하시오: ");
		if (scanf("%d %d", p_n, p_r) != 2) {
			printf("숫자만 입력할 수 있습니다. 다시 입력하세요.\n");
			clear_buffer();

			continue;
		}
		if (*p_n <= 0 || *p_r <= 0)
			printf("0 이하의 수를 입력하면 안됩니다. 자연수를 입력하세요.\n");
		else if (*p_n > 20)
			printf("21 이상의 수는 오버플로우가 발생할 수 있습니다. 20 이하의 수를 입력해주세요.\n");
		else if (*p_n < *p_r)  // 조합 공식에도 (n - r)!가 포함되므로 n이 반드시 r보다 커야함.
			// combination formular includes (n - r)!. so n should be bigger than r
			printf("n이 r보다 작으면 안됩니다.다시 입력하세요.\n");
		else
			break;
	}
	return 1;
}

// 조합 계산 함수(팩토리얼 계산 함수 활용)
long long combination(int n,int r) {
	long long result;
	result = calc_fact(n) / (calc_fact(r) * calc_fact(n - r));  // 수정 사항 -  동일한 계산을 함수에서 반복하는 것이 아닌 팩토리얼 계산 함수 활용
	// adjustment - not iterate same calculation in function, use factorial function / 중복 제거(DRY: Don't Repeat Yourself)
	return result;
}

// 메인 함수 (switch문 활용)
int main() {
	while (1) {
    // 순열, 조합 함수에 있는 포인터 변수에 넘겨져 다른 값이 덮어써질 것이지만 C언어에서는 변수를 반드시 초기화해야하므로 0으로 초기화
    // n, r will be overwrited by the entered values of permu_input() and combi_input() but C language require to initialize the variables so set n, r to 0
		int n = 0; 
		int r = 0;
		print_menu();
		switch (menu_input()) {
		case 1:
			printf("결과: %lld\n\n", calc_fact(fact_input()));
			break;
		case 2:
			printf("결과: %lf\n\n", sine(sine_input()));
			break;
		case 3:
			printf("결과: %lf\n\n", logBase10(log_input()));
			break;
		case 4:
			printf("결과: %lf\n\n", root(root_input()));
			break;
		case 5:
			if (permu_input(&n, &r) == 1) { // permu_input() 함수가 정상적으로 실행되어 1을 반환한 경우에만 결과 출력 print the result only if permu_input() return 1
				printf("결과: %lld\n\n", permutation(n, r));
			}
			break;
		case 6:
			if (combi_input(&n, &r) == 1) {
				printf("결과: %lld\n\n", combination(n, r));
			}
			break;
		case 7:
			printf("프로그램을 종료합니다.\n");
			return 0;
		default:
			printf("잘못된 입력입니다.\n");
			break;
		}
	}
	return 0;
}


// scientific_calculator_prime과의 차이점
// 순열, 조합 함수에서 C언어에서의 함수는 1개의 값만 return할 수 있는 문제때문에 활용한 편법을 보완함.
// 편법 - 
// if (r < 10)
//   return (n * 10 + r);
// else if (r >= 10)
//  return (n * 100 + r);
// 10을 기준으로 r을 구별한 뒤, 10 이상이면 100, 10 미만이면 10을 곱한 후 r과 더하여 반환
// 계산 함수에서 반환받은 값의 자릿수를 기준으로 n과 r을 다시 분리

// 포인터를 활용하면 해당 변수의 주소로 가서 값을 직접 바꾸므로 위와 같은 편법을 사용하지 않아도 됨.
// 복잡한 계산과 불필요한 사고 과정을 최소화할 수 있음
