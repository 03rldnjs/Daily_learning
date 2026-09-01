#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
// 표준 입출력 라이브러리
// standard input/output library
#include <stdlib.h>
// malloc과 realloc을 사용하기 위해 추가한 라이브러리
// add stdlib.h to use malloc and realloc 
#include <string.h>
// 문자열을 사용하기 위한 라이브러리
// add library to use string
#define MAX_CAPACITY 5 
// 최대 인스턴스 개수 정의
// define max instance number
#define MIN_CAPACITY 2
// 최소 인스턴스 개수 정의
// define min instance number

// 구조체 정의(문자열, 정수형) -> 구조체는 새로운 자료형을 정의하는 것과 같다
// define the structure(string, int) -> defining struture is same as defining a new variable type
typedef struct {
	char id[20];
	int cpu_usage;
} Instance; // 매번 struct를 적는 것을 방지하기 위한 별명 지정
// give a nickname to prevent write 'struct' everytime

// 평균 계산 함수 정의
// define function which will calculates average
double get_average_cpu(Instance list[], int count) { // 매개 변수 정의(구조체, 정수형 변수) 
  // define parameters(structure, int type)
	double total_per = 0; // 전체 총합을 의미하는 변수 선언
  // define a variable which means sum of cpu usages
	for (int i = 0; i < count; i++) {
		total_per += list[i].cpu_usage; // 총합 계산
	} // calculate the sum of cpu usages
	return total_per / count; // 평균값 반환
  // return the average value
}

int main() {
	int count = 0;

	printf("초기 생성할 EC2 인스턴스 개수 입력: ");
	scanf("%d", &count);

  // 입력한 인스턴스의 개수가 최댓값과 최솟값의 사이에 있도록 while 루프 지정
	while (count < MIN_CAPACITY || count > MAX_CAPACITY) {
		printf("[오류] 인스턴스의 개수는 %d와 %d 사이의 자연수만 입력할 수 있습니다.\n", MIN_CAPACITY, MAX_CAPACITY);
		printf("초기 EC2 인스턴스 개수 재입력: ");
		scanf("%d", &count);
	}
  
  // malloc을 통한 동적 메모리 할당(count의 개수만큼 구조체 공간이 생성됨)
	Instance* servers = (Instance*)malloc(sizeof(Instance) * count);
  // 메모리 할당이 실패할 경우를 대비한 코드(defensive programming)
	if (servers == NULL) {
		printf("초기 메모리 할당 실패!\n");
		return 1;
	}

	for (int i = 0; i < count; i++) {
		printf("\n[%d번 인스턴스] ID 입력: ", i + 1);
		scanf("%19s", servers[i].id);

		printf("[%d번 인스턴스] CPU 사용량 입력: ", i + 1);
		scanf("%d", &servers[i].cpu_usage);
	}

	double avg = get_average_cpu(servers, count);
	printf("\n현재 전체 평균 CPU 사용량: %.2f%%\n", avg);

	while (avg >= 70.0) {
		printf("\n[ALERT] 평균 CPU 사용량 70%% 초과\n");
		if (count >= MAX_CAPACITY) {
			printf("적정 평균 사용량을 초과하였으나, 최대 인스턴스 수에 도달하여 더 확장할 수 없습니다.\n");
			break;
		}
		printf("Auto Scaling(Scale Out)을 진행합니다.\n");

		Instance* temp = (Instance*)realloc(servers, sizeof(Instance) * (count + 1));
		if (temp != NULL) {
			servers = temp;
			count++;
		}
		else { 
			printf("메모리 확장 실패!\n");
			break;
		}
		printf("\n[%d번 인스턴스] ID 입력: ", count);
		scanf("%19s", servers[count - 1].id);
		printf("[%d번 인스턴스] CPU 사용량 입력: ", count);
		scanf("%d", &servers[count - 1].cpu_usage);	
		avg = get_average_cpu(servers, count);
		printf("\n현재 전체 평균 CPU 사용량: %.2f%%\n", avg);
	}
	while (avg <= 30.0) {
		printf("\n[ALERT] 평균 CPU 사용량 30%% 미만\n");
		if (count <= MIN_CAPACITY) {
			printf("적정 평균 사용량 미만이나, 최소 인스턴스 수에 도달하여 더 축소할 수 없습니다.\n");
			break;
		}
		printf("Auto Scaling(Scale IN)을 진행합니다.\n");

		Instance* temp = (Instance*)realloc(servers, sizeof(Instance) * (count - 1));
		if (temp != NULL) {
			servers = temp;
			count--;
		}
		else {
			printf("메모리 축소 실패!\n");
			break;
		}
		avg = get_average_cpu(servers, count);
		printf("\n현재 전체 평균 CPU 사용량: %.2f%%\n", avg);
		printf("현재 인스턴스 개수: %d\n", count);
	}
	printf("\n=== 최종 인스턴스 상태 목록 (총 %d대) ===\n", count);
	for (int i = 0; i < count; i++) {
		printf("- %s : %d%%\n", servers[i].id, servers[i].cpu_usage);
	}
	printf("최종 평균 CPU 사용량: %.2f%%\n", get_average_cpu(servers, count));

	free(servers);

	return 0;
}
