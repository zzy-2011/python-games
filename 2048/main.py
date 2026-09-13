import pygame, sys, random
pygame.init()
N=4; CELL=90; PAD=10; W=N*CELL+PAD*(N+1); H=W+40
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("2048")
font=pygame.font.SysFont(None,40)
board=[[0]*N for _ in range(N)]
def spawn():
    empty=[(r,c) for r in range(N) for c in range(N) if board[r][c]==0]
    if empty: r,c=random.choice(empty); board[r][c]=2 if random.random()<0.9 else 4
def draw():
    screen.fill((60,50,40))
    for r in range(N):
        for c in range(N):
            v=board[r][c]; col=(200,190,170) if v==0 else (237,194,120) if v<32 else (242,160,80)
            pygame.draw.rect(screen,col,(PAD+c*(CELL+PAD),PAD+r*(CELL+PAD),CELL,CELL))
            if v: screen.blit(font.render(str(v),True,(40,30,20)),(PAD+c*(CELL+PAD)+CELL//2-15,PAD+r*(CELL+PAD)+CELL//2-15))
    pygame.display.flip()
def merge(line):
    a=[v for v in line if v]; res=[]; i=0
    while i<len(a):
        if i+1<len(a) and a[i]==a[i+1]: res.append(a[i]*2); i+=2
        else: res.append(a[i]); i+=1
    while len(res)<N: res.append(0)
    return res
def move(dx,dy):
    global board; moved=False
    if dx==0:
        for c in range(N):
            col=[board[r][c] for r in range(N)]
            col=merge(col) if dy==-1 else merge(col[::-1])[::-1]
            for r in range(N):
                if board[r][c]!=col[r]: moved=True
                board[r][c]=col[r]
    else:
        for r in range(N):
            row=[board[r][c] for c in range(N)]
            row=merge(row) if dx==-1 else merge(row[::-1])[::-1]
            for c in range(N):
                if board[r][c]!=row[c]: moved=True
                board[r][c]=row[c]
    if moved: spawn()
spawn(); spawn(); draw()
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN:
            if e.key==pygame.K_LEFT: move(-1,0)
            elif e.key==pygame.K_RIGHT: move(1,0)
            elif e.key==pygame.K_UP: move(0,-1)
            elif e.key==pygame.K_DOWN: move(0,1)
            draw()
    pygame.display.flip()
pygame.quit()
