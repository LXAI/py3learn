import sys, pygame
import random
from collections import deque
import numpy as np

pygame.init()
#code：刘兴
snakeLen=10
size = width, height = 500, 500
black = 0, 0, 0

gameMapSize=(50,50)
snakeNodeW=int(width/gameMapSize[0])
snakeNodeH=int(height/gameMapSize[1])
gameMap=np.zeros(gameMapSize,dtype=np.int16)
snakeShowPos=[0,0]

screen = pygame.display.set_mode(size)
snakeNodeSize=(snakeNodeW,snakeNodeH)
snakeNodeImage = pygame.image.load("snake1.png")
snakeNode = pygame.transform.scale(snakeNodeImage,snakeNodeSize)
snakeNodeRect = snakeNode.get_rect()
print(snakeNode.get_size())
print(snakeNodeRect.width,snakeNodeRect.height)
snakeNodeDeque=deque([])#蛇节点队列
fpsClock = pygame.time.Clock()
newNodeMapPos=[0,0]
nowNodeMapPos=[0,0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    runSpeed = list(snakeNodeSize)
    runDirection=random.randint(1,4)#left,right,up,down
    if runDirection==1:
        if (newNodeMapPos[0]<0):
            continue
        runSpeed[1]=0 
        runSpeed[0]=-runSpeed[0]
    elif runDirection==2:
        if (newNodeMapPos[1]>=gameMapSize[0]):
            continue
        runSpeed[1]=0     
    elif runDirection==3:
        runSpeed[0]=0
        runSpeed[1]=-runSpeed[1]
    elif runDirection==4:
        runSpeed[0]=0     


    snakeNodeRect= snakeNodeRect.move(runSpeed)
    snakeNodeHeadNew = snakeNode
    snakeNodeHeadNewRect= snakeNodeRect
    snakeNodeDeque.append((snakeNodeHeadNew,snakeNodeHeadNewRect))

        
    if len(snakeNodeDeque)>snakeLen:
        snakeNodeAbandon=snakeNodeDeque.popleft()
        del snakeNodeAbandon
    
    screen.fill(black)   
    for snakeNodeData in snakeNodeDeque:
        screen.blit(snakeNodeData[0],snakeNodeData[1])
    pygame.display.update()
    fpsClock.tick(5)

def getPositionFromMap(mapPos):
    return (mapPos[0]*snakeNodeW,mapPos[1]*snakeNodeH)