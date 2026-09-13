import pygame, sys, random
pygame.init()
N=9; CELL=40; W=N*CELL; H=N*CELL+40
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("数独")
font=pygame.font.SysFont(None,30)
def ok(b,r,c,v):
    for i in range(N):
        if b[r][i]==v or b[i][c]==v: return False
    br,bc=3*(r//3),3*(c//3)
    for i in range(br,br+3):
        for j in range(bc,bc+3):
            if b[i][j]==v: return False
    return True
def solve(b):
    for r in range(N):
        for c in range(N):
            if b[r][c]==0:
                for v in range(1,10):
                    if ok(b,r,c,v):
                        b[r][c]=v
                        if solve(b): return True
                        b[r][c]=0
                return False
    return True
board=[[0]*9 for _ in range(9)]; solve(board)
puzzle=[row[:] for row in board]
for r in range(9):
    for c in range(9):
        if random.random()<0.55: puzzle[r][c]=0
sel=None
def draw():
    screen.fill((240,240,250))
    for r in range(9):
        for c in range(9):
            col=(255,255,255) if (r//3+c//3)%2==0 else (220,225,245)
            pygame.draw.rect(screen,col,(c*CELL,r*CELL,CELL,CELL))
            if puzzle[r][c]: screen.blit(font.render(str(puzzle[r][c]),True,(20,20,40)),(c*CELL+13,r*CELL+8))
    for i in range(10):
        pygame.draw.line(screen,(120,120,140),(0,i*CELL),(W,i*CELL),1 if i%3 else 3)
        pygame.draw.line(screen,(120,120,140),(i*CELL,0),(i*CELL,H-40),1 if i%3 else 3)
    screen.blit(font.render("点格子 + 数字键 1-9 填数",True,(20,20,40)),(5,H-32))
    pygame.display.flip()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            x,y=e.pos
            if y<H-40: sel=(y//CELL,x//CELL)
        elif e.type==pygame.KEYDOWN and sel and pygame.K_1<=e.key<=pygame.K_9:
            if puzzle[sel[0]][sel[1]]==0 or True: puzzle[sel[0]][sel[1]]=e.key-pygame.K_0
    draw()
pygame.quit()
