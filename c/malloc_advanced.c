#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* s) {
    int count = 0;
    while (s[count] != 0) {
        count++;
    }
    char* answer;
    if (count % 2 == 1) {
        answer = (char*)malloc(2); // if문 안에서 동적 할당할 수 있다. can you memory allocation function in if{}
        answer[0] = s[count / 2];  // 인덱싱할 때에는 항상 인덱스가 0부터 시작한다는 점을 주의해야한다.
        // should always think about the start of index is 0
        answer[1] = 0;  // 문자열의 끝은 반드시 \0이어야하므로 마지막 인덱스에 0을 대입해주어야한다.
        // the last value of string should always be \0
    }
    else {
        answer = (char*)malloc(3);  // 마찬가지로 if문 안에서 동적 할당할 수 있다.
        answer[0] = s[count / 2 - 1];
        answer[1] = s[count / 2];
        answer[2] = 0;  
    }

    return answer;
}

int main() {
    char str[100];
    scanf("%s", str);

    char* result = solution(str);

    printf("%s\n", result);

    free(result);
    
    return 0;
}
