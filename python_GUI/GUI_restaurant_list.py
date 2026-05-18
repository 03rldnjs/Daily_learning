from tkinter import *

window = Tk()

restaurants = {}

def search_list():
    rest_name = e1.get()
    if rest_name in restaurants:
        l3.config(text = f'식당 이름: {rest_name}, 대표 메뉴: {restaurants[rest_name]}')
        e1.delete(0, END)
    else:
        l3.config(text = '검색하신 식당은 리스트에 존재하지 않습니다.')
    
def add_list():
    if len(e2.get()) == 0 or len(e3.get()) == 0:
        l3.config(text = '식당 이름과 메뉴를 모두 입력해주세요')
        return

    rest_name = e2.get()
    menu_name = e3.get()
    restaurants[rest_name] = menu_name
    l3.config(text = f'추가가 완료되었습니다.\n추가 내역: {rest_name} : {menu_name}')
    e2.delete(0, END)
    e3.delete(0, END)

def view_list():
    # l3.config(text = f'{restaurants}')  처음에 사용했던 원시적인 방법
    output_text = ""

    if not restaurants:
        l3.config(text = '저장된 식당이 없습니다.')
        return
    
    for rest, men in restaurants.items():
        output_text += f'식당 이름: {rest} | 대표 메뉴: {men}\n'

    l3.config(text = output_text)

window.title("맛집 리스트")

l_first = Label(window, text = '식당 검색')
l_first.grid(row = 0, column = 0)

e1 = Entry(window)
e1.grid(row = 0, column = 1)

b1 = Button(window, text = '검색', width = 10, command = search_list)
b1.grid(row = 0, column = 2)

l1 = Label(window, text = '식당 이름')
l1.grid(row = 1, column = 0)

e2 = Entry(window)
e2.grid(row = 1, column = 1)

l2 = Label(window, text = '메뉴 이름')
l2.grid(row = 2, column = 0)

e3 = Entry(window)
e3.grid(row = 2, column = 1)

b2 = Button(window, text = '추가', width = 10, command = add_list)
b2.grid(row = 2, column = 2)

l3 = Label(window, text = '맛집 리스트')
l3.grid(row = 3, column = 0, columnspan = 3, pady = 10)

b3 = Button(window, text = '전체 식당 리스트', width = 20, command = view_list)
b3.grid(row = 4, column = 0, columnspan = 3, pady = 5)

window.mainloop()
