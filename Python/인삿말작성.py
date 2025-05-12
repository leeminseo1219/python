# '''
# # num1= int(input("숫자1==> "))
# # num2= int(input("숫자2==> "))

# # print(num1,"+",num2,"=",num1+num2)
# # print(num1,"-",num2,"=",num1-num2)
# # print(num1,"*",num2,"=",num1*num2)
# # print(num1,"/",num2,"=",num1/num2)
# # print(num1,"%",num2,"=",num1%num2)
# # print(num1,"**",num2,"=",num1**num2)
# # '''


# '''
# print("## 택배를 보내기 위한 정보를 입력하세요. ##")
# rec = str(input("받는 사람: "))
# adress = str(input("주소: "))
# g = int(input("무게(g): "))

# g_fee = g*5

# print("** 받는 사람 ==>",rec)
# print("** 주소 ==>",adress)
# print("** 배송비 ==>",g_fee, "원")
# '''


# '''
# import tkinter
# root = tkinter.Tk()

# def click_btn():
#     btn["text"] = "클릭했습니다."

# root.title("버튼클릭판정 시스템")
# root.geometry("800x600")
# btn = tkinter.Button(root, text="클릭하십시오",command=click_btn)
# btn.place(x=500, y=500)

# root.mainloop()

# '''

# '''
# import tkinter
# root = tkinter.Tk()

# def gett():
#     txt = entry1.get()
#     e_b["text"]=txt

# root.title("필드 입력값 받아오기")
# root.geometry("400x200")

# entry1 = tkinter.Entry(width=30)
# entry1.place(x=150,y=100)

# e_b = tkinter.Button(root, text="문자열 얻기", command=gett)
# e_b.place(x=150, y=140)

# root.mainloop()

# '''

# '''
# import tkinter

# def cal():

#     ded_g=int(entry1.get())  #변수 명이 아닌 계산식에서서 int형으로 바꿔줘야함
#     der_g=int(entry2.get())

#     m1 = int(ded_g // der_g)
#     n1 = int(ded_g % der_g)


#     m2_t=str(ded_g)+"을(를)"+str(der_g)+"로 나눈 몫은"+ str(m1)+"입니다."
#     n2_t=str(ded_g)+"을(를)"+str(der_g)+"로 나눈 나머지는"+ str(n1)+"입니다."

#     m2 = tkinter.Label(root, text=m2_t)
#     m2.place(x=30, y=160)
#     n2 = tkinter.Label(root, text=n2_t)
#     n2.place(x=30, y=190)

# root = tkinter.Tk()
# root.title("입력된 수의 나머지와 몫 구하기")
# root.geometry("400x300")

# ded=tkinter.Label(root, text="나눠 지는 수")
# ded.place(x=30,y=50)
# der=tkinter.Label(root, text="나누는 수")
# der.place(x=30,y=90)

# entry1 = tkinter.Entry(width=9)
# entry2 = tkinter.Entry(width=9)
# entry1.place(x=140,y=50)
# entry2.place(x=140,y=90)

# cal_b= tkinter.Button(root,text="계산",command=cal)
# cal_b.place(x=220,y=50,width=50,height=70)

# root.mainloop()

# '''

# '''
# b = int(input("파운드를(1b) 입력하세요: "))
# b_to_kg=float(b * 0.453592)
# print(b,"파운드(lb)는",b_to_kg,"킬로그램(kb)입니다.")

# kg = int(input("킬로그램을(kg) 입력하세요: "))
# kg_to_b=float(kg * 2.204623)
# print(kg,"킬로그램(kg)는",kg_to_b,"파운드(lb)입니다.")
# '''

# '''
# import tkinter

# def cal():
#     cof_purp= 500 * int(cof_pur.get())
#     cof_sellp = 1800 *int(cof_sell.get())
#     sam_purp = 900 * int(sam_pur.get())
#     sam_sellp = 1400 * int(sam_sell.get())
#     dosi_purp = 3500 * int(dosi_pur.get())
#     dosi_sellp = 4000 *int(dosi_sell.get())

#     all_pur = int(cof_purp)+int(sam_purp)+int(dosi_purp)
#     all_sell =int(cof_sellp)+int(sam_sellp)+int(dosi_sellp)
#     total = int(all_sell)-int(all_pur)

#     str1 = "오늘의 총 매출은"+str(total)+" 원 입니다."
#     notion=tkinter.Label(root, text=str1)
#     notion.place(x=100 , y=320)

    

# root = tkinter.Tk()
# root.title("편의점 매출")
# root.geometry("600x400")

# cof = tkinter.Label(root,text="캔커피")
# sam = tkinter.Label(root, text="삼각김밥")
# dosi = tkinter.Label(root, text="도시락")
# cof.place(x=100,y=80)
# sam.place(x=200,y=80)
# dosi.place(x=300,y=80)

# cof_sell = tkinter.Entry(width=9)
# cof_pur = tkinter.Entry(width=9)
# cof_sell.place(x=100, y=140)
# cof_pur.place(x=100, y=200)

# sam_sell = tkinter.Entry(width=9)
# sam_pur = tkinter.Entry(width=9)
# sam_sell.place(x=200, y=140)
# sam_pur.place(x=200, y=200)

# dosi_sell = tkinter.Entry(width=9)
# dosi_pur = tkinter.Entry(width=9)
# dosi_sell.place(x=300, y=140)
# dosi_pur.place(x=300, y=200)

# sell = tkinter.Label(root, text="판매 수량")
# pur = tkinter.Label(root, text="구매 수량")
# sell.place(x=10,y=140)
# pur.place(x=10,y=200)

# cal_b = tkinter.Button(root, text="계산", command=cal)
# cal_b.place(x=100, y=260,width=240,height=40)


# root.mainloop()
# '''

# '''
# var1 = input("첫번째 문자열 ==> ")
# var2 = input("두번째 문자열 ==> ")

# len1 = len(var1)
# len2 = len(var2)

# diff = len1 - len2
# print("두 문자열의 길이차이는",diff,"입니다.")
# '''

# '''
# var1 = input("4자리 문자열을 입력하세요 ==> ")
# var1_Out = var1[3]+var1[2]+var1[1]+var1[0]

# print(var1_Out)
# '''

# """
# import tkinter
# root = tkinter.Tk()
# root.title("캔버스 연습")
# #캔버스의 크기가 윈도우의 크기가 되므로 지오메트리는 생략해도 됨
# canvas = tkinter.Canvas(root,width=400, height=600, bg="skyblue")
# canvas.pack()
# toro = tkinter.PhotoImage(file=r"C:\Users\my\Downloads\brain (1).png") #사이즈가 크거나 하면 출력이 안 될수도 있음, 그리고 경로 따옴표 앞에 r을 적어서 raw string처리 해주면 오류X
# canvas.create_image(200,300,image=toro)

# root.mainloop()
# """


# num =int(input("수를 입력해주세요 ==> "))              #블록 전체 선택하고 ctrl + / 같이 누르면 전체 주석처리됨 !!

# if num < 100:
#     print("100보다 작군요.")
# else:
#     print("100보다 크군요.")
#     print("프로그램 종료.")


# num = int(input("숫자를 입력하라 ==> "))

# if num % 2 == 0:
#     print("입력하신 숫자는 짝수입니다.")
# else:
#     print("입력하신 숫자는 홀수입니다.")



# score = int(input("점수를 입력하시오: "))

# if score >= 90:
#     print("니 성적은 A")
# elif score >= 80:
#     print("니 성적은 B")
# elif score >= 70:
#     print("니 성적은 C")
# elif score >= 60:
#     print("니 성적은 D")
# else:
#     print("니 성적은 F")
# print("학점입니다.")


# age = int(input("나이를 입력 ==> "))

# if age<18:
#     print("집에 갈 시간이네요!")
#     print("협조 감사합니다.")
# else:
#     print("협조 감사합니다.")


# i, hap = 0,0
# for i in range(500,1001,2):
#     hap += i
# print("500에서 1000까지의 짝수의 합: ", hap)



# for i in range(2,10,1):
#     for k in range(1,10,1):
#         print(i,"X",k,"=",i*k,"\n", end='')



hap=0

for i in range(1,101,1):
    if i%4==0:
        continue
    hap+=i

print(hap)

    