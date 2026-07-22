#define _CRT_SECURE_NO_WARNINGS  // scanf 보안 오류 방지
#include <stdio.h>  // 표준입출력 라이브러리(standard input/output)
#include <stdlib.h>  // 동적 할당 함수(malloc) 및 재할당함수(realloc)활용을 위한 라이브러리(랜덤함수 사용시에도 필요)
#include <string.h>  // 문자열 처리 전문 라이브러리

// 차량 정보를 담을 구조체
typedef struct {
    char plate[20];   // 차량 번호 (예: "123가4567")
    int entry_time;   // 입차 시간 (HHMM 포맷, 예: 1420)
} Car;  // 해당 구조체를 선언할 때 Car로 대체
// 구조체는 기존의 자료형들을 활용/조합하여 새로운 자료형을 만드는 것과 같다. -> 그러므로 함수의 반환형으로도 사용할 수 있음

// [도움 함수] HHMM 포맷의 정수를 "총 분(minutes)"으로 변환해주는 함수
// ex. 1420 -> 14시 20분 -> 14 * 60 + 20 반환
int to_minutes(int hhmm) {
    int hh = hhmm / 100;
    int mm = hhmm % 100;
    return (hh * 60) + mm;
}

// 1. 입차 함수: 주차장에 차가 들어오면 가방을 늘리고 차량 정보를 저장
// 해당 함수의 반환형은 Car**형
Car** car_in(Car** lot, int* count, const char* plate, int entry_time) {
    // [미션]
    // 1-1. (*count + 1) * sizeof(Car*) 크기만큼 lot을 realloc 하기 (안전 패턴 적용!)
    Car** temp = (Car**)realloc(lot, (*count + 1) * sizeof(Car*));  // try1에서의 타입 불일치 문제 해소

    if (temp != NULL) {
         lot = temp;
    }
    else {
        printf("메모리가 부족합니다.\n");
        exit(1);
    }
    // 1-2. 새 방 lot[*count]에 sizeof(Car)만큼 malloc으로 구조체 공간 파기
    lot[*count] = (Car*)malloc(sizeof(Car));  // try1에서의 타입 불일치 문제 해소
    // 1-3. strcpy로 차량번호 복사하고, 입차시간 저장하기
    strcpy(lot[*count]->plate, plate);  // ->를 활용하여 구조체 내의 대상을 정확하게 지정하여 복사
    lot[*count]->entry_time = entry_time;
    // 1-4. (*count)++ 해주고 새 lot 반환하기
    (*count)++;

    return lot; // 임시 반환
}

// 2. 출차 및 정산 함수: 차가 나가면 요금을 계산하고 주차장에서 제거
Car** car_out(Car** lot, int* count, const char* plate, int exit_time) {
    int target_index = -1;
    int total_time;
    int parking_fee;

    // [미션] 
    // 2-1. 반복문을 돌며 lot[i]->plate와 plate가 일치하는 차량 검색 (strcmp 사용!)
    for (int i = 0; i < *count; i++) {
        if (strcmp(lot[i]->plate, plate) == 0) {
            target_index = i;
        }
    }
    // 2-2. 차량을 못 찾았다면 "주차된 차량이 아닙니다." 출력 후 lot 반환
    if (target_index == -1) {
        printf("주차된 차량이 아닙니다.\n");
        return lot;
    }
    // 2-3. 차량을 찾았다면 요금 계산 로직 수행
    //      - to_minutes 함수를 써서 (출차시간 - 입차시간)으로 총 주차 시간 구하기
    //      - 15분 이하인지 초과인지에 따라 요금 계산 후 금액 출력하기
    else {
        total_time = (to_minutes(exit_time) - to_minutes(lot[target_index]->entry_time));
        if (total_time <= 15) {
            parking_fee = 0;
            printf("회차입니다.\n");
        }
        else {
            parking_fee = 1000 + ((total_time - 15)) * 100;
            if(parking_fee >= 50000){
                parking_fee = 50000; // 일일 최대금액 조건 추가
                printf("주차 요금이 일일최대금액 이상입니다.\n");
            }
        }
        printf("주차요금은 %d원 입니다.\n", parking_fee);
    }


    // 2-4. 주차장에서 해당 차량 삭제 처리하기
    //      - 찾은 차량의 메모리 free(lot[target_index]) 수행
    //      - 뒤에 있는 차량 포인터들을 한 칸씩 앞으로 당기기 (lot[j] = lot[j+1])
    //      - (*count)-- 수행 후 lot 반환 (realloc으로 가방 크기를 줄여줘도 좋음!)
    free(lot[target_index]); // 나간 차 메모리 해제

    // 나간 위치(target_index)부터 마지막 한 칸 전까지만 돌면서 당기기
    for (int j = target_index; j < *count - 1; j++) {  // try1에 존재했던 for루프 범위 문제 해결
        lot[j] = lot[j + 1];
    }
    (*count)--; // 차 개수 줄이기

    return lot; // 임시 반환
}

int main() {
    Car** parking_lot = NULL;
    int car_count = 0;
    int choice;
    char plate[20];
    int time;

    while (1) {
        printf("\n--- 가천 주차장 차단기 시스템 ---\n");
        printf("1. 입차 | 2. 출차 | 3. 종료\n");
        printf("선택: ");
        scanf("%d", &choice);

        if (choice == 3) break;

        printf("차량 번호 입력: ");
        scanf("%s", plate);

        if (choice == 1) {
            printf("입차 시간 입력(HHMM): ");
            scanf("%d", &time);
            parking_lot = car_in(parking_lot, &car_count, plate, time);
            printf("[%s] 차량이 입차되었습니다. (현재 주차: %d대)\n", plate, car_count);
        }
        else if (choice == 2) {
            printf("출차 시간 입력(HHMM): ");
            scanf("%d", &time);
            parking_lot = car_out(parking_lot, &car_count, plate, time);
        }
    }

    // 프로그램 종료 전 남아있는 모든 차량 메모리 해제
    for (int i = 0; i < car_count; i++) {
        free(parking_lot[i]);
    }
    free(parking_lot);

    printf("시스템을 종료합니다.\n");
    return 0;
}
