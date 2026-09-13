import pygame, sys, random
pygame.init()
W,H=480,300; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("小恐龙")
clock=pygame.time.Clock(); font=pygame.font.SysFont(None,26)
px,py=60,H-60; vy=0; ground=H-60; obs=[]; score=0; spd=4
def draw():
    screen.fill((240,240,245))
    pygame.draw.rect(screen,(60,200,120),(px-12,py-24,24,24))
    for o in obs: pygame.draw.rect(screen,(120,90,60),(o[0],ground-30,18,30))
    screen.blit(font.render("分数:%d  空格跳"%score,True,(20,20,40)),(5,5))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE and py>=ground: vy=-12
    vy+=0.8; py+=int(vy)
    if py>=ground: py=ground; vy=0
    if random.random()<0.02: obs.append([W,0])
    obs=[(x-spd,y) for x,y in obs if x>-30]
    for o in obs:
        if abs(o[0]-px)<18 and abs((ground-15)-py)<24:
            screen.fill((240,240,245)); screen.blit(font.render("结束 分数:%d 按R"%score,True,(200,0,0)),(W//2-80,H//2)); pygame.display.flip()
            wait=True
            while wait:
                for ev in pygame.event.get():
                    if ev.type==pygame.QUIT: wait=False; running=False
                    elif ev.type==pygame.KEYDOWN and ev.key==pygame.K_r: wait=False; obs=[]; score=0
    score+=1
    draw(); clock.tick(40)
pygame.quit()
