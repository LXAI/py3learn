import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

snakeNode = pygame.image.load("snake1.png")
snakeComputer=snakeNode
snakeNodeRect = snakeNode.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    snakeNodeRect = snakeNodeRect.move(speed)
    if snakeNodeRect.left < 0 or snakeNodeRect.right > width:
        speed[0] = -speed[0]
    if snakeNodeRect.top < 0 or snakeNodeRect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(snakeComputer, snakeNodeRect)
    pygame.display.flip()