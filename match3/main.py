import pygame, sys, random
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
N=8; CELL=50; W=N*CELL; H=N*CELL+30
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("消消乐")
font=pygame.font.Font(_FN,30)
cols=[(230,80,80),(80,200,120),(80,150,230),(240,210,80),(200,120,220),(90,210,210)]
g=[[random.randint(0,5) for _ in range(N)] for _ in range(N)]
sel=None; score=0
def draw():
    screen.fill((30,30,50))
    for r in range(N):
        for c in range(N):
            pygame.draw.rect(screen,cols[g[r][c]],(c*CELL+2,r*CELL+2,CELL-4,CELL-4))
            if sel==(r,c): pygame.draw.rect(screen,(255,255,255),(c*CELL+2,r*CELL+2,CELL-4,CELL-4),3)
    screen.blit(font.render("分数:%d  点两格交换"%score,True,(255,255,255)),(5,H-26))
    pygame.display.flip()
def matches():
    s=set()
    for r in range(N):
        for c in range(N-2):
            if g[r][c]==g[r][c+1]==g[r][c+2]: s|={(r,c),(r,c+1),(r,c+2)}
    for c in range(N):
        for r in range(N-2):
            if g[r][c]==g[r+1][c]==g[r+2][c]: s|={(r,c),(r+1,c),(r+2,c)}
    return s
def gravity():
    for c in range(N):
        col=[g[r][c] for r in range(N) if g[r][c]>=0]
        while len(col)<N: col.insert(0,-1)
        for r in range(N): g[r][c]=col[r]
draw(); running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            x,y=e.pos
            if y<H-30:
                c,r=x//CELL,y//CELL
                if sel is None: sel=(r,c)
                else:
                    if abs(sel[0]-r)+abs(sel[1]-c)==1:
                        g[sel[0]][sel[1]],g[r][c]=g[r][c],g[sel[0]][sel[1]]
                        m=matches()
                        if m:
                            for (rr,cc) in m: g[rr][cc]=-1; score+=len(m)
                            gravity()
                            while matches():
                                m2=matches()
                                for (rr,cc) in m2: g[rr][cc]=-1; score+=len(m2)
                                gravity()
                        else:
                            g[sel[0]][sel[1]],g[r][c]=g[r][c],g[sel[0]][sel[1]]
                    sel=None
    draw()
pygame.quit()
