import pygame, sys, random
pygame.init()
W,H=400,460; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("打砖块")
clock=pygame.time.Clock()
pad=pygame.Rect(W//2-35,H-30,70,10)
ball=pygame.Rect(W//2,H-50,10,10); bvx,bvy=4,-4
bricks=[pygame.Rect(c*40+5,r*20+5,34,16) for r in range(6) for c in range(9)]
def draw():
    screen.fill((20,22,40))
    for b in bricks: pygame.draw.rect(screen,(90,160,255),b)
    pygame.draw.rect(screen,(255,255,255),pad)
    pygame.draw.rect(screen,(255,210,63),ball)
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.MOUSEMOTION: pad.centerx=e.pos[0]
    ball.x+=bvx; ball.y+=bvy
    if ball.left<0 or ball.right>W: bvx=-bvx
    if ball.top<0: bvy=-bvy
    if pad.left<ball.centerx<pad.right and ball.bottom>=pad.top and ball.bottom<=pad.top+12: bvy=-bvy
    hit=[i for i,b in enumerate(bricks) if b.colliderect(ball)]
    for i in hit: bricks.pop(i); bvy=-bvy
    if ball.top>H: ball.x=W//2; ball.y=H-50; bvx,bvy=4,-4
    draw(); clock.tick(60)
pygame.quit()
