import sys, pygame
import random
from collections import deque
import numpy as np
import copy


def getPositionFromMap(mapPos):
    return (mapPos[0]*snakeNodeW,mapPos[1]*snakeNodeH)

    


pygame.init()
#code：刘兴
snakeLen=6
size = width, height = 500, 500
black = 0, 0, 0

gameMapSize=(50,50)
#gamemap
gameMap=np.zeros(gameMapSize,dtype=np.int16)
screen = pygame.display.set_mode(size)
#snake1node:
snakeNodeW=int(width/gameMapSize[0])
snakeNodeH=int(height/gameMapSize[1])
snakeNodeSize=(snakeNodeW,snakeNodeH)
snakeNodeImage = pygame.image.load("snake1.png")
snakeNode = pygame.transform.scale(snakeNodeImage,snakeNodeSize)
snakeNodeRect = snakeNode.get_rect()
#蛇节点队列
snakeNodeDeque=deque([])
fpsClock = pygame.time.Clock()
#mappos
nowNodeMapPos=[gameMapSize[0]//2,gameMapSize[1]//2]
#nowsnakenode
nowSnakeNode=snakeNode
nowSnakeNodeRect=copy.deepcopy(snakeNodeRect)
nowNodePos=getPositionFromMap(nowNodeMapPos)
nowSnakeNodeRect.x=nowNodePos[0]
nowSnakeNodeRect.y=nowNodePos[1]
gameMap[tuple(nowNodeMapPos)]=1
#snakedeque
snakeNodeDeque.append((nowSnakeNode,nowSnakeNodeRect,nowNodeMapPos))


print(nowNodeMapPos)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    runDirection=random.randint(1,4)#left,right,up,down
    
    isContiune=True
    newNodeMapPos=copy.deepcopy(nowNodeMapPos)
    for i in range(5): 
        if runDirection==1:
            oldNodeMapPos=copy.deepcopy(nowNodeMapPos)
            newNodeMapPos[0]=nowNodeMapPos[0]-1
            if newNodeMapPos[0]<0:
                isContiune=True
                newNodeMapPos=oldNodeMapPos
            elif gameMap[tuple(newNodeMapPos)]==0:
                isContiune=False

                
        elif runDirection==2  :
            oldNodeMapPos=copy.deepcopy(nowNodeMapPos)
            newNodeMapPos[0]=nowNodeMapPos[0]+1
            if newNodeMapPos[0]>=gameMapSize[0]:
                isContiune=True
                newNodeMapPos=oldNodeMapPos
            elif gameMap[tuple(newNodeMapPos)]==0:
                isContiune=False            
    
            
        elif runDirection==3 :
            oldNodeMapPos=copy.deepcopy(nowNodeMapPos)
            newNodeMapPos[1]=nowNodeMapPos[1]-1
            if newNodeMapPos[1]<0 :
                isContiune=True
                newNodeMapPos=oldNodeMapPos
            elif gameMap[tuple(newNodeMapPos)]==0:
                isContiune=False             

        elif runDirection==4 :
            oldNodeMapPos=copy.deepcopy(nowNodeMapPos)
            newNodeMapPos[1]=nowNodeMapPos[1]+1        
            if newNodeMapPos[1]>=gameMapSize[1]:
                isContiune=True
                newNodeMapPos=oldNodeMapPos
            elif gameMap[tuple(newNodeMapPos)]==0:
                isContiune=False             

       

        if not isContiune:
            print("===")
            print(nowNodeMapPos)
            print(newNodeMapPos)
            print("===") 
            break
        else:
            print(f"前方受阻，第{i}次尝试改变方向...")
            runDirection=i  
            
    if isContiune:   
        print("game over")
        pygame.quit()
        sys.exit()
        
    snakeNodeHeadNewRect= copy.deepcopy(nowSnakeNodeRect)  
    newNodePos=getPositionFromMap(newNodeMapPos)
    snakeNodeHeadNewRect.x=newNodePos[0]
    snakeNodeHeadNewRect.y=newNodePos[1]
    snakeNodeHeadNew =nowSnakeNode
    snakeNodeDeque.append((snakeNodeHeadNew,snakeNodeHeadNewRect,newNodeMapPos))
    gameMap[tuple(newNodeMapPos)]=1 
    nowNodeMapPos=copy.deepcopy(newNodeMapPos)
    nowSnakeLen=len(snakeNodeDeque)    
    if nowSnakeLen>snakeLen: 
        snakeNodeAbandon=snakeNodeDeque.popleft()
        snakeNodeAbandonPos=snakeNodeAbandon[2]
        print(f"---{snakeNodeAbandonPos}")
        print(snakeNodeDeque)
        gameMap[tuple(snakeNodeAbandonPos)]=0
        del snakeNodeAbandon
    else:
        print(f"@@@{nowSnakeLen}@@@")
    
    

    screen.fill(black)   
    for snakeNodeData in snakeNodeDeque:
        screen.blit(snakeNodeData[0],snakeNodeData[1])
    pygame.display.update()

    fpsClock.tick(5)
