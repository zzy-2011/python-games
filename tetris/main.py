import pygame, sys, random
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
COLS,ROWS=10,20; CELL=24; W=COLS*CELL; H=ROWS*CELL+30
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("俄罗斯方块")
font=pygame.font.Font(_FN,24)
SHAPES=[[[1,1,1,1]],[[1,1],[1,1]],[[1,1,1],[0,1,0]],[[1,1,1],[1,0,0]],[[1,1,1],[0,0,1]],[[0,1,1],[1,1,0]],[[1,1,0],[0,1,1]]]
board=[[0]*COLS for _ in range(ROWS)]
cur=None; cx=0; cy=0; score=0
def newp():
    global cur,cx,cy
    cur=random.choice(SHAPES); cx=COLS//2-1; cy=0
def collide():
    for r in range(len(cur)):
        for c in range(len(cur[0])):
            if cur[r][c]:
                nr=cy+r; nc=cx+c
                if nr>=ROWS or nc<0 or nc>=COLS or (nr>=0 and board[nr][nc]): return True
    return False
def merge():
    for r in range(len(cur)):
        for c in range(len(cur[0])):
            if cur[r][c]: board[cy+r][cx+c]=1
def clear():
    global score
    full=[r for r in range(ROWS) if all(board[r])]
    for r in full:
        del board[r]; board.insert(0,[0]*COLS); score+=10
def draw():
    screen.fill((20,22,40))
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c]: pygame.draw.rect(screen,(80,200,120),(c*CELL,r*CELL,CELL-1,CELL-1))
    if cur:
        for r in range(len(cur)):
            for c in range(len(cur[0])):
                if cur[r][c]: pygame.draw.rect(screen,(230,120,80),((cx+c)*CELL,(cy+r)*CELL,CELL-1,CELL-1))
    screen.blit(font.render("分数:%d 方向键移动/旋转 空格速降"%score,True,(255,255,255)),(5,H-26))
    pygame.display.flip()
newp(); draw(); clock=pygame.time.Clock(); fall=0
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN:
            if e.key==pygame.K_LEFT:
                cx-=1
                if cx<0 or collide(): cx+=1
            elif e.key==pygame.K_RIGHT:
                cx+=1
                if cx>=COLS or collide(): cx-=1
            elif e.key==pygame.K_DOWN:
                cy+=1
                if collide(): cy-=1
            elif e.key==pygame.K_UP:
                cur=list(zip(*cur[::-1]))
                if collide(): cur=list(zip(*cur[::-1]))
            elif e.key==pygame.K_SPACE:
                while not collide(): cy+=1
                cy-=1; merge(); clear(); newp()
    fall+=1
    if fall>=8:
        fall=0; cy+=1
        if collide():
            cy-=1; merge(); clear(); newp()
            if collide():
                screen.fill((20,22,40)); screen.blit(font.render("结束 分数:%d 按R"%score,True,(255,80,80)),(W//2-80,H//2)); pygame.display.flip()
                wait=True
                while wait:
                    for ev in pygame.event.get():
                        if ev.type==pygame.QUIT: wait=False; running=False
                        elif ev.type==pygame.KEYDOWN and ev.key==pygame.K_r: wait=False; board=[[0]*COLS for _ in range(ROWS)]; score=0; newp()
    draw(); clock.tick(20)
pygame.quit()
