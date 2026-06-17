#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char str[10];
	int i = 0;

	printf("문자열을 입력하시오: ");
	//scanf("%s", str); scanf함수는 오버플로우(사용자가 문자열의 크기보다 더 큰 입력을 한 경우)가 발생했을 때 대처하기 어려움
  //따라서 오버플로우를 방지해주는 fgets()함수를 활용하는 것을 추천
  // scanf() can not prevent overflow problem. so recommend to use fgets() which can prevent overflow problem.
	fgets(str, sizeof(str), stdin);
	// (변수명, 변수크기, 입력 통로(ex. 키보드, 파일))
	// 키보드로 입력하는 경우 C언어에서 키보드를 뜻하는 정해진 단어인 stdin을 적어주면 됨.
  // ( variable name, size of varialbe, pathway of input)
  // keyboard input -> stdin
  
	int len = 0;
	while (str[len] != 0) {
		len++;
	}
	if (len > 0 && str[len - 1] == '\n') { // 빈 문자열이 아니면서 마지막 문자가 엔터키라면 
    // if str is not empty and last char is \n
		str[len - 1] = 0;// 엔터키를 지워버림  
    // remove the \n
		len--; // 엔터키를 지웠으니 글자수도 -1
    // len -1 (because we remove the \n)
	}
	// 만약 문자열이 변수의 크기보다 큰 경우에는 마지막이 \n이 아니므로 해당 작업을 할 필요가 없음.
  // if input string is bigger than str[10], the last char is not \n. so we don't have to remove \n
	
	printf("순수 글자수: %d\n", len);
	printf("출력 확인: [%s]\n", str);

	return 0;
}
