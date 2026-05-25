#include <stdio.h>
     
int main(void) {
    // unsigned형으로 포인터 변수를 선언하는 이유는 부호비트를 고려하지 않기 위함 /  declare pointer variables for unsigned type because of distraction of sign bit
    unsigned int* i; // unsigned int형 포인터 변수 선언 / declare pointer variables for unsigned int type
    unsigned short* s;  // unsigned short형 포인터 변수 선언 / declare pointer variables for unsigned short type
    unsigned char* c;  // unsigned char형 포인터 변수 선언 / declare pointer variables for unsigned char type
    unsigned int num = 0xFFFFFFFF;  // num이라는 일반 변수에 0xFFFFFFFF 저장 / put 0xFFFFFFFF in num
     
    i = &num;  // i에 num의 주소 저장 / put the address of num in i
    s = (unsigned short*)&num;  // s에 num의 시작 주소를 unsigned short*의 형태로 형변환하여 저장(2byte) / put the address of num which is transformed in unsigned short* type
    c = (unsigned char*)&num;  // c에 num의 시작 주소를 unsigned char*의 형태로 형변환하여 저장(1byte) / put the address of num which is transformed in unsigned char* type
     
    *i = 0xCC; // 포인터 변수 i의 값을 0xCC로 수정(*을 통해 i에 들어있는 주소(&num)의 값을 수정)  / revise the value of i to '0xCC'
    printf("first: %08x\n", num);  // i는 4바이트 포인터이므로 시작 주소부터 4바이트 전체를 0x000000CC로 덮어씀 -> 따라서 출력값 = 000000cc
    // i is 4byte pointer so overwrite all of num's value
  
    num = 0xFFFFFFFF;  // num의 값을 다시 0xFFFFFFFF로 리셋 / reset the value of num to 0xFFFFFFFF
    *s = 0xCC; // s는 2바이트 포인터이므로 시작주소부터 하위(리틀 엔디안) 2바이트만 0x00CC로 덮어씀. / s is 2 byte pointer so overwrite only 2 byte of value of num
    printf("second: %08x\n", num); // 하위 2바이트(16진수 기준 4칸)만 수정된 ffff00cc 출력 / print ffff00cc
     
    num = 0xFFFFFFFF; // num의 값을 다시 0xFFFFFFFF로 리셋 / reset the value of num to 0xFFFFFFFF
    *c = 0xCC;  // c는 1바이트 포인터이므로 시작주소부터 1바이트만 0xCC로 덮어씀 / c is 1 byte pointer so overwrite only 1 byte of value of num
    printf("third: %08x\n", num); // 하위 1바이트(16진수 기준 2칸)만 수정된 ffffffcc 출력 / print ffffffcc
     
    return 0;
}
