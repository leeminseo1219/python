import tkinter
import random
import tkinter.messagebox

root = tkinter.Tk()

root.title("체크버튼 실습")


result = [
    "전생에 고양이었을 가능성은 매우 낮습니다."
    "보통 사람입니다."
    "꽤 고양이다운 구석이 있습니다."
    "고양이와 비슷한 성격같습니다."
    "고양이와 근접한 성격입니다"
    "전생에 고양이었을지도 모릅니다"
    "겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다."
]


#체크버튼 클릭시
def chkBtnClick():
    numCheck = 0
    if cvalue1.get()==True:numCheck +=1
    if cvalue2.get()==True:numCheck +=1
    if cvalue3.get()==True:numCheck +=1
    if cvalue4.get()==True:numCheck +=1
    if cvalue5.get()==True:numCheck +=1
    if cvalue6.get()==True:numCheck +=1
    if cvalue7.get()==True:numCheck +=1
    print(numCheck)    
   
#버튼 클릭시
def BtnClick():
    numCheck = 0
    if cvalue1.get()==True:numCheck +=1
    if cvalue2.get()==True:numCheck +=1
    if cvalue3.get()==True:numCheck +=1
    if cvalue4.get()==True:numCheck +=1
    if cvalue5.get()==True:numCheck +=1
    if cvalue6.get()==True:numCheck +=1
    if cvalue7.get()==True:numCheck +=1
    print(numCheck)
    textField.delete("1.0",tkinter.END) #처음부터 끝까지 지우고 다시 작성해줌
    textField.insert("1.0","<진단결과>\n 당신의 고양이 지수는"
                     +str(int(numCheck/7*100))+"%입니다. \n"
                     + result[numCheck])

        #print("체크 되었습니다.")
                #tkinter.messagebox.showinfo("제목","내용")
                #tkinter.messagebox.showwarning("제목","내용")
                #tkinter.messagebox.showerror("제목","내용")
                #answer = tkinter.messagebox.askyesno("제목","게임에 참가하시겠습니까?")
                #if answer == True:
                #    print("동의")
                #else:
                #    print("거절")

#좌표출력기
def mouseMove(event):
    x =event.x
    y = event.y
    labelMouse["text"]=str(x)+","+str(y)

root.bind("<Motion>",mouseMove)
labelMouse = tkinter.Label(root,text=",",font=("맑은 고딕",10))
labelMouse.pack()



canvas = tkinter.Canvas(root, width=800, height=600,bg="skyblue")
canvas.pack()

bgimg = tkinter.PhotoImage(file="mina.png")
canvas.create_image(400,300,image=bgimg)

#체크버튼
ygap =40
cvalue1 = tkinter.BooleanVar()
cvalue1.set(False)
cbtn1 = tkinter.Checkbutton(text = "높은 곳이 좋다.", variable=cvalue1, command=chkBtnClick)
cbtn1.place(x=402,y=165)

cvalue2 = tkinter.BooleanVar()
cvalue2.set(False)
cbtn2 = tkinter.Checkbutton(text = "공을 보면 굴리고 싶어진다.", variable=cvalue2, command=chkBtnClick)
cbtn2.place(x=100,y=165+ygap*1)

cvalue3 = tkinter.BooleanVar()
cvalue3.set(False)
cbtn3 = tkinter.Checkbutton(text = "깜짝놀라면 털이 곤두선다.", variable=cvalue3, command=chkBtnClick)
cbtn3.place(x=100,y=165+ygap*2)

cvalue4 = tkinter.BooleanVar()
cvalue4.set(False)
cbtn4 = tkinter.Checkbutton(text = "쥐구멍이 마음에 든다.", variable=cvalue4, command=chkBtnClick)
cbtn4.place(x=100,y=165+ygap*3)

cvalue5 = tkinter.BooleanVar()
cvalue5.set(False)
cbtn5= tkinter.Checkbutton(text = "개에게 적대감을 느긴다", variable=cvalue5, command=chkBtnClick)
cbtn5.place(x=100,y=165+ygap*4)

cvalue6 = tkinter.BooleanVar()
cvalue6.set(False)
cbtn6= tkinter.Checkbutton(text = "생선 뼈를 발라먹고 싶다.", variable=cvalue6, command=chkBtnClick)
cbtn6.place(x=100,y=165+ygap*5)

cvalue7 = tkinter.BooleanVar()
cvalue7.set(False)
cbtn7= tkinter.Checkbutton(text = "밤, 기운이 난다", variable=cvalue7, command=chkBtnClick)
cbtn7.place(x=100,y=165+ygap*6)


textField = tkinter.Text()
textField.place(x=330, y=50, width=420, height=90)

btn = tkinter.Button(command=BtnClick)
btn.place(x=430, y=480)

root.mainloop()

#w=420,h=90
#ckbtn x=150, y=60