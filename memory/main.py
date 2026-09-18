import pygame, sys, random
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
COLS=ROWS=4; CELL=80; W=COLS*CELL; H=ROWS*CELL+30
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("记忆翻牌")
font=pygame.font.Font(_FN,40)
syms=list("AABBCCDDEEFFGGHH"); random.shuffle(syms)
cards=[[syms[r*COLS+c] for c in range(COLS)] for r in range(ROWS)]
flipped=[[False]*COLS for _ in range(ROWS)]; open1=None; open2=None; pairs=0; lock=0
def draw():
    screen.fill((30,30,50))
    for r in range(ROWS):
        for c in range(COLS):
            f=flipped[r][c] or (open1==(r,c)) or (open2==(r,c))
            pygame.draw.rect(screen,(200,200,220) if f else (70,70,120),(c*CELL+4,r*CELL+4,CELL-8,CELL-8))
            if f: screen.blit(font.render(cards[r][c],True,(20,20,60)),(c*CELL+CELL//2-12,r*CELL+CELL//2-20))
    screen.blit(font.render("配对:%d/%d"%(pairs,COLS*ROWS//2),True,(255,255,255)),(5,H-26))
    pygame.display.flip()
draw(); running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.MOUSEBUTTONDOWN and lock==0:
            x,y=e.pos
            if y<H-30:
                c,r=x//CELL,y//CELL
                if 0<=r<ROWS and 0<=c<COLS and not flipped[r][c] and (r,c)!=open1:
                    if open1 is None: open1=(r,c)
                    elif open2 is None:
                        open2=(r,c); lock=1
                        if cards[open1[0]][open1[1]]==cards[open2[0]][open2[1]]:
                            flipped[open1[0]][open1[1]]=flipped[open2[0]][open2[1]]=True; pairs+=1; open1=open2=None; lock=0
                        else:
                            pygame.time.delay(500); open1=open2=None; lock=0
    draw()
pygame.quit()
