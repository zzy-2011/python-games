import pygame, sys, random
pygame.init()
N=3; CELL=100; W=N*CELL; H=N*CELL+30
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("数字拼图")
font=pygame.font.SysFont(None,50); font2=pygame.font.SysFont(None,24)
tiles=list(range(1,9))+[0]; random.shuffle(tiles)
grid=[tiles[r*N:(r+1)*N] for r in range(N)]
def draw():
    screen.fill((40,40,60))
    for r in range(N):
        for c in range(N):
            v=grid[r][c]
            if v: pygame.draw.rect(screen,(120,160,220),(c*CELL+4,r*CELL+4,CELL-8,CELL-8)); screen.blit(font.render(str(v),True,(255,255,255)),(c*CELL+CELL//2-15,r*CELL+CELL//2-25))
    screen.blit(font2.render("点空格旁的块移动 R重开",True,(255,255,255)),(5,H-26))
    pygame.display.flip()
def blank(): return [(r,c) for r in range(N) for c in range(N) if grid[r][c]==0][0]
draw(); running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            c,r=e.pos[0]//CELL, e.pos[1]//CELL
            if 0<=r<N and 0<=c<N:
                br,bc=blank()
                if abs(br-r)+abs(bc-c)==1: grid[br][bc],grid[r][c]=grid[r][c],grid[br][bc]
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_r:
            random.shuffle(tiles); grid=[tiles[r*N:(r+1)*N] for r in range(N)]
    draw()
pygame.quit()
