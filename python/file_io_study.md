📂 Python 파일 입출력 완벽 가이드
1. 파일 입출력의 기본 흐름
파이썬에서 파일을 다룰 때는 반드시 [파일 열기 -> 작업(읽기/쓰기) -> 파일 닫기]의 과정을 거칩니다.

1) 파일 열기: open()
Python
f = open("파일명.txt", "모드", encoding="utf-8")
파일명: 경로를 포함한 파일의 이름

모드:

'w': 쓰기 모드 (새로 만들기, 기존 내용 삭제)

'a': 추가 모드 (기존 내용 뒤에 이어 쓰기)

'r': 읽기 모드 (파일 내용 읽기)

encoding: 한글 깨짐 방지를 위해 보통 "utf-8"을 사용합니다.

2) 파일 닫기: close()
파일을 열었으면 반드시 닫아야 합니다. 닫지 않으면 메모리 낭비가 발생하거나 파일이 손상될 수 있습니다.

2. 안전한 파일 입출력: with 문
매번 close()를 쓰는 것은 번거롭고 실수하기 쉽습니다. 파이썬의 with 문을 사용하면 블록이 끝날 때 자동으로 파일을 닫아줍니다. (권장 방식)

Python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요, 기원입니다.")
# 블록을 나가면 자동으로 f.close()가 호출됨
3. 텍스트 파일 읽기 및 쓰기
1) 쓰기 (write)
Python
lines = ["첫 번째 줄\n", "두 번째 줄\n"]
with open("test.txt", "w", encoding="utf-8") as f:
    f.writelines(lines) # 리스트의 내용을 한꺼번에 기록
2) 읽기 (read, readline, readlines)
read(): 파일 전체 내용을 하나의 문자열로 읽음

readline(): 한 줄만 읽음

readlines(): 파일의 모든 줄을 읽어 각각 리스트의 요소로 반환

4. 실전: CSV 파일 다루기
가계부와 같이 표 형태의 데이터를 저장할 때는 CSV(Comma-Separated Values) 형식이 가장 많이 쓰입니다. 파이썬 내장 csv 모듈을 사용하면 편리합니다.

1) CSV 저장하기 (가계부 예시)
Python
import csv

# history 리스트에 Transaction 객체들이 담겨 있다고 가정
def save_to_csv(history):
    with open('assets.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['날짜', '항목', '금액', '구분']) # 헤더
        for record in history:
            writer.writerow([record.date, record.item, record.amount, record.category])
Tip: utf-8-sig 인코딩을 사용하면 엑셀(Excel)에서 CSV를 열었을 때 한글이 깨지지 않습니다.

2) CSV 불러오기
Python
def load_from_csv():
    with open('assets.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        next(reader) # 헤더(첫 줄) 건너뛰기
        for line in reader:
            print(f"날짜: {line[0]}, 금액: {line[2]}")
💡 요약 및 주의사항
상태 관리: 'w' 모드는 기존 내용을 다 지우고 새로 쓰므로 주의해야 합니다.

경로 문제: 파일이 실행 파일과 같은 폴더에 있는지 확인하세요.

자원 해제: with 문을 사용하여 안정성을 확보하세요.
