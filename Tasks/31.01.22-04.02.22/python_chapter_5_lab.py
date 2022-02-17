import pygame
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139,69,19)
 
PI = 3.141592653

screen_size = (400, 500)
screen = pygame.display.set_mode(screen_size)

done = False
clock = pygame.time.Clock()
 
pygame.display.set_caption("Dustin's new house")
 
while not done:
 
    # Checking for pressing close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear screen
    screen.fill(WHITE)

    # DRAWING
    # House-walls
    pygame.draw.rect(screen, BLUE, pygame.Rect(30, 30, 60, 60))

    # House-roof
    pygame.draw.polygon(screen, RED, [[60, 0], [25, 30], [95, 30]])

    # House-door
    pygame.draw.rect(screen, GREEN, pygame.Rect(40, 60, 15, 30))

    # House-window
    pygame.draw.rect(screen, GREEN, pygame.Rect(65, 60, 15, 15))

    # Tree
    # Var tree stem
    x_stem_origin = 120
    y_stem_origin = 45
    stem_width = 15
    stem_height = 45

    # Var tree leaves
    leaves_rad = 20
    x_leaves_origin = 127
    y_leaves_origin = 45

    for i in range(1, 3):
        # Tree-stem
        pygame.draw.rect(screen, BROWN, pygame.Rect(x_stem_origin, y_stem_origin, stem_width, stem_height))

        # Tree-leaves
        pygame.draw.circle(screen, GREEN, (x_leaves_origin, y_leaves_origin), leaves_rad)

        x_stem_origin = x_stem_origin + (i * 60)
        x_leaves_origin = x_leaves_origin + (i * 60)
        
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
