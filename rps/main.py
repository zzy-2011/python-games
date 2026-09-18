import pygame, sys, random
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
W,H=420,320
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("石头剪刀布")
font=pygame.font.Font(_FN,30)
opts=["石头","剪刀","布"]; you=0; cpu=0; dr=0; msg="按 1/2/3 出拳"
def draw():
    screen.fill((20,22,40))
    screen.blit(font.render(msg,True,(255,210,63)),(20,30))
    screen.blit(font.render("你:%d  电脑:%d  平:%d"%(you,cpu,dr),True,(120,200,255)),(20,80))
    screen.blit(font.render("1石头 2剪刀 3布",True,(150,150,200)),(20,260))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN and e.key in (pygame.K_1,pygame.K_2,pygame.K_3):
            y=e.key-pygame.K_1; c=random.randint(0,2)
            if y==c: dr+=1; msg="你%s 电脑%s 平"%(opts[y],opts[c])
            elif (y-c)%3==1: you+=1; msg="你%s 电脑%s 你赢"%(opts[y],opts[c])
            else: cpu+=1; msg="你%s 电脑%s 你输"%(opts[y],opts[c])
    draw()
pygame.quit()
