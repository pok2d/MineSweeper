import pygame

# Importation and Initialization
pygame.init()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Minesweeper')
running = True
icon = pygame.image.load('mine.png')
pygame.display.set_icon(icon)

# Main variables

minetile = pygame.image.load('mine.png')
unknowntile = pygame.image.load('unknown.png')
onetile = pygame.image.load('one.png')
twotile = pygame.image.load('two.png')
threetile = pygame.image.load('three.png')
fourtile = pygame.image.load('four.png')
fivetile = pygame.image.load('five.png')
sixtile = pygame.image.load('six.png')
seventile = pygame.image.load('seven.png')
eighttile = pygame.image.load('eight.png')


# Main game loop
while running:

    # Quit detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Loading sequence for background and other objects.
    window.fill((0, 0, 0))
    window.blit(minetile, (0, 0))
    window.blit(unknowntile, (40, 0))
    window.blit(onetile, (80, 0))
    window.blit(twotile, (120, 0))
    window.blit(threetile, (160, 0))
    window.blit(fourtile, (200, 0))
    window.blit(fivetile, (240, 0))
    window.blit(sixtile, (280, 0))
    window.blit(seventile, (320, 0))
    window.blit(eighttile, (360, 0))

    # Update the pygame display.
    pygame.display.update()