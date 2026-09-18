import pygame, sys, random
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
N=8; CELL=56; W=N*CELL; H=N*CELL+30
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("黑白棋")
font=pygame.font.Font(_FN,24)
b=[[0]*N for _ in range(N)]; b[3][3]=b[4][4]=2; b[3][4]=b[4][3]=1
def draw():
    screen.fill((0,120,0))
    for i in range(N):
        pygame.draw.line(screen,(0,0,0),(0,i*CELL),(W,i*CELL)); pygame.draw.line(screen,(0,0,0),(i*CELL,0),(i*CELL,H-30))
    for r in range(N):
        for c in range(N):
            if b[r][c]: pygame.draw.circle(screen,(20,20,20) if b[r][c]==1 else (240,240,240),(c*CELL+CELL//2,r*CELL+CELL//2),CELL//2-3)
    screen.blit(font.render("黑:%d 白:%d"%(sum(r.count(1) for r in b),sum(r.count(2) for r in b)),True,(255,255,255)),(5,H-26))
    pygame.display.flip()
def flips(r,c,p):
    if b[r][c]: return []
    res=[]
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
        line=[]; nr,nc=r+dr,c+dc
        while 0<=nr<N and 0<=nc<N and b[nr][nc]==3-p: line.append((nr,nc)); nr+=dr; nc+=dc
        if 0<=nr<N and 0<=nc<N and b[nr][nc]==p and line: res+=line
    return res
def legal(p): return [(r,c) for r in range(N) for c in range(N) if flips(r,c,p)]
def ai():
    mv=legal(2)
    if mv:
        r,c=random.choice(mv); b[r][c]=2
        for f in flips(r,c,2): b[f]=2
draw(); running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            x,y=e.pos
            if y<H-30:
                c,r=x//CELL,y//CELL
                if 0<=r<N and 0<=c<N:
                    fl=flips(r,c,1)
                    if fl:
                        b[r][c]=1
                        for f in fl: b[f]=1
                        ai()
    draw()
pygame.quit()
