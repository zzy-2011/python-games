import pygame, sys
pygame.init()
import os as _os; _FN=r"C:\Windows\Fonts\msyh.ttc" if _os.path.exists(r"C:\Windows\Fonts\msyh.ttc") else None
lvl=["########","#      #","# .$@. #","#      #","#  $   #","#  .   #","########"]
ROWS=len(lvl); COLS=max(len(x) for x in lvl)
CELL=40; W=COLS*CELL; H=ROWS*CELL+30
screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("推箱子")
font=pygame.font.Font(_FN,24)
grid=[list(row.ljust(COLS,'#')) for row in lvl]
player=None
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c]=='@': player=(r,c); grid[r][c]=' '
def draw():
    screen.fill((40,40,60))
    for r in range(ROWS):
        for c in range(COLS):
            ch=grid[r][c]
            if ch=='#': pygame.draw.rect(screen,(80,80,100),(c*CELL,r*CELL,CELL,CELL))
            elif ch=='$': pygame.draw.rect(screen,(200,150,60),(c*CELL+4,r*CELL+4,CELL-8,CELL-8))
            elif ch=='.': pygame.draw.rect(screen,(120,200,120),(c*CELL+10,r*CELL+10,CELL-20,CELL-20))
            elif ch=='*': pygame.draw.rect(screen,(120,255,120),(c*CELL+4,r*CELL+4,CELL-8,CELL-8))
    pygame.draw.circle(screen,(80,160,255),(player[1]*CELL+CELL//2,player[0]*CELL+CELL//2),CELL//3)
    screen.blit(font.render("方向键推箱子 全部到目标点",True,(255,255,255)),(5,H-26))
    pygame.display.flip()
def move(dr,dc):
    global player, grid
    r,c=player; nr,nc=r+dr,c+dc
    if grid[nr][nc]=='#': return
    if grid[nr][nc] in ('$','*'):
        br,bc=nr+dr,nc+dc
        if grid[br][bc] in (' ','.'):
            grid[br][bc]='*' if grid[br][bc]=='.' else '$'
            grid[nr][nc]='.' if grid[nr][nc]=='*' else ' '
            player=(nr,nc)
    elif grid[nr][nc] in (' ','.'):
        player=(nr,nc)
draw(); running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        elif e.type==pygame.KEYDOWN:
            if e.key==pygame.K_LEFT: move(0,-1)
            elif e.key==pygame.K_RIGHT: move(0,1)
            elif e.key==pygame.K_UP: move(-1,0)
            elif e.key==pygame.K_DOWN: move(1,0)
    draw()
pygame.quit()
