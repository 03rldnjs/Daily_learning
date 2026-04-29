# 함수 분리 ver. (Modularizing code)
stu_list = []

def grade_search(id_num, source_list):   # 학번을 통해 성적을 찾는 로직을 함수로 분리 (extracted the grade search logic into separate function) 
  found = False  # 변수에 bool형을 저장하여 확인 도구 생성 (storing bool type in 'found' variable to create check tool)
  for student in source_list:   # 파이썬다운 for문 활용 (pyhonic 'for' loop usage)
    if student['id'] == id_num:
      print(f"학번: {student['id']}, 성적: {student['grade']}")
      found = True   # found함수가 True가 되면 더 이상 찾지 않고 for루프를 벗어남 -> 추가적인 반복을 하지 않으므로 효율성 up
      break               # if found = True, it breaks out of the loop -> makes better efficicy because computer doesn't have to do unnecessary iteration

  if not found:  # 입력한 학번이 존재하지 않아 found = False가 계속 유지되었다면 (if the state of found keeps 'False' because the user's id input is not in list)
    print("해당 학번은 존재하지 않습니다.")
    
def sum_avg(stu_grade_list):   # list를 입력받아 점수 합계와 평균, 최고점자를 찾는 로직을 함수로 분리 (extracted the total, avg, topscorer calculating logic into separate function)
  total_grade = sum(s['grade'] for s in stu_grade_list)   # for문 제너레이터 표현식 활용 (for loop generator expression)
  avg_grade = total_grade / len(stu_grade_list)
  top_student = max(stu_grade_list, key=lambda x: x['grade'])

  print(f"총점: {total_grade}")
  print(f"평균: {avg_grade:.2f}")
  print(f"최고득점자: {top_student['name']}({top_student['grade']}점)")

while True:
  try:
    opt_input = int(input("1. 학생추가, 2. 성적조회, 3. 통계보기, 4. 종료: "))
  except ValueError:
    print("잘못된 입력입니다. 다시 입력하세요.")
    continue

  if opt_input == 1:
    while True:
      try:
        stu_in_num = int(input("추가할 학생의 인원 수를 입력하시오: "))
        break
      except ValueError:
        print("잘못된 입력입니다. 자연수를 입력하세요.")
    if stu_in_num > 0:
      for i in range(stu_in_num):
        while True:
          try:
            stu_num = int(input("학번을 입력하시오: "))
            break
          except:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
        stu_name = input("이름을 입력하시오: ")
        stu_grade = int(input("성적을 입력하시오: "))
        stu_dic = {
            'id': stu_num,
            'name': stu_name,
            'grade': stu_grade
        }
        print(stu_dic)
        stu_list.append(stu_dic)
      stu_list.sort(key = lambda x: x['id'])
      print("학번 순 정렬 결과:", stu_list)
    else:
      print("잘못된 입력입니다. 자연수를 입력하세요.")

  elif opt_input == 2:
    try:
      view_num = int(input("성적을 조회할 학생의 학번을 입력하시오(종료하려면 음수 입력): "))
    except ValueError:
      print("잘못된 입력입니다. 다시 입력하세요.")
    if view_num < 0:
      pass
    else:
      grade_search(view_num, stu_list)

  elif opt_input == 3:
    if not stu_list:   # 학생 데이터가 아예 없는 경우 0으로 나눠야하므로 미리 걸러내기 (use 'if' to prevent Zero Division) 
      print("조회할 데이터가 없습니다. 먼저 학생을 추가하세요.")
    else:
      sum_avg(stu_list)

  elif opt_input == 4:
    print("프로그램을 종료합니다.")
    break

  else:
    print("잘못된 입력입니다. 1부터 4까지의 정수를 입력하세요.")
