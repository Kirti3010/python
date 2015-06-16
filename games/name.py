import pygame, sys

pygame.init()

windowSize = (600, 400)
window = pygame.display.set_mode(windowSize)       #set d width and height of the window

name = pygame.font.Sysfont("Courier",20)

paint =name.render("hlw mlw khelw",1,(255,0,255),(255,255,255))            #paint the screen

while 1:
    for x in pygame.event.get():      #events(for performing something)on d window
        if x.type == pygame.QUIT:
            sys.exit()        #for the clossing window

    window.blit(paint,(100, 50))
    pygame.display.update()
