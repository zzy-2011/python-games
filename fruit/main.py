import pygame, sys, random
pygame.init()
W,H=400,460; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("接水果")
clock=pygame.time.Clock(); font=pygame.font.SysFont(None,26)
bx=W//2; fruits=[]; score=0
def draw():
    screen.fill((20,30,20))
    pygame.draw.rect(screen,(200,160,80),(bx-25,H-30,50,16))
    for f in fruits: pygame.draw.circle(screen,(230,80,80),(f[0],f[1]),10)
    screen.blit(font.render("分数:%d  方向键移动"%score,True,(255,255,255)),(5,H-26))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: bx-=6
    if keys[pygame.K_RIGHT]: bx+=6
    bx=max(25,min(W-25,bx))
    if random.random()<0.05: fruits.append([random.randint(20,W-20),-10])
    new=[]
    for f in fruits:
        f[1]+=4
        if abs(f[0]-bx)<30 and abs(f[1]-(H-22))<18: score+=1
        elif f[1]<H: new.append(f)
    fruits=new
    draw(); clock.tick(40)
pygame.quit()
