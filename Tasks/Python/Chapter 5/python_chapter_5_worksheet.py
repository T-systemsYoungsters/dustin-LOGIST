import pygame

# 18.
'''
pygame.init()

screen_size = (400, 500)
screen = pygame.display.set_mode(screen_size)
RED = (200,0,0)
circleX = 100
circleY = 100
radius = 10
active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False

   pygame.draw.circle(screen,RED,(circleX,circleY),radius) # DRAW CIRCLE

   pygame.display.update()
'''