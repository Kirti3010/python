import pygame, sys

pygame.init()
window = pygame.display.set_mode((800, 550))

paintName = pygame.font.SysFont("Courier", 40).render("DB Mall", 1, (255, 255, 0), (255, 255, 255))
x, y = 0, 0
directionsX, directionsY = 1, 2

boardSize = paintName.get_size()
frameSpeed = pygame.time.Clock()

while 1:
    frameSpeed.tick(50)
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    window.blit(paintName, (x, y))

    x += 5 * directionsX
    y += 5 * directionsY

    if x + boardSize[0] > 800 or x <= 0:
        directionsX *= -1
    if y + boardSize[1] > 550 or y <= 0:
        directionsY *= -1

    x = x + 1
    pygame.display.update()
