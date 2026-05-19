from tkinter import *

window = Tk()

selected_role = StringVar()

selected_role.set('부원')

club_members = {}

def search_member():
    mem_number = e1.get()
    if mem_number in club_members:
        club_info = club_members[mem_number]
        l4.config(text = f'학번: {mem_number}, 이름: {club_info["이름"]}, 역할: {club_info["역할"]}')  
        # f-string오류를 방지하기 위해 "와 '를 구분해야 한다 / should use " and ' distinctly to prevent f-sting error (confuse start-end' and key ')
        e1.delete(0, END)
    elif len(e1.get()) == 0:
        l4.config(text = '학번을 입력해주세요')
        e1.delete(0, END)
    else:
        l4.config(text = '해당 학번은 명단에 존재하지 않습니다.')
        e1.delete(0, END)
        
def add_member():
    mem_number = e2.get()
    mem_name = e3.get()
    mem_role = selected_role.get()
    if mem_number in club_members:
        l4.config(text = '해당 학번은 이미 존재합니다.')
    elif len(e2.get()) == 0 or len(e3.get()) == 0:
        l4.config(text = '이름과 학번을 정확히 입력해주세요')
    else:
        club_members[mem_number] = {'이름': mem_name, '역할': mem_role}
        l4.config(text = f'추가가 완료되었습니다.\n학번: {mem_number}, 이름: {mem_name}, 역할: {mem_role}')
        e2.delete(0, END)
        e3.delete(0, END)

def view_member():
    output_text = ""

    if not club_members:
        l4.config(text = '명단이 비었습니다.')
        return
    
    for num, item in club_members.items():
        output_text += f'학번: {num}, 이름: {item["이름"]}, 역할: {item["역할"]}\n'

    l4.config(text = output_text)


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

window.mainloop()
