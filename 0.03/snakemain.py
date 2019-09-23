import sys, pygame
import random
from collections import deque
pygame.init()
#code：刘兴
size = width, height = 320, 240
black = 0, 0, 0
snakeNodeSize=(24,24)

screen = pygame.display.set_mode(size)

snakeNodeImage = pygame.image.load("snake1.png")
snakeNode = pygame.transform.scale(snakeNodeImage,snakeNodeSize)
snakeNodeRect = snakeNode.get_rect()
print(snakeNode.get_size())
print(snakeNodeRect.width,snakeNodeRect.height)
snakeNodeDeque=deque([])#蛇节点队列
fpsClock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    runSpeed = [24, 24]
    runDirection=random.randint(1,4)#left,right,up,down
    if runDirection==1:
        runSpeed[1]=0 
        runSpeed[0]=-runSpeed[0]
    elif runDirection==2:
        runSpeed[1]=0     
    elif runDirection==3:
        runSpeed[0]=0
        runSpeed[1]=-runSpeed[1]
    elif runDirection==4:
        runSpeed[0]=0     


    snakeNodeRect= snakeNodeRect.move(runSpeed)

    if snakeNodeRect.left < 0 :
        snakeNodeRect.x=width-snakeNodeRect.width
    if snakeNodeRect.right > width:
        snakeNodeRect.x=0    
    if snakeNodeRect.top < 0:
        snakeNodeRect.y=height-snakeNodeRect.height
    if snakeNodeRect.bottom > height:
        snakeNodeRect.y=0
    snakeNodeHeadNew = snakeNode
    snakeNodeHeadNewRect= snakeNodeRect
    snakeNodeDeque.append((snakeNodeHeadNew,snakeNodeHeadNewRect))

        
    if len(snakeNodeDeque)>10:
        snakeNodeAbandon=snakeNodeDeque.popleft()
        del snakeNodeAbandon
    
    screen.fill(black)   
    for snakeNodeData in snakeNodeDeque:
        screen.blit(snakeNodeData[0],snakeNodeData[1])
    pygame.display.update()
    fpsClock.tick(5)