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
int permu_input() {
	int n, r;
	while (1) {
		printf("n과 r을 입력하시오: ");
		if (scanf("%d %d", &n, &r) != 2) {
			printf("숫자만 입력할 수 있습니다. 다시 입력하세요.\n");
			clear_buffer();

			continue;
		}
		if (n <= 0 || r <= 0)
			printf("0 이하의 수를 입력하면 안됩니다. 자연수를 입력하세요.\n");
		else if (n > 20)
			printf("21 이상의 수는 오버플로우가 발생할 수 있습니다. 20 이하의 수를 입력해주세요.\n");
		else if (n < r)   // 순열 공식에 (n - r)!가 포함되므로 n이 반드시 r보다 커야함.
			// permutation formular includes (n -r)!. so n should be bigger than r
			printf("n이 r보다 작으면 안됩니다.다시 입력하세요.\n");
		else
			break;
	}
	if (r < 10)
		return (n * 10 + r);
	else if (r >= 10)
		return (n * 100 + r);
}

// 순열 계산 함수(팩토리얼 계산 함수 활용)
long long permutation(int num) {
	int n, r;
	if (num / 100 <= 20 && num % 100 >= 10) {
		n = num / 100;
		r = num % 100;
	}
	else {
		n = num / 10;
		r = num % 10;
	}
	long long result;

	result = calc_fact(n) / calc_fact(n - r);  // 수정 사항 -  동일한 계산을 함수에서 반복하는 것이 아닌 팩토리얼 계산 함수 활용
	// adjustment - not iterate same calculation in function, use factorial function / 중복 제거(DRY: Don't Repeat Yourself)
	return result;
}

// 조합 입력 함수
int combi_input() {
	int n, r;
	while (1) {
		printf("n과 r을 입력하시오: ");
		if (scanf("%d %d", &n, &r) != 2) {
			printf("숫자만 입력할 수 있습니다. 다시 입력하세요.\n");
			clear_buffer();

			continue;
		}
		if (n <= 0 || r <= 0)
			printf("0 이하의 수를 입력하면 안됩니다. 자연수를 입력하세요.\n");
		else if (n > 20)
			printf("21 이상의 수는 오버플로우가 발생할 수 있습니다. 20 이하의 수를 입력해주세요.\n");
		else if (n < r)  // 조합 공식에도 (n - r)!가 포함되므로 n이 반드시 r보다 커야함.
			// combination formular includes (n - r)!. so n should be bigger than r
			printf("n이 r보다 작으면 안됩니다.다시 입력하세요.\n");
		else
			break;
	}
	if (r < 10)
		return (n * 10 + r);
	else if (r >= 10)
		return (n * 100 + r);
}

// 조합 계산 함수(팩토리얼 계산 함수 활용)
long long combination(int num) {
	int n, r;
	if (num / 100 <= 20 && num % 100 >= 10) {
		n = num / 100;
		r = num % 100;
	}
	else {
		n = num / 10;
		r = num % 10;
	}
	long long result;
	result = calc_fact(n) / (calc_fact(r) * calc_fact(n - r));  // 수정 사항 -  동일한 계산을 함수에서 반복하는 것이 아닌 팩토리얼 계산 함수 활용
	// adjustment - not iterate same calculation in function, use factorial function / 중복 제거(DRY: Don't Repeat Yourself)
	return result;
}

// 메인 함수 (switch문 활용)
int main() {
	int fact_num;
	double sine_num;
	double log_num;
	double root_num;
	int permu_num;
	int combi_num;
	long long result_1;
	double result_2;
	double result_3;
	double result_4;
	long long result_5;
	long long result_6;
	while (1) {
		print_menu();
		switch (menu_input()) {
		case 1:
			fact_num = fact_input();
			result_1 = calc_fact(fact_num);
			printf("결과: %lld\n\n", result_1);
			break;
		case 2:
			sine_num = sine_input();
			result_2 = sine(sine_num);
			printf("결과: %lf\n\n", result_2);
			break;
		case 3:
			log_num = log_input();
			result_3 = logBase10(log_num);
			printf("결과: %lf\n\n", result_3);
			break;
		case 4:
			root_num = root_input();
			result_4 = root(root_num);
			printf("결과: %lf\n\n", result_4);
			break;
		case 5:
			permu_num = permu_input();
			result_5 = permutation(permu_num);
			printf("결과: %lld\n\n", result_5);
			break;
		case 6:
			combi_num = combi_input();
			result_6 = combination(combi_num);
			printf("결과: %lld\n\n", result_6);
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
