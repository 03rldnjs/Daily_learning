from tkinter import *  
#from import를 사용하면 라이브러리 내부의 함수를 사용할 때 클래스를 앞에 붙이지 않아도 된다 / you don't have to add the name of class when you use from import

window = Tk()  # tkinter에 들어있는 클래스를 window라는 이름의 객체로 생성시킴 / create instance of 'class Tk()' which is included in tkinter library

restaurants = {}  # 공백 딕셔너리 생성 / create empty dictionary

# 식당 이름 검색 함수 / method that can search restaurant's name in dictionary
def search_list():
    rest_name = e1.get()  
    if rest_name in restaurants:
        l3.config(text = f'식당 이름: {rest_name}, 대표 메뉴: {restaurants[rest_name]}')
        e1.delete(0, END)  # 버튼을 누른 다음 entry 내부 청소 / clear the entry after the button was pressed
    else:
        l3.config(text = '검색하신 식당은 리스트에 존재하지 않습니다.')  

# 식당 추가 함수 / method that can add new restaurant
def add_list():
    if len(e2.get()) == 0 or len(e3.get()) == 0:
        l3.config(text = '식당 이름과 메뉴를 모두 입력해주세요')
        return

    rest_name = e2.get()
    menu_name = e3.get()
    restaurants[rest_name] = menu_name
    l3.config(text = f'추가가 완료되었습니다.\n추가 내역: {rest_name} : {menu_name}')
    e2.delete(0, END)   # 번튼을 누른 다음 entry 내부 청소 / clear the entry after the button was pressed
    e3.delete(0, END)  

# 식당 리스트 출력 함수 / method that can print list of restaurants
def view_list():
    # l3.config(text = f'{restaurants}')  처음에 사용했던 원시적인 방법
    output_text = ""  # 공백 문자열 생성 / create empty string

    if not restaurants:  # 딕셔너리가 공백인 경우 출력할 내용 / print warning sign when dictionary is empty
        l3.config(text = '저장된 식당이 없습니다.')
        return
    
    for rest, men in restaurants.items():  # items()함수를 활용하여 식당 이름과 메뉴를 각각 언패킹 / unpack the keys and values respectly by function 'items()'
        output_text += f'식당 이름: {rest} | 대표 메뉴: {men}\n'  # 식당 이름과 대표 메뉴를 줄바꿈 문자를 포함하여 text에 추가 / add restaurant' name and menu with \n in text

    l3.config(text = output_text)  # .config()는 줄바꿈 문자도 잘 표현함 / .config() can express \n very well

window.title("맛집 리스트") 

# GUI 화면 레이아웃 조정부 / GUI window layout control part
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
