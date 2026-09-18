import pygame, sys, random
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
W,H=400,460; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("弹球")
clock=pygame.time.Clock()
p1=pygame.Rect(15,H//2-30,10,60); p2=pygame.Rect(W-25,H//2-30,10,60)
ball=pygame.Rect(W//2,H//2,10,10); bvx,bvy=4,4; s1=s2=0
font=pygame.font.Font(_FN,26)
def draw():
    screen.fill((20,22,40))
    pygame.draw.rect(screen,(255,255,255),p1); pygame.draw.rect(screen,(255,255,255),p2)
    pygame.draw.rect(screen,(255,210,63),ball)
    screen.blit(font.render("%d : %d"%(s1,s2),True,(200,200,255)),(W//2-20,10))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN:
            if e.key==pygame.K_w: p1.y-=20
            elif e.key==pygame.K_s: p1.y+=20
    if ball.y<0 or ball.y>H: bvy=-bvy
    ball.x+=bvx; ball.y+=bvy
    if ball.colliderect(p1): bvx=abs(bvx)
    if ball.colliderect(p2): bvx=-abs(bvx)
    p2.y=ball.y-30
    if ball.left<0: s2+=1; ball.x=W//2; ball.y=H//2; bvx=4
    if ball.right>W: s1+=1; ball.x=W//2; ball.y=H//2; bvx=-4
    draw(); clock.tick(60)
pygame.quit()
