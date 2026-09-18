import pygame, sys, random
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
W,H=400,300
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("猜数字")
font=pygame.font.Font(_FN,30)
target=random.randint(1,100); guess=""; msg="我想了一个 1-100 的数，猜猜看"
def draw():
    screen.fill((20,22,40))
    screen.blit(font.render(msg,True,(255,210,63)),(20,40))
    screen.blit(font.render("输入: "+guess,True,(120,200,255)),(20,100))
    screen.blit(font.render("Enter 提交  Esc 重开",True,(150,150,200)),(20,250))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE: target=random.randint(1,100); guess=""; msg="新的一局，猜吧"
            elif e.key==pygame.K_RETURN:
                if guess.isdigit():
                    g=int(guess)
                    if g==target: msg="猜对了！就是 %d"%g
                    elif g<target: msg="%d 小了"%g
                    else: msg="%d 大了"%g
                    guess=""
            elif e.key==pygame.K_BACKSPACE: guess=guess[:-1]
            elif e.unicode.isdigit(): guess+=e.unicode
    draw()
pygame.quit()
