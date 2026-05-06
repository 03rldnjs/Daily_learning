#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#define PI 3.14159265   // sin()함수에서 입력받은 각을 라디안으로 바꾸기 위한 기호 상수 선언 declare symbolic constants to translate angle into radian

int menu() {
	int n;
	printf("1. 팩토리얼\n");
	printf("2. 싸인\n");
	printf("3. 로그(base 10)\n");
	printf("4. 제곱근\n");
	printf("5. 순열(nPr)\n");
	printf("6. 조합(nCr)\n");
	printf("7. 종료\n");
	printf("선택해주세요: ");
	scanf("%d", &n);

	return n;
}

long long calc_fact(int n) {   // 팩토리얼 계산 전용 함수 생성(매개변수 포함, long long형 반환) create function only for calculate factorial(include parameter, return long long type)
	long long result = 1;      // 팩토리얼의 계산 결과는 매우 클 수 있으므로 long long으로 선언하는 것이 안전함
	// declare by long long for result because result of factorial can be huge
	if (n > 20)
		printf("결과값이 너무 커서 정확하지 않을 수 있습니다.\n");
	for (int i = 1; i <= n; i++)
		result *= i;
	return result;             // 출력이 아닌 반환 return, not print
}

void factorial() {             // 팩토리얼 계산 결과를 출력하기 위한 함수 생성 create function to print the result of factorial calculation
	int n;      			   // 입력값은 int로 선언해도 문제 없음 declare in int is big enough for input number
	while(1){
		printf("정수를 입력하세요(0 ~ 20): ");   // 오버플로우를 방지하기 위해 입력할 수 있는 정수를 0부터 20 사이로 제한
		// restrict input in range 0 to 20 to avoid overflow (cause 21! is bigger than long long type max value)
		scanf("%d", &n);
		if ( n < 0 ) 
			printf("음수는 입력할 수 없습니다. 다시 입력하세요.\n");
		else if ( n > 20 )
			printf("21 이상의 정수는 오버플로우가 발생할 수 있습니다. 다시 입력하세요.\n");
		else
			break;
	}
	printf("결과: %lld\n\n", calc_fact(n));
}

//sin()함수는 라디안을 기준으로 계산하므로 각도를 입력받은 경우 a * pi / 180을 해줘야 함.
void sine() {   
	double a, result;
	printf("각도를 입력하세요(0도~360도): ");
	scanf("%lf", &a);
	result = sin(a * PI / 180.0);  // 수정 사항 - sin()함수는 라디안을 기준으로 계산, 따라서 입력받은 각을 라디안으로 변환해주어야함.
	// adjustment - sin() function calculate base on radian, so we should translate angle to radian
	printf("결과: %lf\n\n", result);
}

void logBase10() {
	double a, result;
	while (1) {
		printf("실수값을 입력하시오: ");   
		scanf("%lf", &a);
		if (a <= 0.0)  // 수정 사항 - log는 진수가 0보다 클 때 정의되므로 0도 입력 오류에 포함됨.
			// adjustment - log funtion's value should be bigger than 0. so 0 for input number should be included in wrong input
			printf("입력 오류\n");  // means wrong input
		else {
			result = log10(a);
			printf("결과 = %lf\n\n", result);
			break;
		}
	}
}

void root() {
	double a, result;
	while (1) {
		printf("실수를 입력하시오: ");
		scanf("%lf", &a);
		if (a < 0.0)  // 수정 사항 - 제곱근은 0보다 크거나 같을 때 정의되므로 0이 입력되어도 오류가 아님.
			// adjustment - square root is defined in 0 and bigger. so 0 for input number is not an wrong input
			printf("제곱근이므로 0이상의 실수를 입력해주세요.\n");
		else {
			result = sqrt(a);
			printf("결과: %lf\n\n", result);
			break;
		}
	}
}

void permutation() {
	int n, r;
	long long result;
	while (1) {
		printf("n과 r을 입력하시오: ");
		scanf("%d %d", &n, &r);
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
	result = calc_fact(n) / calc_fact(n-r);  // 수정 사항 -  동일한 계산을 함수에서 반복하는 것이 아닌 팩토리얼 계산 함수 활용
	// adjustment - not iterate same calculation in function, use factorial function / 중복 제거(DRY: Don't Repeat Yourself)
	printf("결과: %lld\n\n", result);
}

void combination() {
	int n, r;
	long long result;
	while (1) {
		printf("n과 r을 입력하시오: ");
		scanf("%d %d", &n, &r);
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
	result = calc_fact(n) / (calc_fact(r) * calc_fact(n-r));  // 수정 사항 -  동일한 계산을 함수에서 반복하는 것이 아닌 팩토리얼 계산 함수 활용
	// adjustment - not iterate same calculation in function, use factorial function / 중복 제거(DRY: Don't Repeat Yourself)
	printf("결과: %lld\n\n", result);
}

int main() {
	while (1) {
		switch (menu()) {
		case 1:
			factorial();
			break;
		case 2:
			sine();
			break;
		case 3:
			logBase10();
			break;
		case 4:
			root();
			break;
		case 5:
			permutation();
			break;
		case 6:
			combination();
			break;
		case 7:
			printf("프로그램을 종료합니다.\n");
			return 0;
		default:
			printf("잘못된 입력입니다.\n");
			break;
		}
	}
}
