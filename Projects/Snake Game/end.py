# The Blue Marble Academy
# Snake Game 
# Made by Darian and Arifa

import pygame
import snakegame

def main(score):
      #The screen
      pygame.init()
      dis = pygame.display.set_mode((445, 462))
      endscreen = pygame.image.load("endscreen.jpg").convert()
      endscreen_size = pygame.transform.scale(endscreen,(445,462))
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
            dis.blit(endscreen_size,(0,0))
            font = pygame.font.Font(None, 45)
            pygame.draw.rect(dis, (0,0,255),button)
            Hometext = font.render('Play', True, (123,130,185))
            
            
            endtext = font.render(f'You lost your score was:{score}', True, (123,130,185))
            dis.blit(Hometext, (185, 145))
            dis.blit(endtext, (50, 100))
            
            #apple
            font = pygame.font.Font(None, 45)
            pygame.display.update()
            
