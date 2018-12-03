import pygame

pygame.init()

white = (0,0,0)
black = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('sample game')

exit_game = False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    screen.fill(red)
    pygame.display.update()
