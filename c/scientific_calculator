#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#define PI 3.14159265

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

long long calc_fact(int n) {
	long long result = 1;
	for (int i = 1; i <= n; i++)
		result *= i;
	return result;
}

void factorial() {
	int n;
	printf("정수를 입력하세요: ");
	scanf("%d", &n);
	printf("결과: %lld\n\n", calc_fact(n));
}

//sin()함수는 라디안을 기준으로 계산하므로 각도를 입력받은 경우 a * pi / 180을 해줘야 함.
void sine() {
	double a, result;
	printf("각도를 입력하세요(0도~360도): ");
	scanf("%lf", &a);
	result = sin(a * PI / 180.0);
	printf("결과: %lf\n\n", result);
}

void logBase10() {
	double a, result;
	while (1) {
		printf("실수값을 입력하시오: ");
		scanf("%lf", &a);
		if (a <= 0.0)
			printf("입력 오류\n");
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
		if (a < 0.0)
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
		if (n == 0 || r == 0)
			printf("0을 입력하면 안됩니다. 자연수를 입력하세요.\n");
		else if (n < r)
			printf("n이 r보다 작으면 안됩니다.다시 입력하세요.\n");
		else 
			break;
	}
	result = calc_fact(n) / calc_fact(n-r);
	printf("결과: %lld\n\n", result);
}

void combination() {
	int n, r;
	long long result;
	while (1) {
		printf("n과 r을 입력하시오: ");
		scanf("%d %d", &n, &r);
		if (n == 0 || r == 0)
			printf("0을 입력하면 안됩니다. 자연수를 입력하세요.\n");
		else if (n < r)
			printf("n이 r보다 작으면 안됩니다.다시 입력하세요.\n");
		else
			break;
	}
	result = calc_fact(n) / (calc_fact(r) * calc_fact(n-r));
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
