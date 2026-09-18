import pygame, sys
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
COLS=ROWS=4; CELL=80; W=COLS*CELL; H=ROWS*CELL+30
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("华容道")
font=pygame.font.Font(_FN,24)
blocks=[(0,0,2,2,(200,120,80)),(0,2,1,2,(120,160,220)),(0,3,1,2,(120,160,220)),
        (2,0,2,1,(120,200,120)),(2,1,2,1,(120,200,120)),
        (2,3,1,1,(230,220,80)),(3,0,1,1,(230,220,80)),(3,1,1,1,(230,220,80)),(3,2,1,1,(230,220,80)),(3,3,1,1,(230,220,80))]
occ=[[0]*COLS for _ in range(ROWS)]
for i,(r,c,w,h,col) in enumerate(blocks):
    for rr in range(r,r+h):
        for cc in range(c,c+w): occ[rr][cc]=i+1
def draw():
    screen.fill((40,40,60))
    for i,(r,c,w,h,col) in enumerate(blocks):
        pygame.draw.rect(screen,col,(c*CELL+2,r*CELL+2,w*CELL-4,h*CELL-4))
    pygame.draw.rect(screen,(255,255,255),(COLS*CELL//2-CELL,ROWS*CELL-CELL*2,CELL,CELL*2),2)
    screen.blit(font.render("拖动方块 把大块移到底部出口",True,(255,255,255)),(5,H-26))
    pygame.display.flip()
def block_at(x,y):
    c=x//CELL; r=y//CELL
    if 0<=r<ROWS and 0<=c<COLS: return occ[r][c]-1
    return -1
drag=None; ox=oy=0
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            i=block_at(*e.pos)
            if i>=0: drag=i; ox=e.pos[0]-blocks[i][1]*CELL; oy=e.pos[1]-blocks[i][0]*CELL
        elif e.type==pygame.MOUSEMOTION and drag is not None:
            nc=(e.pos[0]-ox)//CELL; nr=(e.pos[1]-oy)//CELL
            r,c,w,h,col=blocks[drag]
            if 0<=nr and nr+h<=ROWS and 0<=nc and nc+w<=COLS:
                free=True
                for rr in range(ROWS):
                    for cc in range(COLS):
                        if occ[rr][cc]==drag+1: continue
                        if nr<=rr<nr+h and nc<=cc<nc+w: free=False
                if free:
                    for rr in range(r,r+h):
                        for cc in range(c,c+w): occ[rr][cc]=0
                    blocks[drag]=(nr,nc,w,h,col)
                    for rr in range(nr,nr+h):
                        for cc in range(nc,nc+w): occ[rr][cc]=drag+1
        elif e.type==pygame.MOUSEBUTTONUP: drag=None
    draw()
pygame.quit()
