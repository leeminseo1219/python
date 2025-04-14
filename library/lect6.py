
# 실습 1
#팩토리아 계산기: 1부터 N까지의 합

N = 5
res = 1
for i in range(1,N+1,1):
    res = res*i

#print(res) #120

#연습 1
#1000에서 2000사이의 홀수의 합을 구하는 프로그램

hap = 0
for i in range(1003, 2001,2):
    hap = hap+i+1002

print(hap)

#중첩for문
#for i in range()
pass

#실습 2
#2단부터 9단까지의 구구단 출력하는 구구단 계산기
#for num1 in range(2,10,1):
#    print("--------구구단",num1,"단----------")
#    for num2 in range(1,10,1):
#        print(num1,"X",num2,"=\t",num1*num2)

#while문
#while(True):
 #   num1 =  int(input("숫자1==> "))
 #   #num1이 0이면 반복문 종료
 #   if num1 == 0:
 #       break

 #   num2 =  int(input("숫자2==> "))
 # print(num1,"+",num2,"=",num1+num2)

#연습2
#1부터 100까지의 수를 더하되 4의 배수를 더하지 않음.
#3의 배수도 더하지 않음음

res = 0 
for i in range(1,101,1):
    if i % 4 ==0:
        continue
    elif i % 3 ==0:
        continue
    res=res+i
print(res)

