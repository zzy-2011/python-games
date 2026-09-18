import pygame, sys, random
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
W,H=480,300; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("跳一跳")
clock=pygame.time.Clock(); font=pygame.font.Font(_FN,26)
plat=[(60,200,80),(200,200,80),(340,200,80)]
bx=100; by=plat[0][1]-12; vy=0; on=0; score=0
def draw():
    screen.fill((230,235,245))
    for p in plat: pygame.draw.rect(screen,(120,160,220),(p[0],p[1],p[2],12))
    pygame.draw.circle(screen,(230,120,80),(int(bx),int(by)),12)
    screen.blit(font.render("分数:%d  空格跳"%score,True,(20,20,40)),(5,5))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE and by>=plat[on][1]-12:
            vy=-12; by-=1
    vy+=0.7; by+=int(vy)
    if vy>0:
        landed=False
        for i,p in enumerate(plat):
            if p[0]<=bx<=p[0]+p[2] and by>=p[1]-12 and by<=p[1]+6:
                by=p[1]-12; vy=0; on=i; score+=1; landed=True; break
        if not landed and by>H:
            screen.blit(font.render("结束 按R",True,(200,0,0)),(W//2-40,H//2)); pygame.display.flip()
            wait=True
            while wait:
                for ev in pygame.event.get():
                    if ev.type==pygame.QUIT: wait=False; running=False
                    elif ev.type==pygame.KEYDOWN and ev.key==pygame.K_r: wait=False; bx=100; by=plat[0][1]-12; on=0; score=0
    draw(); clock.tick(40)
pygame.quit()
