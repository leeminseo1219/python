import tkinter

root = tkinter.Tk()
root.title("제목")
root.geometry("300x300")

file = open("test.txt","r", encoding="UTF-8")


strFile = file.readline()
root.geometry(strFile.rstrip("\n"))

strFile = file.readline()
root.title(strFile[:-1])


file.close()

root.mainloop()


'''
while True:
    str = file.readline()
    print(str, end='')
    if(str == ""):
        break
'''

'''
fileList = file.readlines()
index = 1
for strList in fileList   :
    print(str(index)+"  :   "+strList, end="")
    index = index+1

'''

'''
fileList = file.readlines()
for strList in fileList   :
    print(strList, end="")

strFile = file.readline()
root.title("제목")

strFile = file.readline()
root.title("300x300")
'''