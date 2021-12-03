import pygame 

# Getting pygames started 
pygame.init()

# This creates the screen 
screen = pygame.display.set_mode((800, 600))


#Title 
pygame.display.set_caption("Chess Board")
icon = pygame.image.load('chess.png')
pygame.display.set_icon(icon)

# Game loop 
active = True 
while active: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False 