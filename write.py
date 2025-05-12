
outFile = open("outTest.txt", "w", encoding="UTF-8")

outStr = input("내용입력 ==> ")
outFile.writelines(outStr+"\n")

while True :
    outStr = input("내용입력 ==> ")
    #'끝'이라고 입력하면 종료
    if outStr == '끝':
        break
    outFile.writelines(outStr+"\n")

outFile.close()