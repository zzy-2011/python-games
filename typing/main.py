import pygame, sys, random, time
pygame.init()
W,H=480,260
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("打字练习")
font=pygame.font.SysFont(None,34)
WORDS=["python","game","happy","world","code","play","speed","typing","keyboard","fun"]
target=random.choice(WORDS); typed=""; start=time.time(); msg="照着打下面的词"
def draw():
    screen.fill((20,22,40))
    screen.blit(font.render(target,True,(255,210,63)),(20,40))
    screen.blit(font.render(typed,True,(120,200,255)),(20,110))
    screen.blit(font.render(msg,True,(150,150,200)),(20,200))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN:
            if e.key==pygame.K_RETURN:
                if typed==target:
                    t=time.time()-start; wpm=int(len(target)/max(t,0.1)/5*60)
                    msg="完成! %d 字/分"%wpm; target=random.choice(WORDS); typed=""; start=time.time()
                else: msg="不对，重打"
            elif e.key==pygame.K_BACKSPACE: typed=typed[:-1]
            elif e.unicode.isalpha(): typed+=e.unicode
    draw()
pygame.quit()
