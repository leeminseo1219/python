import tkinter

#전역변수 선언

key = 0
cx = 400
cy = 300

#함수영역

def main_proc():
    global cx,cy,key

    #label["text"] = key
    #키보드입력으로 위치변경
    if key =="Up":
        cy-=20
    if key =="Down":
        cy+=20
    if key =="Left":
        cx = cx-20
    if key =="Right":
        cx =cx+20

    #변경된 위치의 경계를 확인
    if cy < 40 : cy = 40
    if cy > 600-40 : cy = 600-40
    if cx < 40 : cx = 40
    if cx > 800-40 : cx = 800-40

    #변경된 위치에 이미지를 옮김김
    canvas.coords("스티커",cx,cy)
    key=0

    root.after(100,main_proc) #자기자신을 호출하는 함수(0.1초 간격)

def key_down(e):
    global key
    key= e.keysym #keycode

def key_up(e):
    global key
    key= 0


#메인영역

root = tkinter.Tk()
root.title("키 이벤트")
root.bind("<KeyPress>",key_down) #bind는 함수등록 함수:키프레스가 될 때마다 키프레스함수가 실행됨
root.bind("<KeyRelease>",key_up)
#label =tkinter.Label(font=("맑은 고딕",80))
#label.pack()

canvas = tkinter.Canvas(width=800,height=600,bg='skyblue')
canvas.pack()

img=tkinter.PhotoImage(file="sticker.png")
canvas.create_image(400,300,image=img)
#canvas.coords("스티커",cx,cy)


main_proc()
root.mainloop()
