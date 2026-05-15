from tkinter import *    # GUI 활용을 위해 tkinter 모듈 import / import tkinter module for using GUI
import random            # 난수 발생을 위해 random 모듈 import / import random module to create random number

num = random.randint(1, 100)   # 난수 생성(전역 변수) /  create random number(global variable)
count = 0                

def rand_num():
    global num  # 함수 내부에서 변수를 수정하기 위해 global 추가 / add 'global' to change value of variable in function(method) 
    global count
    try:
        input_num = int(e1.get())   # get()함수는 데이터 타입이 문자열이므로 비교를 위해 정수형으로 전환 / change the data type for number comparison(get() data type: string) 
        count += 1
        if input_num > num:   # 숫자 비교 로직 / number comparison logic
            l3.config(text = f'DOWN \n(현재 {count}회 시도 중)')   # .config()는 f-string과 \n 등을 사용할 수 있음(.insert()는 f-string은 가능하지만 \n은 불가)
          # .config() can use f-stirng and \n(.insert() can't use \n)
        elif input_num < num:
            l3.config(text = f'UP \n(현재 {count}회 시도 중)')
        else:
            l3.config(text = f'정답입니다! 시도 횟수: {count}회 \n 다음 게임을 위해 정답을 초기화합니다.')
            num = random.randint(1, 100)
            count = 0   # 정답이 나옸으므로 시도 횟수 초기화 / reset count variable for next game
    except ValueError:   # 입력 오류 방지를 위한 try-except 활용 / use try-except to prevent wrong input
        e2.insert(0, '숫자만 입력해주세요!')
            
window = Tk()
window.title("숫자 맞추기 게임")  / guess number game

# 제목 / title
l1 = Label(window, text = '1부터 100사이의 숫자 맞추기', width = 25)
l1.grid(row = 0, column = 0, columnspan = 2, pady = 10)
 
# 입력창 / input window
l2 = Label(window, text = '정답', width = 5)
l2.grid(row = 1, column = 0, padx = 5, pady = 5)  # padx, pady : x축, y축 기준 여백 형성 / padx, pady : create blank(padx: x-axis,pady: y-axis)
e1 = Entry(window)
e1.grid(row = 1, column = 1)

# 버튼 / button
b1 = Button(window, text = '결과 확인', width = 10, command = rand_num)
b1.grid(row = 2, column = 0, columnspan = 2)

# 출력창 / output window
l3 = Label(window, text = '결과가 여기에 표시됩니다.')
l3.grid(row = 3, column = 0, columnspan = 2, pady = 5)

window.mainloop()
