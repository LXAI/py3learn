import sys, pygame
import random
from collections import deque
import numpy as np


def getPositionFromMap(mapPos):
    return (mapPos[0]*snakeNodeW,mapPos[1]*snakeNodeH)




pygame.init()
#code：刘兴
snakeLen=10
size = width, height = 500, 500
black = 0, 0, 0

gameMapSize=(50,50)
snakeNodeW=int(width/gameMapSize[0])
snakeNodeH=int(height/gameMapSize[1])
gameMap=np.zeros(gameMapSize,dtype=np.int16)


screen = pygame.display.set_mode(size)
snakeNodeSize=(snakeNodeW,snakeNodeH)
snakeNodeImage = pygame.image.load("snake1.png")
snakeNode = pygame.transform.scale(snakeNodeImage,snakeNodeSize)
snakeNodeRect = snakeNode.get_rect()
print(snakeNode.get_size())
print(snakeNodeRect.width,snakeNodeRect.height)
snakeNodeDeque=deque([])#蛇节点队列
fpsClock = pygame.time.Clock()
[0,0]
nowNodeMapPos=[gameMapSize[0]//2,gameMapSize[1]//2]
newNodeMapPos=nowNodeMapPos
nowNodePos=getPositionFromMap(nowNodeMapPos)
snakeNodeRect.x=nowNodePos[0]
snakeNodeRect.y=nowNodePos[1]
snakeNodeDeque.append((snakeNode,snakeNodeRect,nowNodeMapPos))
gameMap[tuple(nowNodeMapPos)]=1
print(nowNodeMapPos)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    runSpeed = list(snakeNodeSize)
    runDirection=random.randint(1,4)#left,right,up,down
    
    isContiune=True
    for i in range(2):        
        if runDirection==1 and isContiune :
            newNodeMapPos[0]=nowNodeMapPos[0]-1
            if newNodeMapPos[0]<0:
                isContiune=True
            elif gameMap[tuple(newNodeMapPos)]==0:
                isContiune=False
                runSpeed[1]=0 
                runSpeed[0]=-runSpeed[0]
                
        if runDirection==2 and isContiune :
            newNodeMapPos[0]=nowNodeMapPos[0]+1
            if newNodeMapPos[0]>=gameMapSize[0]:
                isContiune=True
            elif gameMap[tuple(newNodeMapPos)]==0:
                isContiune=False            
                runSpeed[1]=0     
            
        if runDirection==3 and isContiune :
            newNodeMapPos[1]=nowNodeMapPos[1]-1
            if newNodeMapPos[1]<0 :
                isContiune=True
            elif gameMap[tuple(newNodeMapPos)]==0:
                isContiune=False             
                runSpeed[0]=0
                runSpeed[1]=-runSpeed[1]
        if runDirection==4 and isContiune :
            newNodeMapPos[1]=nowNodeMapPos[1]+1        
            if newNodeMapPos[1]>=gameMapSize[1]:
                isContiune=True
            elif gameMap[tuple(newNodeMapPos)]==0:
                isContiune=False             
                runSpeed[0]=0 
        print("===")
        print(nowNodeMapPos)
        print(newNodeMapPos)
        print("===")        
        if not isContiune:
            break
        
        
    if isContiune:   
        print("game over")
        pygame.quit()
        sys.exit()
        

    snakeNodeRect= snakeNodeRect.move(runSpeed)
    snakeNodeHeadNew = snakeNode
    snakeNodeHeadNewRect= snakeNodeRect
    snakeNodeDeque.append((snakeNodeHeadNew,snakeNodeHeadNewRect,newNodeMapPos))
    gameMap[tuple(newNodeMapPos)]=1 
    nowNodeMapPos=newNodeMapPos
        
    if len(snakeNodeDeque)>snakeLen: 
        snakeNodeAbandon=snakeNodeDeque.popleft()
        snakeNodeAbandonPos=snakeNodeAbandon[2]
        gameMap[tuple(snakeNodeAbandonPos)]=0
        del snakeNodeAbandon
    

    screen.fill(black)   
    for snakeNodeData in snakeNodeDeque:
        screen.blit(snakeNodeData[0],snakeNodeData[1])
    pygame.display.update()

    fpsClock.tick(5)
