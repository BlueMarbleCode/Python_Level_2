# The Blue Marble Academy
# Snake Game 
# Made by Darian and Arifa

import pygame
import snakegame

#The screen
pygame.init()
dis = pygame.display.set_mode((445, 462))
snake = pygame.image.load("snake.jpg").convert()
snake_size = pygame.transform.scale(snake,(445,462))
button = pygame.Rect(123, 130, 205, 50)

gameover = True
while gameover:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              gameover = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                  if button.collidepoint(event.pos):
                        snakegame.main()
      #screen
      dis.fill ((255,255,255))

      #apple
      dis.blit(snake_size, (0, 0))

      font = pygame.font.Font(None, 45)
      Hometext = font.render('Snake Game', True, (92,138,185))
      dis.blit(Hometext, (123, 100))

      pygame.draw.rect(dis, (0,0,255),button)
      Play = font.render('Play', True, (92,138,185))
      dis.blit(Play, (195, 138))
      
      pygame.display.update()

