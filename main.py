import pygame

pygame.init()


SCREEN_WIDTH = 810
SCREEN_HEIGHT = 900


WIDTH = 30

#27x30

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

init_pos = [405,675]




running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")


    pygame.draw.circle(screen,"yellow",init_pos,WIDTH/2)


    pygame.display.flip()

pygame.quit()