import tkinter

##애니메이션 생성의 기초초

#전역 변수
tmr = 0


##함수 선언
def countUp():
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    root.after(100,countUp)

root = tkinter.Tk()

## 메인 함수
root.title("타이머")
root.geometry("300x200")
label = tkinter.Label(text="0",font=("궁서체",80))
label.pack()
root.after(100,countUp)

root.mainloop()