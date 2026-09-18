import pygame, sys, random
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
N=3; CELL=120; W=N*CELL; H=N*CELL+40
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("井字棋")
font=pygame.font.Font(_FN,60)
b=[[0]*3 for _ in range(3)]; turn=1; msg=""
def draw():
    screen.fill((230,230,240))
    for r in range(3):
        for c in range(3):
            pygame.draw.rect(screen,(255,255,255),(c*CELL+4,r*CELL+4,CELL-8,CELL-8))
            v=b[r][c]
            if v: screen.blit(font.render("X" if v==1 else "O",True,(200,60,60) if v==1 else (60,60,200)),(c*CELL+CELL//2-18,r*CELL+CELL//2-30))
    screen.blit(font.render(msg,True,(20,20,40)),(10,H-32))
    pygame.display.flip()
def win(p):
    for i in range(3):
        if all(b[i][j]==p for j in range(3)) or all(b[j][i]==p for j in range(3)): return True
    if all(b[i][i]==p for i in range(3)) or all(b[i][2-i]==p for i in range(3)): return True
    return False
def ai():
    empt=[(r,c) for r in range(3) for c in range(3) if b[r][c]==0]
    if empt: r,c=random.choice(empt); b[r][c]=2
draw(); running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.MOUSEBUTTONDOWN and turn==1:
            x,y=e.pos
            if y<H-40:
                c,r=x//CELL,y//CELL
                if 0<=r<3 and 0<=c<3 and b[r][c]==0:
                    b[r][c]=1
                    if win(1): msg="你赢了! 按R重开"; turn=0
                    elif all(b[i][j] for i in range(3) for j in range(3)): msg="平局 按R"; turn=0
                    else:
                        ai()
                        if win(2): msg="电脑赢了 按R"; turn=0
                        elif all(b[i][j] for i in range(3) for j in range(3)): msg="平局 按R"
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_r:
            b=[[0]*3 for _ in range(3)]; turn=1; msg=""
    draw()
pygame.quit()
