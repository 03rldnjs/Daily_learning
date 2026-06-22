#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int solution(const char* video_len, const char* pos, const char* op_start, const char* op_end, const char* commands[], size_t commands_len);
// 비디오 총 길이, 현재 위치, 오프닝 시작, 오프닝 끝, 사용자 입력값, 문자열 배열의 길이(크기) 
int conver_to_sec(const char*);


int main() {
	int min, sec;
	int result;
	const char* video_len = "34:33";
	const char* pos = "13:00";
	const char* op_start = "00:55";
	const char* op_end = "02:55";
	const char* commands[] = {"next","prev"}; // 포인터 배열, 일종의 이차원배열인데, 한 요소의 크기를 특정하지 않고 사용할 수 있어서 메모리 효율성이 뛰어남.
	size_t commands_len = 2;
	result = solution(video_len, pos, op_start, op_end, commands, commands_len);
	min = result / 60;
	sec = result % 60;

	printf("%02d:%02d", min, sec);
}

int convert_to_sec(const char* time_str) {
	int min, sec;
	sscanf(time_str, "%d:%d", &min, &sec);   // 문자열 형태를 int형으로 읽어옴
  // scanf string to interger

	return (min * 60) + sec;
}

int solution(const char* video_len, const char* pos, const char* op_start, const char* op_end, const char* commands[], size_t commands_len) {
	int video_sec = convert_to_sec(video_len);
	int pos_sec = convert_to_sec(pos);
	int start_sec = convert_to_sec(op_start);
	int end_sec = convert_to_sec(op_end);

	if (pos_sec <= end_sec && pos_sec >= start_sec) {
		pos_sec = end_sec;
	}

	for (size_t i = 0; i < commands_len; i++) {
		if (strcmp(commands[i], "prev") == 0) { //commands[i]가 문자열, commands라는 배열의 i번째 요소가 prev인지 확인하는 작업
      // commands[] is string, check the element of commands[i]. "prev" or "next" 
			pos_sec -= 10;

			if (pos_sec < 0) {
				pos_sec = 0;
			}
		}
		if (strcmp(commands[i], "next") == 0) {
			pos_sec += 10;
			
			if (pos_sec > video_sec) {
				pos_sec = video_sec;
			}
		}
		if (pos_sec <= end_sec && pos_sec >= start_sec) {  // 시간 이동 작업을 마친 후 pos_sec이 오프닝 구간 내에 있다면 end_sec으로 이동
      // if pos_sec is in the range of opening time after revising, change the value of pos_sec same as end_sec 
			pos_sec = end_sec;
		}
	}

	return pos_sec;
}

