#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define SIZE 10

int main() {
	int seats[SIZE] = {0};
	char answer;
	int seat_num;
	int total;

	while (1) {
		printf("좌석을 예약하시겠습니까?(y or n): ");
		scanf(" %c", &answer);
		if (answer == 'y') {
			printf("-------------------------\n");
			printf("1 2 3 4 5 6 7 8 9 10\n");
			printf("-------------------------\n");
			for (int i = 0; i < 10; i++)
				printf("%d ", seats[i]);
			printf("\n");
			while (1) {
				printf("몇 번째 좌석을 예약하시겠습니까?: ");
				scanf("%d", &seat_num);

				while (getchar() != '\n');  // 사용자 오입력 시 발생할 수 있는 무한 루프 예방 / prevent the infinite loop when user's input is wrong
        /* ex) 사용자 좌석을 5a로 입력 (문자가 포함됨)
          이 whlie문이 없다면 5를 처리한 다음 루프에서 a를 %d로 처리하지 못해 무한 루프 발생.
          getchar함수는 파이썬에서의 pop함수처럼 해당 문자를 제거하면서 반환하므로 while 루프의 첫 번째 루프 때 a가 제거됨.
          그 이후 \n을 만나므로 while루프가 끝나고 프로그램 정상 작동*/
        
				if (seat_num <= 10 && seat_num >= 1) {
					if (seats[seat_num - 1] == 0) {
						seats[seat_num - 1] = 1;
						printf("예약되었습니다.\n");
						break;
					}
					else {
						printf("해당 좌석은 이미 예약되었습니다. 다른 좌석을 선택해주세요.\n");
					}
				}
				else
					printf("1부터 10까지의 자연수를 입력해주세요.\n");
			}
			total = 0;
			for (int k = 0; k < 10; k++) {
				total += seats[k];
			}
			if (total == 10) {
				printf("모든 좌석이 예약되었습니다. 프로그램을 종료합니다.\n");
				break;
			}
		}
		else if(answer == 'n') {
			printf("no를 선택하셨으므로 프로그램을 종료합니다.\n");
			break;
		}
		else {
			printf("'y'나 'n'중 하나를 입력해주세요.\n");
		}
	}
	return 0;
}
