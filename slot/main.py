import pygame, sys, random
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
W,H=360,260; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("老虎机")
font=pygame.font.Font(_FN,40); font2=pygame.font.Font(_FN,28)
syms=["7","CHERRY","LEMON","BELL","STAR"]
reels=[0,0,0]; coins=100; msg="空格 拉霸"
def draw():
    screen.fill((30,20,40))
    for i in range(3):
        pygame.draw.rect(screen,(240,240,250),(i*110+20,H//2-40,90,80))
        screen.blit(font.render(syms[reels[i]],True,(20,20,60)),(i*110+28,H//2-30))
    screen.blit(font2.render("金币:%d"%coins,True,(255,220,80)),(20,20))
    screen.blit(font2.render(msg,True,(255,255,255)),(20,H-40))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            if coins>0:
                coins-=1; reels=[random.randint(0,4) for _ in range(3)]
                if reels[0]==reels[1]==reels[2]: coins+=20; msg="中奖! +20"
                elif reels[0]==reels[1] or reels[1]==reels[2] or reels[0]==reels[2]: coins+=2; msg="小奖 +2"
                else: msg="再来"
    draw()
pygame.quit()
