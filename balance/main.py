import pygame, sys
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
W,H=480,300; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("平衡球")
clock=pygame.time.Clock(); font=pygame.font.Font(_FN,26)
bx=W//2; vx=0; score=0
def draw():
    screen.fill((30,30,50))
    pygame.draw.line(screen,(200,200,200),(40,H-80),(W-40,H-80),6)
    pygame.draw.circle(screen,(230,120,80),(int(bx),H-92),12)
    screen.blit(font.render("分数:%d  方向键倾斜"%score,True,(255,255,255)),(5,5))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
    keys=pygame.key.get_pressed()
    a=0
    if keys[pygame.K_LEFT]: a=-0.3
    if keys[pygame.K_RIGHT]: a=0.3
    vx+=a; vx*=0.98; bx+=vx
    if bx<40 or bx>W-40:
        screen.blit(font.render("掉落! 分数:%d 按R"%score,True,(255,80,80)),(W//2-80,H//2)); pygame.display.flip()
        wait=True
        while wait:
            for ev in pygame.event.get():
                if ev.type==pygame.QUIT: wait=False; running=False
                elif ev.type==pygame.KEYDOWN and ev.key==pygame.K_r: wait=False; bx=W//2; vx=0; score=0
    score+=1
    draw(); clock.tick(40)
pygame.quit()
