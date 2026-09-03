// scanf 오류 방지를 위한 라인
// line to prevent 'scanf' error
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
// 표준 입출력 라이브러리
// standard input/output library
#include <string.h>
// 문자열 처리 전용 라이브러리
// string specified library
#define TOTAL_SERVERS 3
// 총 서버 수 기호 상수로 지정 -> 코드의 유연성 향상
// define the number of total server as Symbolic constant -> improve the code's elasticity

// 구조체 정의(문자열, 정수형)
// define the structure(string, integer)
typedef struct {
	char id[20];
	int cpu_usage;
} Instance;
// Instance라는 별명 지정 -> 코드의 간결성 향상
// put the nickname 'Instance' -> enhance the code's simplicity

// 평균 계산 전용 함수 정의 (매개변수: instance(구조체), int(정수형))
// define the function that will calculate the average of CPU usages (parameters: instance(structure), integer)
double get_average_cpu(Instance list[], int count) {
	double total_per = 0;
	double avg = 0;
	for (int i = 0; i < count; i++) {
		total_per += list[i].cpu_usage;
	}
	avg = total_per / count;
	return avg;
  // 평균값 반환
  // return the average value
}

// 과부하 인스턴스 색출 함수 정의
// define the function that will identify the overloaded instance
void check_high_load(Instance list[], int count) {
	printf("\n=== [경고] 과부하 인스턴스 목록 ===\n");
	for (int i = 0; i < count; i++) {
		if (list[i].cpu_usage >= 80.0) {
			printf("%s (%d%%)\n", list[i].id, list[i].cpu_usage);
		}
	}
}

int main() {
  // 'servers'라는 이름의 구조체 배열 선언
  // declare the Struct array named 'servers'
	Instance servers[TOTAL_SERVERS];

	printf("=== AWS EC2 모니터링 시스템 ===\n");

  // ID와 CPU 사용량 입력부
  // input the ID & CPU usages
	for (int i = 0; i < TOTAL_SERVERS; i++) {
		printf("\n[%d번 인스턴스] ID 입력 (예: i-123): ", i + 1);
		scanf("%s", servers[i].id);
		// 문자열은 배열의 일종이므로 변수의 이름 자체가 주소를 의미함
		printf("[%d번 인스턴스] CPU 사용량 입력(%%): ", i + 1);
		scanf("%d", &servers[i].cpu_usage);
		// int는 이름 자체가 배열이 아니므로 &이 필요함
	}
  // get_average_cpu함수의 반환값을 avg라는 실수형 변수에 저장
  // store the get_average_cpu return value in 'avg' which is 'double' type variable
	double avg = get_average_cpu(servers, TOTAL_SERVERS);
	printf("\n------------------------\n");
	printf("전체 서버 평균 CPU 사용량: %.2f%%\n", avg);

  // 과부하 CPU 색출 함수 호출
  // call the check_high_load which will identify the overloaded CPU Instance
	check_high_load(servers, 3);

	return 0;
}
