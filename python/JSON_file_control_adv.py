import json

try:
    with open("students_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

except (FileNotFoundError, json.JSONDecodeError):
    print("기존 파일이 없거나 내용이 비어있어 새 데이터 목록을 생성합니다.\n")
    data = []

while True:
    try:
        count = int(input("추가할 학생의 수를 입력하시오: "))
        if count > 0:
            break
        else:
            print("잘못된 입력입니다. 자연수를 입력하세요.")
    except ValueError:
        print("잘못된 입력입니다. 자연수를 입력하세요.")
print()

for n in range(count):
    print(f"{n+1}/{count}번째 학생 정보 입력") 
    stu_name = input("이름 입력: ")
    while True: 
        try:
            stu_age = int(input("나이 입력: "))
            if stu_age > 0:
                break
            else:
                print("잘못된 입력입니다. 자연수를 입력하세요.")    
        except:
            print("잘못된 입력입니다. 자연수를 입력하세요.")
        
    stu_major = input("전공 입력: ")
    while True:
        try:
            stu_grade = int(input("학년 입력: "))
            if 1 <= stu_grade <= 4: 
                break
            else:
                print("잘못된 입력입니다. 1,2,3,4 중 하나를 입력하세요.")
        except:
            print("잘못된 입력입니다. 1,2,3,4 중 하나를 입력하세요.")
    print()
    stu_dic = {
        'name': stu_name,
        'age': stu_age,
        'major': stu_major,
        'grade': stu_grade
    }
    data.append(stu_dic)


with open("students_data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("students_data.json 파일에 저장 완료\n")

for student in data:
    print(f"이름: {student['name']}")
    print(f"나이: {student['age']}")
    print(f"전공: {student['major']}")
    print(f"학년: {student['grade']}\n")
