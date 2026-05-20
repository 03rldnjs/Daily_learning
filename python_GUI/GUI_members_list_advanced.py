from tkinter import *

window = Tk()
window.title("동아리 부원 관리 시스템")
window.geometry("450x380")  # 창 크기를 명확하고 여유 있게 지정

selected_role = StringVar()
selected_role.set('부원')

club_members = {}

# --- 기능 함수 구역 ---
def search_member():
    mem_number = e1.get()
    if mem_number in club_members:
        club_info = club_members[mem_number]
        l4.config(text = f'검색 결과\n학번: {mem_number}\n이름: {club_info["이름"]}\n역할: {club_info["역할"]}')
        e1.delete(0, END)
    elif len(e1.get()) == 0:
        l4.config(text = '학번을 입력해주세요.')
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
        l4.config(text = '이름과 학번을 정확히 입력해주세요.')
    else:
        club_members[mem_number] = {'이름': mem_name, '역할': mem_role}
        l4.config(text = f'추가가 완료되었습니다!\n학번: {mem_number} | 이름: {mem_name} | 역할: {mem_role}')
        e2.delete(0, END)
        e3.delete(0, END)

def view_member():
    output_text = ""
    if not club_members:
        l4.config(text = '명단이 비었습니다.')
        return
    
    output_text += "[전체 동아리원 명부]\n"
    for num, item in club_members.items():
        output_text += f'- 학번: {num} | 이름: {item["이름"]} | 역할: {item["역할"]}\n'
    l4.config(text = output_text)


# --- UI 레이아웃 개선 구역 ---

# 1. 상단 검색 프레임 (LabelFrame을 쓰면 테두리가 생김)
search_frame = LabelFrame(window, text=" 부원 검색 ", padx=10, pady=10)
search_frame.pack(fill="x", padx=15, pady=10)

e1 = Entry(search_frame, width=25)
e1.grid(row=0, column=0, padx=5)

b1 = Button(search_frame, text = '검색', width = 10, bg="#e1e1e1", command = search_member)
b1.grid(row = 0, column = 1, padx=5)


# 2. 중단 정보 등록 프레임
add_frame = LabelFrame(window, text=" 신규 등록 ", padx=10, pady=10)
add_frame.pack(fill="x", padx=15, pady=5)

l1 = Label(add_frame, text = '학번 :')
l1.grid(row = 0, column = 0, sticky=E, pady=3)
e2 = Entry(add_frame, width = 25)
e2.grid(row = 0, column = 1, padx=10, pady=3, columnspan=2, sticky=W)

l2 = Label(add_frame, text = '이름 :')
l2.grid(row = 1, column = 0, sticky=E, pady=3)
e3 = Entry(add_frame, width = 25)
e3.grid(row = 1, column = 1, padx=10, pady=3, columnspan=2, sticky=W)

l3 = Label(add_frame, text = '역할 :')
l3.grid(row = 2, column = 0, sticky=E, pady=3)

# OptionMenu 가로 크기를 깔끔하게 늘려주기 위해 width 옵션 추가
op1 = OptionMenu(add_frame, selected_role, '회장','총무','부원')
op1.config(width=10)
op1.grid(row = 2, column = 1, padx=10, pady=3, sticky=W)

b2 = Button(add_frame, text = '등록', width = 10, bg="#4CAF50", fg="white", command = add_member)
b2.grid(row = 2, column = 2, padx=5, pady=3, sticky=W)


# 3. 하단 기능 및 출력 구역
b3 = Button(window, text = '전체 명부 보기 📋', width = 20, command = view_member)
b3.pack(pady = 10)

# 결과 창을 스크롤이나 긴 글도 안 잘리게 좌측 정렬(justify, sticky) 적용
# 시각적 편안함을 위해 x축 방향 여백 지정 (padx = 20)
l4 = Label(window, text = '결과가 여기에 표시됩니다.', fg="blue", justify=LEFT, anchor="nw", padx = 20)  
l4.pack(fill="both", expand=True, padx=20, pady=5)

window.mainloop()
