import tkinter
root = tkinter.Tk()

def old_con():


    if int(old.get())>=0 and int(old.get())<3:
        fee=0
    elif int(old.get())>=3 and int(old.get())<99:
        fee=19000
    else:
        fee=0

    notion = "고갱님이 내실 요금은"+str(fee)+"원 입니다."
    
    fee_notion=tkinter.Label(root, text=notion)
    fee_notion.place(x=340,y=220, width=250,height=90)




root.title("니얼굴공화국")
root.geometry("900x900")

welcome= tkinter.Label(root, text="니얼굴공화국에 오신 것을 진심으로 환영합니다.", font=("돋움",16))
welcome.place(x=100,y=40, width=500,height=100)

desk=tkinter.Label(root, text="* 니얼굴공화국 요금소",font=("돋움",14))
desk.place(x=110,y=150, width=200,height=50)

how_old=tkinter.Label(root, text="나이를 입력해주세요",font=("돋움",12))
how_old.place(x=105,y=200, width=180,height=50)

old = tkinter.Entry(width=6)
old.place(x=290, y=215)

old_button = tkinter.Button(root, text="확인",command=old_con)
old_button.place(x=340,y=210)


root.mainloop()

