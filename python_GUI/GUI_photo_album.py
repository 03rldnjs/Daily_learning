from tkinter import *
i = 1
def p1():
    global i
    i -= 1
    if i == 0:
        i = i + 4
        l1.config(image = photo_list[3])
    else:
        l1.config(image = photo_list[i % 4])
def p2():
    global i
    i += 1
    if i == 4:
        i = i - 4
        l1.config(image = photo_list[0])
    else:
        l1.config(image = photo_list[i % 4]) 


window = Tk()

photo1 = PhotoImage(file = '그림1.gif')
photo2 = PhotoImage(file = '그림2.gif')
photo3 = PhotoImage(file = '그림3.gif')
photo4 = PhotoImage(file = '그림4.gif')

photo_list = [photo1, photo2, photo3, photo4]

l1 = Label(window, image = photo1)
l1.grid(row = 0, column = 0, columnspan = 2)

b1 = Button(window, text = '이전', command = p1, width = 16)
b1.grid(row = 1, column = 0)

b2 = Button(window, text = '다음', command = p2, width = 16)
b2.grid(row = 1, column = 1)


window.mainloop()

# 초안 / draft
