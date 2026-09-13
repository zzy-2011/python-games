import pygame, sys, random
pygame.init()
W,H=400,500; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("飞机大战")
clock=pygame.time.Clock(); font=pygame.font.SysFont(None,26)
px,py=W//2,H-60; bullets=[]; foes=[]; score=0
def draw():
    screen.fill((10,12,30))
    pygame.draw.rect(screen,(80,200,255),(px-15,py-15,30,30))
    for b in bullets: pygame.draw.rect(screen,(255,230,80),(b[0]-2,b[1]-8,4,10))
    for f in foes: pygame.draw.rect(screen,(255,90,90),(f[0]-12,f[1]-12,24,24))
    screen.blit(font.render("分数:%d  方向键移动 空格射击"%score,True,(255,255,255)),(5,H-26))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE: bullets.append([px,py])
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: px-=5
    if keys[pygame.K_RIGHT]: px+=5
    if keys[pygame.K_UP]: py-=5
    if keys[pygame.K_DOWN]: py+=5
    px=max(15,min(W-15,px)); py=max(15,min(H-15,py))
    bullets=[(x,y-8) for x,y in bullets if y>0]
    if random.random()<0.03: foes.append([random.randint(20,W-20),-20])
    foes=[(x,y+3) for x,y in foes if y<H]
    for b in bullets:
        for f in foes:
            if abs(b[0]-f[0])<16 and abs(b[1]-f[1])<16: f[1]=H+99; score+=1
    foes=[f for f in foes if f[1]<=H]
    draw(); clock.tick(40)
pygame.quit()
