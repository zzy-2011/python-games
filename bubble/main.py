import pygame, sys, random, math
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
COLS=ROWS=11; CELL=36; W=COLS*CELL; H=ROWS*CELL+120
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("泡泡龙")
clock=pygame.time.Clock(); font=pygame.font.Font(_FN,24)
cols=[(230,80,80),(80,200,120),(80,150,230),(240,210,80)]
g=[[random.randint(0,3) if r<ROWS-3 else 0 for c in range(COLS)] for r in range(ROWS)]
bx=W//2; by=H-60; ang=math.pi/2; curc=random.randint(0,3); shot=None; score=0
def draw():
    screen.fill((20,22,40))
    for r in range(ROWS):
        for c in range(COLS):
            if g[r][c]: pygame.draw.circle(screen,cols[g[r][c]],(c*CELL+CELL//2,r*CELL+CELL//2),CELL//2-2)
    if shot is None: pygame.draw.circle(screen,cols[curc],(bx,by),CELL//2-2)
    else: pygame.draw.circle(screen,cols[shot[2]],(int(shot[0]),int(shot[1])),CELL//2-2)
    screen.blit(font.render("分数:%d 左右瞄准 空格发射"%score,True,(255,255,255)),(5,H-26))
    pygame.display.flip()
def cluster(r,c,color,seen):
    seen.add((r,c))
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in seen and g[nr][nc]==color: cluster(nr,nc,color,seen)
def checkpop(r,c):
    global score
    seen=set(); cluster(r,c,g[r][c],seen)
    if len(seen)>=3:
        for (rr,cc) in seen: g[rr][cc]=0
        score+=len(seen)
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN:
            if e.key==pygame.K_LEFT: ang=min(math.pi*0.9, ang+0.1)
            elif e.key==pygame.K_RIGHT: ang=max(math.pi*0.1, ang-0.1)
            elif e.key==pygame.K_SPACE and shot is None:
                shot=[bx,by,curc,math.cos(ang)*8,-math.sin(ang)*8]
    if shot:
        shot[0]+=shot[3]; shot[1]+=shot[4]
        if shot[1]<CELL//2:
            c=max(0,min(COLS-1,shot[0]//CELL)); g[0][c]=shot[2]; shot=None; curc=random.randint(0,3); checkpop(0,c)
        else:
            hitc=shot[0]//CELL; hitr=shot[1]//CELL
            if 0<=hitr<ROWS and 0<=hitc<COLS and g[hitr][hitc]:
                r=max(0,hitr-1); c=hitc; g[r][c]=shot[2]; shot=None; curc=random.randint(0,3); checkpop(r,c)
    draw(); clock.tick(60)
pygame.quit()
