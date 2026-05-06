#define _CRT_SECURE_NO_WARNINGS    // scanf 오류를 방지하기 위한 문구 (to prevent scanf error in visual studio)
#include <stdio.h>
#include <math.h>                  // 수학 관련 함수를 활용하기 위한 헤더파일 추가 (include math.h to use mathmatical functions

int menu() {   // 팩토리얼, 사인, 상용로그, 제곱근, 순열, 조합을 지원하는 공학용 계산기 (scientific calculator that provide factorial, sin, log(base10), root, permutation and combination
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

void factorial() {  // 팩토리얼 계산을 위한 함수 생성 create function to calculate factorial
	int n;
    long long result = 1;
	printf("정수를 입력하세요: ");
	scanf("%d", &n);
    for (int i = 1; i <= n; i++)   // factorial calculate Algorithm
		result *= i;
	printf("결과: %lld\n\n", result);
}

void sine() {  // sin계산을 위한 함수 생성 create function to calculate sin
	double a, result;
	printf("각도를 입력하세요(0도~360도): ");
	scanf("%lf", &a);
	result = sin(a);   // math.h에 포함된 sin()함수 사용 use sin() function which is included in math.h
	printf("결과: %lf\n\n", result);
}

void logBase10() {  // 상용로그 계산을 위한 함수 생성 create function to calculate log(base10)
	double a, result;
	while (1) {  // 입력 오류에 의한 프로그램 종료를 방지하기 위한 무한 루프 생성 create infinite loop to avoid program exit because of wrong input  
		printf("실수값을 입력하시오: ");
		scanf("%lf", &a);
		if (a < 0.0)
			printf("입력 오류\n");  // 입력 오류일 경우 정상적인 입력이 들어올 때까지 무한 반복 iterate infinitly until user's proper input
		else {
			result = log10(a);
			printf("결과 = %lf\n\n", result);
			break;   // 정상적인 입력이 들어오면 바로 무한 루프를 빠져나옴 escape infinite loop if user's input is fit to input condition
		}
	}
}

void root() {  // 제곱근 계산을 위한 함수 생성 create funtion to calculate root 
	double a, result;
	while (1) {   // 이전과 동일한 입력오류로 인한 프로그램 종료 방지 무한 루프 infinite loop to avoid program exit (same as log function while loop) 
		printf("실수를 입력하시오: ");
		scanf("%lf", &a);
		if (a <= 0.0) 
			printf("제곱근이므로 0이상의 실수를 입력해주세요.\n");
		else {
			result = sqrt(a);  // sqrt = square root math.h에 포함되어있는 함수. included in math.h
			printf("결과: %lf\n\n", result);
			break;
		}
	}
}

void permutation() {  // 조합 계산을 위한 함수 생성 create funtion to calculate permutation
	int n, r;  // 입력값은 크지 않으므로 int형으로 충분 int(4byte) is enough for input value
	long long result;  // 팩토리얼을 하므로 값이 매우 커질 수 있음. 따라서 long long으로 선언하는 것이 안전함 
					   // result should be declared by long long(8byte) because permutation include factorial calculation
    long long denomin = 1; // result와 같은 이유로 long long형으로 선언 
    long long numer = 1;  // declare result for long long type just a same reason with result declaration
	while (1) {   // 이전과 동일한 입력오류로 인한 프로그램 종료 방지 무한 루프 infinite loop to avoid program exit (same as log function while loop)
		printf("n과 r을 입력하시오: ");
		scanf("%d %d", &n, &r);
		if (n == 0 || r == 0)   // 순열에서 0이 포함되면 안되므로 0 입력 방지 include no 0 condition because permutaion should not include 0 in elements(n, r)
			printf("0을 입력하면 안됩니다. 자연수를 입력하세요.\n");
		else 
			break;
	}
	for (int i = 1; i <= n; i++)  // factorial calculation Algorithm
    	numer *= i;
    for (int j = 1; j <= (n - r); j++)  
    	denomin *= j;
    result = numer / denomin;
	printf("결과: %lld\n\n", result);
}

void combination() {
	int n, r;
    long long numer = 1;
    long long denomin1 = 1;
    long long denomin2 = 1;
	long long result;
	while (1) {
		printf("n과 r을 입력하시오: ");
		scanf("%d %d", &n, &r);
		if (n == 0 || r == 0)  // 순열과 마찬가지로 조합에서도 0이 포함되면 안되므로 0 입력 방지 include no 0 condition because combination should not include 0 in elements(n, r) same as permutation
			printf("0을 입력하면 안됩니다. 자연수를 입력하세요.\n");
		else if (n < r)  // 조합 공식은 (n-r)을 포함하므로 n이 반드시 r보다 커야 함 combination formular includes (n - r), so n should be bigger than n
			printf("n이 r보다 작으면 안됩니다.다시 입력하세요.\n");
		else
			break;
	}
    for (int i = 1; i <= n; i++)  // factorlal calcuation Algorithm
    	numer *= i;
    for (int j = 1; j <= r; j++)
    	denomin1 *= j;
    for (int k = 1; k <= (n-r); k++)
    	denomin2 *= k;
	result = numer / (denomin1 * denomin2);
	printf("결과: %lld\n\n", result);
}

int main() {
	while (1) {
		switch (menu()) {  // 효율적인 알고리즘을 위한 switch함수 활용 use switch function for efficient Algorithm
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
			return 0;  // 7을 입력한 경우 프로그램을 종료하므로 return 0 입력 put return 0 because 7 for input means program exit
		default:
			printf("잘못된 입력입니다.\n");
			break;
		}
	}
}
