
p = input("파운드(lb)를 입력하세요: ")
kg = input("킬로그램(kg)을 입력하세요: ")

p_cal = p*0.453592
kg_cal = kg*2.204623

print(p+"파운드(lb)는"+round(p_cal,5)+"킬로그램(kb)입니다.")
print(kg+"킬로그램(kg)는"+round(kg_cal,5)+"파운드(lb)입니다.")
