#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>  // 동적 메모리 할당을 위해 필요한 라이브러리 추가
// include stdlib.h for malloc function

int main() {
	int n;
	int sum = 0;
	printf("몇 명의 학생 점수를 입력할 건가요: ");
	scanf("%d", &n);

	int* studs = (int*)malloc(sizeof(int) * n);
	//heap영역에 int(4byte)만큼의 크기를 n개 할당받음
  //allocate n * (4byte) in heap area

	for (int i = 0; i < n; i++) {
		printf("%d번 째 학생의 점수를 입력하세요: ", i + 1);
		scanf("%d", &studs[i]); // scanf("%d", studs + i)도 정확히 똑같이 작동한다.
		// studs는 포인터 변수인데 &를 붙이는 이유는 []가 붙는 순간 값을 불러오라는 의미가 되어 주소의 의미가 사라짐
		// 따라서 변수의 주소를 요구하는 scanf를 위해 주소연산자인 &를 반드시 붙여줘야 한다.
    // studs is pointer variable but [] means the value of varible so should put & in front of studs[]
    // scanf always require address of variable, not value
    
		sum += studs[i];
	}
	printf("총점: %d", sum);

	free(studs);
	// free를 적지 않으면 프로그램이 종료될 때까 그 메모리가 계속 RAM에 남아있게 됨.
	// 이 메모리 누수가 누적되면 컴퓨터 메모리가 꽉 차서 시스템에 큰 무리가 됨.
  // if you didn't free the memory, it will stay in RAM until the program end
  // this memory leakage will be a huge burden for computer system
  
	return 0;
}
