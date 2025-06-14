import tkinter
import random
from tkinter import *
from tkinter import messagebox

index = 0
timer = 0
score = 0
hisc = 1000
highScore = 0 #하이스코어
difficulty = 0
tsugi = 0

timeCounter = 0 #타이머 시간
tsugi_time = 0 #마지막으로 블럭 놓은시간

#조커블럭 관련 변수
# joker_flag = False      # 조커블럭 여부를 확인
# joker_count = 0        # 몇번째 블럭인지 세기
# joker_pos = (-1, -1)   # 조커블럭 좌표 기억 (턴 후 일반블럭 변환용)
# joker_time = 0         # 마지막 행동 시간 기억

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

neko = []
check = []
for i in range(12):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def draw_neko(): #
    cvs.delete("NEKO") #캔버스에서 "NEKO"을 삭제
    for y in range(12): #세로
        for x in range(10): #가로
            if 1 <= neko[y][x] <= 7: #모든 칸에 대해서 실행
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]], tag="NEKO") #NEKO생성

def check_neko():
    for y in range(12): #0,10,1
        for x in range(10): #모든 칸에 대해서 실행
            check[y][x] = neko[y][x] #neko->check (복사)

    for y in range(1,11):
        for x in range(10): #맨 위와 맨 아래줄을 제외한 모든칸에 대해서 실행
            if check[y][x] > 0: #세로 블럭
                if check[y - 1][x] == check[y][x] and check[y + 1][x] == check[y][x]:
                    neko[y - 1][x] = 7
                    neko[y][x] = 7
                    neko[y + 1][x] = 7

    for y in range(12):
        for x in range(1,9): #맨 왼쪽과 맨 오른쪽줄을 제외한 모든칸에 대해서 실행
            if check[y][x] > 0: #위아래양옆?
                if check[y][x - 1] == check[y][x] and check[y][x + 1] == check[y][x]:
                    neko[y][x - 1] = 7
                    neko[y][x] = 7
                    neko[y][x + 1] = 7

    for y in range(1,11):
        for x in range(1,9):
            if check[y][x] > 0: #대각선 블럭
                if check[y - 1][x - 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]:
                    neko[y - 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y + 1][x + 1] = 7

                if check[y + 1][x - 1] == check[y][x] and check[y - 1][x + 1] == check[y][x]:
                    neko[y + 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y - 1][x + 1] = 7

    for y in range(11): #블럭 4개가 사각형 모양으로 놓여져있을 때도 파괴
        for x in range(9): 
            if check[y][x] > 0:
                if check[y][x] == check[y+1][x] == check[y][x+1] == check[y+1][x+1]:
                    neko[y][x] = 7
                    neko[y+1][x] = 7
                    neko[y][x+1] = 7
                    neko[y+1][x+1] = 7


def sweep_neko():
    num = 0
    for y in range(12):
        for x in range(10): #모든 칸에 대해서 실행
            if neko[y][x] == 7:
                neko[y][x] = 0 #빈칸
                num = num + 1 #파괴된 블럭 개수를 표현
    return num

def drop_neko():
    flg = False 
    for y in range(10, -1, -1): #아래에서 위로 검사
        for x in range(10): #모든 블럭에 대해서 검사
            if neko[y][x] != 0 and neko[y + 1][x] == 0:
                neko[y + 1][x] = neko[y][x]
                neko[y][x] = 0
                flg = True
    return flg

def over_neko():
    for x in range(10):
        if neko[0][x] > 0: #맨 윗줄에 블럭이 있으면면
            return True #게임 종료
    return False

def set_neko():
        for x in range(10):
            neko[0][x] = random.randint(1, difficulty) #블럭을 생성(0번, 1~6:일반블럭)

def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)


def load_highScore():
    try:
        with open("highScore.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def save_highScore(score):
    with open("highScore.txt", "w") as f:
        f.write(str(score))

highScore = load_highScore() #불러오기


def esc_press(event): #esc키를 누르면 메세지창을 띄운다
    global index
    if index != 0: #게임 진행 중일 때
        result = messagebox.askyesno("게임 종료", "게임을 종료하시겠습니까?")
        if result:
            index = 0  #메인화면 인터페이스
            

def game_main():
    global index, timer, score, hisc, difficulty, tsugi
    global cursor_x, cursor_y, mouse_c
    global highScore #하이스코어 전역변수 선언
    global timeCounter #타이머 전역변수 선언
    global tsugi_time 

    if index == 0:  # 타이틀 로고
        draw_txt("야옹야옹", 378, 238, 100, "violet", "TITLE")
        cvs.create_rectangle(236, 382, 523.5, 453.5, fill="skyblue", width=0, tag="TITLE")
        draw_txt("Easy", 378, 412, 40, "white", "TITLE")
        cvs.create_rectangle(236, 526.4, 523.5, 598, fill="lightgreen", width=0, tag="TITLE")
        draw_txt("Normal", 378, 562, 40, "white", "TITLE")
        cvs.create_rectangle(236.6, 669.5, 524, 741.6, fill="orange", width=0, tag="TITLE")
        draw_txt("Hard", 378, 706, 40, "white", "TITLE")
        index = 1
        mouse_c = 0
    elif index == 1:  # 타이틀 화면, 시작 대기
        difficulty = 0
        if mouse_c == 1:
            if 168 < mouse_x and mouse_x < 456 and 384 < mouse_y and mouse_y < 456:
                difficulty = 4
            if 168 < mouse_x and mouse_x < 456 and 528 < mouse_y and mouse_y < 600:
                difficulty = 5
            if 168 < mouse_x and mouse_x < 456 and 672 < mouse_y and mouse_y < 744:
                difficulty = 6
        if difficulty > 0:
            for y in range(12):
                for x in range(10):
                    neko[y][x] = 0
            mouse_c = 0
            score = 0
            tsugi = 0
            cursor_x = 0
            cursor_y = 0
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 2
    elif index == 2:  # 블록 낙하
        if drop_neko() == False:
            index = 3
        draw_neko()
    elif index == 3:  # 나란히 놓인 블록 확인
        check_neko()
        draw_neko()
        index = 4
    elif index == 4:  # 나란히 놓인 고양이 블록이 있다면
        sc = sweep_neko()
        score = score + sc * difficulty * 2
        if score > hisc:
            hisc = score

        if score > highScore: #하이스코어 저장
            highScore = score
            save_highScore(highScore)

        if sc > 0:
            index = 2
        else:
            if over_neko() == False:
                tsugi = random.randint(1, difficulty)
                tsugi_time = timeCounter
                index = 5
            else:
                index = 6
                timer = 0
        draw_neko()

    elif index == 5:  # 마우스 입력 대기
        if  timeCounter - tsugi_time > 50:  # 5초 지나면 자동배치(50f)
            neko[cursor_y][cursor_x] = tsugi
            tsugi = 0
            index = 2
        else:
            if 24 <= mouse_x and mouse_x < 24 + 72 * 10 and 24 <= mouse_y and mouse_y < 24 + 72 * 12:
                cursor_x = int((mouse_x - 24) / 72) #칸 수만큼 입력 0~7/ 0-9
                cursor_y = int((mouse_y - 24) / 72) #칸 수만큼 입력 0~9/ 0-11
                if mouse_c == 1:
                    mouse_c = 0
                    set_neko()
                    neko[cursor_y][cursor_x] = tsugi #풍선 안에 고냉이 얼굴
                    tsugi = 0
                    index = 2
                    tsugi_time = timeCounter

        if timeCounter - tsugi_time >= 50 and tsugi > 0:  # 5초 경과 + tsugi블럭 있을 때
        #가장 아래 빈 곳 찾기
            for y in range(11, -1, -1):
                if neko[y][cursor_x] == 0:
                    neko[y][cursor_x] = tsugi
                    tsugi = 0
                    index = 2
                    tsugi_time = timeCounter #시간 갱신
                    break

        cvs.delete("CURSOR")
        cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR")
        draw_neko()

    if index in [2, 3, 4, 5]:  #타이머_ 게임 플레이 중일 때의 인덱스
        timeCounter += 1


    elif index == 6:  # 게임 오버
        timer = timer + 1
        if timer == 1:
            draw_txt("GAME OVER", 380, 415, 60, "red", "OVER")

        if timer == 50:
            cvs.delete("OVER")
            index = 0
            timeCounter = 0 #타이머 리셋

    cvs.delete("INFO")
    draw_txt("SCORE " + str(score), 226, 58, 32, "blue", "INFO")
    draw_txt("HISC " + str(highScore), 516, 58, 32, "yellow", "INFO")
    draw_txt("TIMER " + str(timeCounter//10), 900, 58, 32, "pink", "INFO")
    
    if tsugi > 0:
        cvs.create_image(886, 265, image=img_neko[tsugi], tag="INFO")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("블록 낙하 퍼즐 '야옹야옹'")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
cvs = tkinter.Canvas(root, width=1044, height=896)
cvs.pack()

bg = tkinter.PhotoImage(file="C:/Users/my/Desktop/cemester/aa/python/library/neko_bg_modify.png")
cursor = tkinter.PhotoImage(file="C:/Users/my/Desktop/cemester/aa/python/library/neko_cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="C:/Users/my/Desktop/cemester/aa/python/library/neko1.png"),
    tkinter.PhotoImage(file="C:/Users/my/Desktop/cemester/aa/python/library/neko2.png"),
    tkinter.PhotoImage(file="C:/Users/my/Desktop/cemester/aa/python/library/neko3.png"),
    tkinter.PhotoImage(file="C:/Users/my/Desktop/cemester/aa/python/library/neko4.png"),
    tkinter.PhotoImage(file="C:/Users/my/Desktop/cemester/aa/python/library/neko5.png"),
    tkinter.PhotoImage(file="C:/Users/my/Desktop/cemester/aa/python/library/neko6.png"),
    tkinter.PhotoImage(file="C:/Users/my/Desktop/cemester/aa/python/library/neko_niku.png")
]

cvs.create_image(522,448, image=bg)
game_main()

root.bind("<Escape>", esc_press) #esc키 바인드
root.mainloop()
