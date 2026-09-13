import pygame, sys, random
pygame.init()
COLS,ROWS=9; CELL=40; W=COLS*CELL; H=ROWS*CELL+30
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("扫雷")
font=pygame.font.SysFont(None,28)
grid=[[{'m':False,'r':False,'f':False,'n':0} for _ in range(COLS)] for _ in range(ROWS)]
mines=set()
while len(mines)<10: mines.add((random.randint(0,ROWS-1),random.randint(0,COLS-1)))
for (r,c) in mines: grid[r][c]['m']=True
for r in range(ROWS):
    for c in range(COLS):
        if not grid[r][c]['m']: grid[r][c]['n']=sum(1 for dr in(-1,0,1) for dc in(-1,0,1) if (r+dr,c+dc) in mines)
def reveal(r,c):
    if 0<=r<ROWS and 0<=c<COLS and not grid[r][c]['r'] and not grid[r][c]['f']:
        grid[r][c]['r']=True
        if grid[r][c]['n']==0 and not grid[r][c]['m']:
            for dr in(-1,0,1):
                for dc in(-1,0,1): reveal(r+dr,c+dc)
def draw():
    screen.fill((180,180,200))
    for r in range(ROWS):
        for c in range(COLS):
            cell=grid[r][c]
            if cell['r']:
                pygame.draw.rect(screen,(220,220,230),(c*CELL,r*CELL,CELL-1,CELL-1))
                if cell['m']: screen.blit(font.render("*",True,(200,0,0)),(c*CELL+14,r*CELL+6))
                elif cell['n']: screen.blit(font.render(str(cell['n']),True,(0,0,200)),(c*CELL+14,r*CELL+6))
            else:
                pygame.draw.rect(screen,(120,120,160),(c*CELL,r*CELL,CELL-1,CELL-1))
                if cell['f']: screen.blit(font.render("F",True,(200,0,0)),(c*CELL+14,r*CELL+6))
    screen.blit(font.render("左键挖 右键插旗 R重开",True,(0,0,0)),(5,H-26))
    pygame.display.flip()
draw(); running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            x,y=e.pos
            if y<H-30:
                c,r=x//CELL,y//CELL
                if 0<=r<ROWS and 0<=c<COLS:
                    if e.button==1: reveal(r,c)
                    elif e.button==3: grid[r][c]['f']=not grid[r][c]['f']
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_r:
            grid=[[{'m':False,'r':False,'f':False,'n':0} for _ in range(COLS)] for _ in range(ROWS)]
            mines=set()
            while len(mines)<10: mines.add((random.randint(0,ROWS-1),random.randint(0,COLS-1)))
            for (r,c) in mines: grid[r][c]['m']=True
            for r in range(ROWS):
                for c in range(COLS):
                    if not grid[r][c]['m']: grid[r][c]['n']=sum(1 for dr in(-1,0,1) for dc in(-1,0,1) if (r+dr,c+dc) in mines)
    draw()
pygame.quit()
