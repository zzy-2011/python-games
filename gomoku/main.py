import pygame, sys
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
N=15; CELL=32; W=N*CELL; H=N*CELL+30
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("五子棋")
font=pygame.font.Font(_FN,24)
b=[[0]*N for _ in range(N)]; turn=1; msg=""
def draw():
    screen.fill((210,170,110))
    for i in range(N):
        pygame.draw.line(screen,(0,0,0),(0,i*CELL),(W,i*CELL)); pygame.draw.line(screen,(0,0,0),(i*CELL,0),(i*CELL,H-30))
    for r in range(N):
        for c in range(N):
            if b[r][c]: pygame.draw.circle(screen,(20,20,20) if b[r][c]==1 else (230,230,230),(c*CELL+CELL//2,r*CELL+CELL//2),CELL//2-2)
    screen.blit(font.render(msg,True,(0,0,0)),(5,H-26))
    pygame.display.flip()
def win(r,c,p):
    for dr,dc in [(1,0),(0,1),(1,1),(1,-1)]:
        cnt=1; nr,nc=r+dr,c+dc
        while 0<=nr<N and 0<=nc<N and b[nr][nc]==p: cnt+=1; nr+=dr; nc+=dc
        nr,nc=r-dr,c-dc
        while 0<=nr<N and 0<=nc<N and b[nr][nc]==p: cnt+=1; nr-=dr; nc-=dc
        if cnt>=5: return True
    return False
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            x,y=e.pos
            if y<H-30:
                c,r=x//CELL,y//CELL
                if 0<=r<N and 0<=c<N and b[r][c]==0:
                    b[r][c]=turn
                    if win(r,c,turn): msg=("黑" if turn==1 else "白")+"棋胜利! 按R重开"; turn=0
                    else: turn=3-turn
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_r:
            b=[[0]*N for _ in range(N)]; turn=1; msg=""
    draw()
pygame.quit()
