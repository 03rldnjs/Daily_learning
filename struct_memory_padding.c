// 구조체 메모리 패딩 알고리즘
// structure memeory padding Algorithm

#include <stdio.h>

struct TypeA {
	char a;  // 1byte
	int b;   // 4byte -> 가장 큰 바이트수 -> 총 바이트수가 4의 배수여야 함.
  // the biggest byte in structure -> total byte should be the multiple of 4
	char c;  // 1byte
}; // int b의 시작 주소가 4의 배수여야하므로 char a가 1byte가 아닌 4byte로 수정
// the starts address should be the multiple of 4 -> 3byte padding 
// 구조체 총 바이트 수가 4의 배수여야하므로 char c가 1byte가 아닌 4byte로 수정(메모리 정렬)
// total byte should be the multiple of 4 so char c -> 3 byte padding
// 그러므로 4+4+4 = 12가 출력됨
// so print would be 12

struct TypeB {
	int b;  // 4byte -> 가장 큰 바이트수 -> 총 바이트수가 4의 배수여야 함.
  // the biggest byte in structure -> total byte should be the multiple of 4
	char a; // 1byte
	char c; // 1byte
}; // int b가 맨 앞에 있으므로 시작주소가 4의 배수일 필요 없음, 따라서 총 바이트수만 4의 배수면 ok
// int b is in the first place so only total byte should be the multiple of 4
// 따라서 총 8바이트로 수정됨. 
// total byte = 8 byte
// a와 c에 그냥 각각 1바이트가 할당됨. 
// 그냥 구조체의 총 크기가 4의 배수여야하므로 8바이트인 것.
// 나머지 2바이트는 컴퓨터가 채워 넣은 빈칸 구역(걍 빈 방임)
// 1 byte is allocated for a and c
// rest 2 byte is just padding for total byte rule

int main() {
	printf("%d ", sizeof(struct TypeA));
	printf("%d ", sizeof(struct TypeB));

	return 0;
}
