import pygame, sys

pygame.init()
window = pygame.display.set_mode((800, 550))

paintName = pygame.font.SysFont("Courier", 40).render("DB Mall", 1, (255, 255, 0), (255, 255, 255))

boardSize = paintName.get_size()
frameSpeed = pygame.time.Clock()

while 1:
    frameSpeed.tick(50)
    window.fill((0, 0, 0))

    mouseCoordinates = pygame.mouse.get_pos()

    x = mouseCoordinates[0]
    y = mouseCoordinates[1]

    if x + boardSize[0] > 800:
        x = 700- boardSize[0]
    if y + boardSize[1] > 550:
        y = 500- boardSize[1]
    window.blit(paintName, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
