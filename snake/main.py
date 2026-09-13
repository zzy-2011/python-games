import pygame, sys, random
pygame.init()
CELL=20; COLS=20; ROWS=20; W=COLS*CELL; H=ROWS*CELL
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("贪吃蛇")
font=pygame.font.SysFont(None,28)
snake=[(COLS//2,ROWS//2)]; dx,dy=1,0
food=(random.randint(0,COLS-1),random.randint(0,ROWS-1)); score=0; clock=pygame.time.Clock()
def draw():
    screen.fill((20,22,40))
    for s in snake: pygame.draw.rect(screen,(80,220,120),(s[0]*CELL,s[1]*CELL,CELL-1,CELL-1))
    pygame.draw.rect(screen,(255,90,90),(food[0]*CELL,food[1]*CELL,CELL-1,CELL-1))
    screen.blit(font.render("分数 %d"%score,True,(255,210,63)),(5,5))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN:
            if e.key==pygame.K_UP and dy==0: dx,dy=0,-1
            elif e.key==pygame.K_DOWN and dy==0: dx,dy=0,1
            elif e.key==pygame.K_LEFT and dx==0: dx,dy=-1,0
            elif e.key==pygame.K_RIGHT and dx==0: dx,dy=1,0
    nx=snake[0][0]+dx; ny=snake[0][1]+dy
    if nx<0 or nx>=COLS or ny<0 or ny>=ROWS or (nx,ny) in snake:
        screen.fill((20,22,40)); screen.blit(font.render("结束 分数 %d  按R重开"%score,True,(255,90,90)),(W//2-110,H//2)); pygame.display.flip()
        wait=True
        while wait:
            for ev in pygame.event.get():
                if ev.type==pygame.QUIT: wait=False; running=False
                elif ev.type==pygame.KEYDOWN and ev.key==pygame.K_r: wait=False; snake=[(COLS//2,ROWS//2)]; dx,dy=1,0; score=0; food=(random.randint(0,COLS-1),random.randint(0,ROWS-1))
        continue
    snake.insert(0,(nx,ny))
    if (nx,ny)==food: score+=1; food=(random.randint(0,COLS-1),random.randint(0,ROWS-1))
    else: snake.pop()
    draw(); clock.tick(8)
pygame.quit()
