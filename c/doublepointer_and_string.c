#define _CRT_SECURE_NO_WARNINGS   // scanf 보안 오류 방지
#include <stdio.h>   // 표준 입출력 라이브러리(standard input/output)
#include <stdlib.h>  // realloc(재할당)함수와 malloc(동적 할당)함수 활용을 위한 라이브러리(대표적인 다른 활용 방안으로 random함수 활용이 있음)
#include <string.h>  // 문자열 처리 전문 라이브러리

// 이중 포인터의 구조
// **pointer라면 -> *pointer = pointer라는 변수가 가리키는 값(근데 이 값도 주소임) -> *(*pointer) = 아까 (*pointer)가 가리켰던 값(주소)가 가리키는 값


// 1. 히스토리에 새 명령어 추가하는 함수
// (힌트: history가 가리키는 가방의 크기를 realloc으로 늘린 후, 새 명령어 공간을 malloc해서 카피해야 해!)
char** add_command(char** history, int* count, const char* new_cmd) {
    // history: 이중 포인터, count: 포인터 변수(주소값을 받음), new_cmd: 역시 포인터 변수지만 const이므로 읽기 전용
    // 1-1. 현재 개수(*count)보다 1칸 더 큰 주소 가방으로 realloc 하기
    char** temp = (char**)realloc(history, (*count + 1) * sizeof(char*)); // count가 포인터 변수이므로 count의 값에 접근하려면 간접 참조 연산자인 *이 필요함
    if (temp != NULL) {
        history = temp;
    }
    else {
        printf("메모리가 부족합니다.\n");
        exit(1);
    }

    // 1-2. realloc이 성공했다면, 방금 만든 가장 마지막 칸에 새 단어가 들어갈 공간을 malloc 해주기
    history[*count] = (char*)malloc(strlen(new_cmd) + 1);
    // 문자열의 길이 + 1(for \0)만큼의 크기를 history의 가장 마지막 방에 할당

    history[*count] = (char*)malloc(strlen(new_cmd) + 1);
    if (history[*count] == NULL) {
        printf("문자열 메모리 할당 실패!\n");
        exit(1);
    }

    // 1-3. strcpy 함수를 사용해서 new_cmd의 내용을 새로 할당한 공간에 복사하기
    strcpy(history[*count], new_cmd);

    // 1-4. 명령어 개수(*count)를 1 증가시키고 변경된 history 포인터 반환하기
    (*count)++;

    return history;
}

// 2. 저장된 모든 명령어를 출력하는 함수
void print_history(char** history, int count) {
    printf("\n=== 명령어 히스토리 목록 ===\n");
    for (int i = 0; i < count; i++) {
        printf("%s\n", history[i]);
    }
    printf("=============================\n\n");
}

// 3. 프로그램 종료 전 모든 동적 할당을 해제하는 함수
void free_history(char** history, int count) {
    // [미션] 내부 단어들 먼저 free -> 전체 가방 free
    // 여기에 코드 작성!
    for (int i = 0; i < count; i++) {
        free(history[i]);   // 내부 단어들을 먼저 free하고 난 후에 전체 가방을 free해야 안쪽 단어들이 주소를 잃어버려 영영 메모리를 해제할 수 없는 메모리 누수가 발생하지 않음
    }
    free(history); // 내부 단어 free 후에 전체 가방 free

}

int main() {
    char** history = NULL; // 명령어 주소들을 담을 이중 포인터 가방
    int count = 0;         // 현재 저장된 명령어 개수
    char buffer[100];      // 사용자 입력을 임시로 받을 버퍼

    printf("클라우드 터미널 히스토리 시스템을 시작합니다. (종료하려면 'exit' 입력)\n");

    while (1) {
        printf("ubuntu@gachon:~$ ");
        scanf("%s", buffer);

        // 'exit'를 입력하면 루프 탈출
        if (strcmp(buffer, "exit") == 0) {
            break;
        }

        // 입력받은 명령어를 히스토리에 추가
        history = add_command(history, &count, buffer);
    }

    // 저장된 히스토리 출력
    print_history(history, count);

    // 메모리 해제
    free_history(history, count);

    return 0;
}
