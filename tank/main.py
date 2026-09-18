import pygame, sys, random
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
W,H=420,460; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("坦克大战")
clock=pygame.time.Clock(); font=pygame.font.Font(_FN,26)
px=W//2; bullets=[]; foes=[]; score=0
def draw():
    screen.fill((30,40,30))
    pygame.draw.rect(screen,(120,200,120),(px-14,H-40,28,28))
    for b in bullets: pygame.draw.rect(screen,(255,230,80),(b[0]-2,b[1]-6,4,8))
    for f in foes: pygame.draw.rect(screen,(220,80,80),(f[0]-13,f[1]-13,26,26))
    screen.blit(font.render("分数:%d 左右移动 空格射击"%score,True,(255,255,255)),(5,H-26))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE: bullets.append([px,H-40])
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: px-=5
    if keys[pygame.K_RIGHT]: px+=5
    px=max(14,min(W-14,px))
    bullets=[(x,y-7) for x,y in bullets if y>0]
    if random.random()<0.03: foes.append([random.randint(20,W-20),-20])
    foes=[(x,y+2) for x,y in foes if y<H]
    for b in bullets:
        for f in foes:
            if abs(b[0]-f[0])<16 and abs(b[1]-f[1])<16: f[1]=H+99; score+=1
    foes=[f for f in foes if f[1]<=H]
    draw(); clock.tick(40)
pygame.quit()
