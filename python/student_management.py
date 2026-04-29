stu_list = []  #학생들의 정보가 담긴 여러 딕셔너리들을 저장할 리스트 선언(make a list that can save dictionarys about student's information) 

while True: # 4. 종료를 입력할 때까지 무한 루프 (use infinite loop that will run infinitly until user's input is 4(= exit))
  try:
    opt_input = int(input("1. 학생추가, 2. 성적조회, 3. 통계보기, 4. 종료: "))
  except:
    print("잘못된 입력입니다. 다시 입력하세요.")
# 사용자의 입력이 정수가 아닌 경우를 대비하여 try-except구조 사용(use try-except structure for user's wrong input(ex: string, character etc.)
  if opt_input == 1: 
    while True:
      try:
        stu_in_num = int(input("추가할 학생의 인원 수를 입력하시오: "))
        break
      except:
        print("잘못된 입력입니다. 자연수를 입력하세요.")
    # 역시 사용자의 입력이 자연수가 아닌 경우를 대비하여 try-except구조 사용(use try-except structure for user's wrong input(input type is not integer))
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
        }  # 사용자가 입력한 학생의 정보를 딕셔너리에 저장 (write student's informations in dictionary)
           # 딕셔너리를 선택한 이유는 key:value구조를 활용할 수 있기 때문 (the reason why I choose dictionary is I can use dictionary's key:item structure)
        print(stu_dic)
        stu_list.append(stu_dic)
      sorted_list = sorted(stu_list, key=lambda x: x['id'])  # 성적이 높은 순으로 정렬한 리스트 (sort the list, high scorer will be at front)
      print(sorted_list.sort()) 
    else:
      print("잘못된 입력입니다. 자연수를 입력하세요.")

  elif opt_input == 2:
    try:
      view_num = int(input("조회할 학생의 학번을 입력하시오(종료하려면 음수 입력): "))
    except:
      print("잘못된 입력입니다. 다시 입력하세요.")
    if view_num < 0:
      pass
    else:
      for i in range(len(stu_list)):  # for문을 활용하여 stu_list에 있는 모든 요소들 확인(조회), 입력받은 학번과 같은 요소가 있다면
        # this for loop is C language style. maybe annotation under print funtion would be better chioce because it is using python's strength very well
        if stu_list[i]['id'] == view_num:
          print(f"학번: {stu_list[i]['id']}, 성적: {stu_list[i]['grade']}")
      # for student in stu_list:   # python can unpack list's items very well. you don't have to use len() function when you use for loop
          #if student['id'] == view_num:
            #print("....
  
  elif opt_input == 3:
    total_grade = 0
    avg_grade = 0
    for i in range(len(stu_list)):
      total_grade += stu_list[i]['grade']
    if len(stu_list) > 0:
      top_student = max(stu_list, key=lambda x: x['grade'])
      avg_grade = total_grade / len(stu_list)
      print("총점: ", total_grade)
      print("평균: ", avg_grade)
      print(f"최고득점자: {top_student['name']}({top_student['grade']}점)")
    else:
      print("학생이 없습니다.")
  elif opt_input == 4:
    print("프로그램을 종료합니다.")
    break
  else:
    print("잘못된 입력입니다. 다시 입력하세요.")



