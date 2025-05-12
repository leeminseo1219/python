import tkinter

def cal_button():

    num_coffeeSell = int(coffee_s.get())*1800 
    num_coffeePur = int(coffee_p.get())*500
    num_samgimSell = int(samgim_s.get())*1400
    num_samgimPur = int(samgim_p.get())*900
    num_banamilkSell = int(banamilk_s.get())*1800
    num_banamilkPur = int(banamilk_p.get())*800
    num_dosiSell = int(dosi_s.get())*4000
    num_dosiPur = int(dosi_p.get())*3500
    num_colaSell = int(cola_s.get())*1500
    num_colaPur = int(cola_p.get())*700
    num_ggangSell = int(ggang_s.get())*2000
    num_ggangPur = int(ggang_p.get())*1000

    

    sum_Pur = int(num_coffeePur) + int(num_samgimPur) + int(num_banamilkPur) + int(num_dosiPur) + int(num_colaPur) + int(num_ggangPur)
    sum_Sell = int(num_coffeeSell) +int(num_samgimSell) + int(num_banamilkSell) + int (num_dosiSell) +int(num_colaSell) +int(num_ggangSell)
    sum = sum_Sell - sum_Pur

    str1 = "오늘 총 매출액은"+str(sum)+"원 입니다."

    result = tkinter.Label(root,text=str1)
    result.place(x=100,y=330)


root = tkinter.Tk()

root.title("CU")
root.geometry("900x400")

coffee = tkinter.Label(root,text="캔커피")
coffee.place(x=120,y=70)

samgim = tkinter.Label(root,text="삼각김밥")
samgim.place(x=220,y=70)

banamilk = tkinter.Label(root,text="바나나 우유")
banamilk.place(x=320,y=70)

dosi = tkinter.Label(root,text="도시락")
dosi.place(x=420,y=70)

cola = tkinter.Label(root,text="콜라")
cola.place(x=520,y=70)

ggang = tkinter.Label(root,text="새우깡")
ggang.place(x=620,y=70)

sell = tkinter.Label(root,text="판매 수량")
sell.place(x=10,y=120)
pur = tkinter.Label(root,text="구매 수량")
pur.place(x=10,y=180)

coffee_s = tkinter.Entry(width=5)
coffee_s.place(x=120,y=120)
samgim_s = tkinter.Entry(width=5)
samgim_s.place(x=225,y=120)
banamilk_s = tkinter.Entry(width=5)
banamilk_s.place(x=330,y=120)
dosi_s = tkinter.Entry(width=5)
dosi_s.place(x=420,y=120)
cola_s = tkinter.Entry(width=5)
cola_s.place(x=515,y=120)
ggang_s = tkinter.Entry(width=5)
ggang_s.place(x=620,y=120)

coffee_p = tkinter.Entry(width=5)
coffee_p.place(x=120,y=180)
samgim_p = tkinter.Entry(width=5)
samgim_p.place(x=225,y=180)
banamilk_p = tkinter.Entry(width=5)
banamilk_p.place(x=330,y=180)
dosi_p = tkinter.Entry(width=5)
dosi_p.place(x=420,y=180)
cola_p = tkinter.Entry(width=5)
cola_p.place(x=515,y=180)
ggang_p = tkinter.Entry(width=5)
ggang_p.place(x=620,y=180)

cal = tkinter.Button(root, text="계산", command=cal_button)
cal.place(x=100,y=230,width=570,height=45)

root.mainloop()
