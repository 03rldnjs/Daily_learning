#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 5

int main() {
	int scores[SIZE];

	srand((unsigned)time(NULL));
	for (int i = 0; i < SIZE; i++) {\
    // 중복 숫자 배제 알고리즘
		while (1) {
			int num = rand() % 100 + 1;
			int check = 0;

			for (int k = 0; k < i; k++) {
				if (scores[k] == num) {  // 동일한 숫자가 있다면 check = 1, for루프를 다 돌아도 동일한 숫자가 없다면 여전히 check = 0
					check = 1;
					break;
				}
			}
			if (check == 0) {  // check = 0인 경우(= 동일한 숫자를 찾지 못한 경우)에만 배열에 해당 숫자를 대입함.
				scores[i] = num;
				break;
			}
		}
	}

	for (int j = 0; j < SIZE; j++) {
		printf("scores[%d] = %d\n", j, scores[j]);
	}
	return 0;
}

// 배열을 활용한 랜덤 숫자 중복 가능성 배제 알고리즘
