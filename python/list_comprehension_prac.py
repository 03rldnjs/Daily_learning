### list comprehension 문법
# 1. [표현식 for 항목 in 반복가능객체]
#squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# 2. [표현식 for 항목 in 반복가능객체 if 조건]
#evens = [x for x in range(1, 11) if x % 2 == 0]  # [2, 4, 6, 8, 10]

# 3. [참일때값 if 조건 else 거짓일때값 for 항목 in 반복가능객체]
#result = ["Pass" if score >= 60 else "Fail" for score in [50, 75, 90]]

# 프로그램 활용 예시
goals = [2, 0, 1, 4, 0, 3, 0, 1]
names = ["kim", "lee", "son", "hwang", "cho"]

# function 1: 무득점 경기 제외하기 / exclude non-scored game elements in list 'goal'
def ban_noscore(goals):
    scored_list = [x for x in goals if x > 0]
    return scored_list

# function 2: 경기 결과 요약 표기 / translate 0 into 'non-scored' , 1 into 'scored'
def analyize_game(goals):
    analy_list = ["득점" if score >= 1 else "무득점" for score in goals]
    return analy_list

# function 3: 부원 이름 일괄 변경하기 / capitalize the first word of the elements in list 'names'
def cap_names(names):
    cap_list = [x.capitalize() for x in names]
    return cap_list

def veiw_menu():
    print("1. 무득점 제외")
    print("2. 경기 요약")
    print("3. 이름 정정")
    print("4. 종료")

# 가독성 향상과 모듈화를 위해 함수 분리 / define functions respectly to enhance the readability and modulize the program  
while True: # 사용자가 종료를 원할 때까지 무한 반복
    veiw_menu() 
    try:  # try-except를 활용한 예외 처리
        answer = int(input("메뉴를 선택하세요: "))
        if answer == 1:
            result_1 = ban_noscore(goals)
            print(f"무득점 경기를 제외한 리스트: {result_1}")
        elif answer == 2:
            result_2 = analyize_game(goals)
            print(f"경기 득점 여부 요약: {result_2}")
        elif answer == 3:
            result_3 = cap_names(names)
            print(f"선수 명단 정정: {result_3}")
        elif answer == 4:
            print("프로그램을 종료합니다.")
            break
        else:
            print("1부터 4까지의 정수를 입력해야합니다.")
    except:  # except만 사용할 경우 모든 입력 오류를 예외처리할 수 있음(그러나 오류의 유형을 특정하지는 못함) / except can handle all kind of errors and exceptions(but can't specify the error type)
        print("1부터 4까지의 정수를 입력해야합니다.")

### .capitalize()의 작동 규칙 3가지
      
# 1. 첫 글자가 소문자면: 대문자로 바꿈 ("kim" ➡️ "Kim")
# 2. 첫 글자가 이미 대문자면: 그대로 둠 ("Kim" ➡️ "Kim")
# 3. 가장 중요한 특징 (나머지는 소문자로): 첫 글자를 제외한 중간에 대문자가 섞여 있으면, 그 대문자들을 강제로 소문자로 강등시킴.
      
# 예시
#name = "mCdonald"
#print(name.capitalize()) 
# 결과: "Mcdonald" (맨 앞 M은 대문자가 되고, 중간의 C는 소문자로 바뀜)
