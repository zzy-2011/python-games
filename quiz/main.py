import pygame, sys, random
pygame.init()
W,H=460,340
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("知识问答")
font=pygame.font.SysFont(None,26)
QA=[("中国首都是？",["上海","北京","广州"],1),("1+1=",["1","2","3"],1),
    ("水的化学式？",["H2O","CO2","O2"],0),("一年有几个月？",["10","12","11"],1),
    ("太阳从哪边升起？",["东","西","南"],0)]
q=0; score=0; msg=""
def draw():
    screen.fill((20,22,40))
    screen.blit(font.render(QA[q][0],True,(255,210,63)),(20,30))
    for i,opt in enumerate(QA[q][1]):
        screen.blit(font.render("%d. %s"%(i+1,opt),True,(120,200,255)),(20,80+i*40))
    screen.blit(font.render("得分:%d/%d  %s"%(score,len(QA),msg),True,(150,220,150)),(20,300))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN and e.key in (pygame.K_1,pygame.K_2,pygame.K_3):
            if e.key-pygame.K_1==QA[q][2]: score+=1; msg="对!"
            else: msg="错"
            q+=1
            if q>=len(QA): q=0; msg="回合结束，重来"; score=0
    draw()
pygame.quit()
