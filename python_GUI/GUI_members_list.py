from tkinter import *  # tkinter 라이브러리 활용을 위한 import / import tkinter for using tkinter library
# import tkinter도 같은 기능을 제공하지만 from tkinter import *로 적으면 앞에 객체명을 작성하지 않고 함수를 사용할 수 있음.
# 'import tkinter' can provide same funtion but you don't have to add the name of instance when you use 'from tkinter import *'

window = Tk()  # TK() class를 객체로 선언 / declare the class to instance

selected_role = StringVar() # tkinter 라이브러리에 있는 StringVar()라는 class를 selected_role이라는 이름의 객체로 선언
# declare StringVar() class to instance which is included in tkinter library

selected_role.set('부원') # 기본 출력값을 '부원'으로 지정 / '부원' is the default printing value

club_members = {} # 공백 딕셔너리 생성 / create empty dictionary

# 멤버 찾기 함수 / searching the member function
def search_member():
    mem_number = e1.get()
    if mem_number in club_members:
        club_info = club_members[mem_number]
        l4.config(text = f'학번: {mem_number}, 이름: {club_info["이름"]}, 역할: {club_info["역할"]}')  
        # f-string오류를 방지하기 위해 "와 '를 구분해야 한다 / should use " and ' distinctly to prevent f-sting error (confuse start-end' and key ')
        e1.delete(0, END)
    elif len(e1.get()) == 0:  # 아무것도 입력되지 않은 경우 공백이 딕셔너리에 추가되는 현상을 방지 / prevent creating empty dictionary when nothing is entered
        l4.config(text = '학번을 입력해주세요')
        e1.delete(0, END)
    else:
        l4.config(text = '해당 학번은 명단에 존재하지 않습니다.') 
        e1.delete(0, END)

# 멤버 추가 함수 / adding member function
def add_member():
    mem_number = e2.get()
    mem_name = e3.get()
    mem_role = selected_role.get()  # 
    if mem_number in club_members:
        l4.config(text = '해당 학번은 이미 존재합니다.')
    elif len(e2.get()) == 0 or len(e3.get()) == 0:
        l4.config(text = '이름과 학번을 정확히 입력해주세요')
    else:
        club_members[mem_number] = {'이름': mem_name, '역할': mem_role}
        l4.config(text = f'추가가 완료되었습니다.\n학번: {mem_number}, 이름: {mem_name}, 역할: {mem_role}')
        e2.delete(0, END)
        e3.delete(0, END)

# 전체 멤버 조회 함수 / view all members function
def view_member():
    output_text = ""

    if not club_members:  # 아무런 입력 없이 전체 멤버 조회 버튼을 누른 경우 출력할 문구 / text when nothing is included in dictionary
        l4.config(text = '명단이 비었습니다.')
        return  # end the function
    
    for num, item in club_members.items():   # 가독성을 위해 \n을 활용하기 위해 딕셔너리를 그대로 출력하는 것이 아니라 문자열에 언패킹하여 출력
        # unpacking the items of dictionary into string for readablity(string can print \n well)
        output_text += f'학번: {num}, 이름: {item["이름"]}, 역할: {item["역할"]}\n'

    l4.config(text = output_text) # for문을 통해 언패킹된 딕셔너리 item들을 한 번에 l4에 출력 / print the items of dictionary which is unpacked by for loop

# GUI 레이아웃 부분 / GUI layout part
e1 = Entry(window)
e1.grid(row = 0, column = 0)

b1 = Button(window, text = '검색', width = 10, command = search_member)
b1.grid(row = 0, column = 1)

l1 = Label(window, text = '학번')
l1.grid(row = 1, column = 0)

e2 = Entry(window)
e2.grid(row = 1, column = 1)

l2 = Label(window, text = '이름')
l2.grid(row = 2, column = 0)

e3 = Entry(window)
e3.grid(row = 2, column = 1)

l3 = Label(window, text = '역할')
l3.grid(row = 3, column = 0)

op1 = OptionMenu(window, selected_role, '회장','총무','부원')
op1.grid(row = 3, column = 1)

b2 = Button(window, text = '등록', width = 10, command = add_member)
b2.grid(row = 3, column = 2)

b3 = Button(window, text = '전체 명부 보기', width = 10, command = view_member)
b3.grid(row = 4, column = 0)

l4 = Label(window, text = '결과 출력창')
l4.grid(row = 5, column = 0, columnspan = 3)

window.mainloop()  # 잊기 쉽지만 절대 잊으면 안된다 / it's easy to forget but should not forget
