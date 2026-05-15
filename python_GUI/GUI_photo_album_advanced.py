from tkinter import *

# 1. 현재 사진의 위치(인덱스)는 0부터 시작하는 게 정석
current_idx = 0

def update_image():
    # 사진을 바꾸는 중복 코드를 함수로 합치면 관리에 용이
    l1.config(image=photo_list[current_idx])

def p1(): # 이전 버튼
    global current_idx
    # (현재인덱스 - 1)을 전체개수로 나눈 나머지 -> 자동으로 마지막으로 돌아감
    current_idx = (current_idx - 1) % len(photo_list)
    update_image()

def p2(): # 다음 버튼
    global current_idx
    # (현재인덱스 + 1)을 전체개수로 나눈 나머지 -> 자동으로 0으로 돌아감
    current_idx = (current_idx + 1) % len(photo_list)
    update_image()

window = Tk()
window.title("나의 사진 앨범")

# 리스트 컴프리헨션(고급기술!)으로 사진을 한 번에 불러오기
# 그림1.gif ~ 그림4.gif가 있다고 가정
photo_list = [PhotoImage(file=f'그림{i}.gif') for i in range(1, 5)]

l1 = Label(window, image=photo_list[0])
l1.grid(row=0, column=0, columnspan=2)

b1 = Button(window, text='이전', command=p1, width=16)
b1.grid(row=1, column=0)

b2 = Button(window, text='다음', command=p2, width=16)
b2.grid(row=1, column=1)

window.mainloop()
