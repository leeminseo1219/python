import tkinter
import random
from PIL import ImageTk,Image

root = tkinter.Tk()
root.title("캔버스 만들기")

def mouseMove(event):
    x =event.x
    y = event.y
    labelMouse["text"]=str(x)+","+str(y)

def click_btn():
    label["text"] = random.choice(["대길","중길","소길","흉"])


canvas = tkinter.Canvas(root, width=800, height=600,bg="skyblue")
canvas.pack

root.bind("<Motion>",mouseMove)
labelMouse = tkinter.Label(root,text=",",font=("맑은 고딕",10))
labelMouse.pack()

#bgimg = tkinter.PhotoImage(file = "miko.png")
bgimg = ImageTk.PhotoImage(Image.open("c:\Users\user\Desktop\miko.png"))
canvas.create_image(400,300,image=bgimg)

label = tkinter.Label(root,text="??",font=("맑은 고딕",120))
label.place(x=300, y=60)

button = tkinter.Button(root,text="제비뽑기",font=("맑은 고딕",100),command=click_btn)
button.place(x=360,y=400)




root.mainloop()