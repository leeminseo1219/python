import tkinter
import tkinter.font

def click_btn():
    labelE = tkinter.Label(root, text="동")
    labelE.place(x=300, y=200)
    labelW = tkinter.Label(root, text="서")
    labelW.place(x=100, y=200)
    labelN = tkinter.Label(root, text="남")
    labelN.place(x=200, y=100)
    labelS = tkinter.Label(root, text="북")
    labelS.place(x=200, y=300)
    
    txt =entry.get()
    str1 = txt
    labeltxt = tkinter.Label(root, text=str1, font=("돋움",24))
    labeltxt.place(x=250, y=350)

root = tkinter.Tk()

root.title("첫 번째 윈도우")
root.geometry("800x600")

button = tkinter.Button(root, text="버튼",command=click_btn())
button.place(x=200, y=200,width=32,height=32)        

entry=tkinter.Entry(width=5)
entry.place(x=200, y=350)

root.mainloop()


