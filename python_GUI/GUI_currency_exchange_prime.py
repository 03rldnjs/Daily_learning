import tkinter as tk    # tkinter를 import하고 이 코드 내에서 tk라는 별명으로 부름 / import tkinter and call tkinter as tk
from tkinter import messagebox  # tkinter내에 있는 messagebox를 import함 / import messagebox in tkinter
# from tkinter import *이 아닌 import tkinter as tk로 작성하였으므로 tkinter에 들어있는 함수를 사용하려면 앞에 tk.을 붙여주어야 함.
# should add tk. because i use 'import tkinter as tk' instead of 'from tkinter import *'

EXCHANGE_RATE = 1514.9  # 환율의 변동성을 고려하여 기호 상수로 선언 / declare symbolic constant to reflect the volatility of the exchange rate

window = tk.Tk()  # Tk() 클래스를 이 코드 내에서 window라는 객체로 생성 / create 'window' instance of Tk() class(which is included in tkinter library)
window.title(" 환율 계산기 ")
window.geometry("500x400") 

convert_type = tk.StringVar()   # convert_type의 값을 실시간으로 동기화하기 위해 StringVar()함수 활용 / use StringVar() function for real-time synchronization of value of convert_type
convert_type.set("to_usd")      # 기본값을 "to_usd"로 설정 / set default value : "to_usd"

# 환전 버튼의 command 함수 / function for exchange button is pressed  
def exchange(): 
    try:
        if len(e1.get()) == 0:   # 아무것도 입력되지 않은 경우(len() == 0 활용) / case that nothing is entered (use len() == 0)
            messagebox.showerror("금액 오류", "금액이 입력되지 않았습니다.")
            return
        
        money = float(e1.get())  
        if money < 0:   # 음수가 입력된 경우 / case that a negative quantity is entered
            messagebox.showerror("금액 오류", "금액을 음수로 입력하면 안됩니다.")
            return 
    
        current_choice = convert_type.get()  
        if current_choice == "to_usd": 
            # 환율의 변동성을 고려하여 기호 상수 활용 / use symbolic constant to reflect the volatility of the exchange rate well
            exed_money = money / EXCHANGE_RATE  
            l2.config(text = f'결과: ${exed_money:,.2f}, 입력하신 금액: {money:,} (환율: {EXCHANGE_RATE}원/$)')

        elif current_choice == "to_krw":
            # 환율의 변동성을 고려하여 기호 상수 활용 / use symbolic constant to reflect the volatility of the exchange rate well
            exed_money = money * EXCHANGE_RATE
            l2.config(text = f'결과: {exed_money:,.2f}원, 입력하신 금액: {money:,} (환율: {EXCHANGE_RATE}원/$)')
        # DRY 원칙을 위해 if문과 elif문에 넣지 않고 모든 과정이 끝난 후 알림과 칸 비우기 실행
        # operate message and delete function after every process is done for DRY principle
        messagebox.showinfo("환전 완료", "성공적으로 환전되었습니다.")
        e1.delete(0, tk.END)
    
    except ValueError:
        messagebox.showerror("입력 오류", "금액은 숫자만 입력할 수 있습니다!")
        
# 레이아웃 조정부

# frame 1
moninput_frame = tk.LabelFrame(window, text=" 금액 입력 ", padx=10, pady=10)
moninput_frame.pack(fill="x", padx=15, pady=10)

l1 = tk.Label(moninput_frame, text = '금액: ')
l1.grid(row = 0, column = 0, padx = 5)

e1 = tk.Entry(moninput_frame, width = 25)
e1.grid(row = 0, column = 1, padx = 5)

# frame 2
change_frame = tk.LabelFrame(window, text = '변환 방향 선택', padx = 10, pady = 10)
change_frame.pack(fill = "x", padx = 15, pady = 5)

rb1 = tk.Radiobutton(change_frame, text = "원화 -> 달러", variable=convert_type, value = "to_usd")
rb1.pack()

rb2 = tk.Radiobutton(change_frame, text = "달러 -> 원화", variable = convert_type, value = "to_krw")
rb2.pack()

b1 = tk.Button(window, text = " 환전하기 ", width = 30, command = exchange)
b1.pack()

# frame 3
result_frame = tk.LabelFrame(window, text = "변환 결과", padx = 10, pady = 10)
result_frame.pack(fill = "x", padx = 15, pady = 5)

l2 = tk.Label(result_frame, text = "결과 출력창")
l2.pack(anchor = "w")

window.mainloop()

# from tkinter import *보다 import tkinter as tk가 더 나은 점 
# 1. import *는 tkinter 안에 있는 수백 개의 변수, 함수, 클래스를 이름표 없이 네 코드 방(전역 공간)에 통째로 쏟아붓는 행동
#    만약 코드를 짜다가 Tkinter 안에도 내장되어 있는 이름으로 함수나 변수를 만들면, 기존에 있던 요소가 네가 만든 코드로 덮어씌워지면서 원인 모를 버그가 터짐
# 2. 어떤 위젯이 어디서 왔는지 알 수가 없음
#    tkinter뿐만 아니라 time, csv 등 여러 라이브러리를 섞어서 쓰기 시작하면, 코드 중간에 뜬금없이 나타난 함수나 클래스가 tkinter 출신인지, 다른 데서 온 건지 한눈에 파악하기가 어려워짐

# 따라서 지금같은 미니 프로젝트를 하는 경우에는 import * 을 사용해도 무방하지만, 협업을 하거나 여러 라이브러리를 활용하는 경우에는 import * 방식이 아니라 nickname을 붙여 활용하는 것이 권장됨.

# which point does 'import tkinter as tk' is better than 'from tkinter import *'?
# 1. import* is the action of pouring hundreds of variables, functions, and classes in tkinter into your code rooms (global space) without a name tag
#    if you create a function or variables that has same name with the function of variables included in Tkinter library, the existing element will be overwritten and the unknown error or bug will occur
# 2. Can not know which widget came from where
#    When you start mixing multiple libraries such as time and csv, as well as tkinter, it becomes difficult to determine at a glance whether a function or class that appears out of the blue in the middle of the code is from tkinter or something else   

# So you can use 'import *' when you are doing mini project like this program, you should use 'import tkinter as tk' when you are in group project of using several libraries.
