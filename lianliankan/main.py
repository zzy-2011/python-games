import pygame, sys, random
from collections import deque
pygame.init()
COLS,ROWS=10; CELL=40; W=COLS*CELL; H=ROWS*CELL+30
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("连连看")
font=pygame.font.SysFont(None,26)
g=[[0]*(COLS+2) for _ in range(ROWS+2)]
syms=[]
for i in range(COLS*ROWS//2): syms+=[i+1,i+1]
random.shuffle(syms)
k=0
for r in range(1,ROWS+1):
    for c in range(1,COLS+1):
        g[r][c]=syms[k]; k+=1
sel=None; cleared=0
def draw():
    screen.fill((30,30,50))
    for r in range(1,ROWS+1):
        for c in range(1,COLS+1):
            if g[r][c]:
                pygame.draw.rect(screen,(80,120,200),(c*CELL,r*CELL,CELL-2,CELL-2))
                screen.blit(font.render(str(g[r][c]),True,(255,255,255)),(c*CELL+12,r*CELL+8))
    screen.blit(font.render("已消除:%d/%d"%(cleared,COLS*ROWS),True,(255,255,255)),(5,H-26))
    pygame.display.flip()
def canlink(a,b):
    sr,sc=a; tr,tc=b
    if g[sr][sc]!=g[tr][tc] or (sr,sc)==(tr,tc): return False
    q=deque([(sr,sc,-1,0)]); best={}
    while q:
        r,c,pd,t=q.popleft()
        for nd,(dr,dc) in enumerate([(1,0),(-1,0),(0,1),(0,-1)]):
            nr,nc=r+dr,c+dc
            if not(0<=nr<ROWS+2 and 0<=nc<COLS+2): continue
            nt=t+(0 if pd==-1 else (0 if nd==pd else 1))
            if nt>2: continue
            if (nr,nc)==(tr,tc): return True
            if g[nr][nc]!=0: continue
            key=(nr,nc,nd)
            if key in best and best[key]<=nt: continue
            best[key]=nt; q.append((nr,nc,nd,nt))
    return False
draw(); running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            x,y=e.pos
            if y<H-30:
                c,r=x//CELL,y//CELL
                if 1<=r<=ROWS and 1<=c<=COLS and g[r][c]:
                    if sel is None: sel=(r,c)
                    else:
                        if g[sel]==g[r][c] and canlink(sel,(r,c)):
                            g[sel[0]][sel[1]]=0; g[r][c]=0; cleared+=2; sel=None
                        else: sel=(r,c)
    draw()
pygame.quit()
