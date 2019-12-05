# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:14:58 2019

@author: nikhil
"""

import pygame
pygame.init()
screen=pygame.display.set_mode((80,100))
running = True
while (running ==True):
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            pygame.quit
            running=False
            break
        pygame.display.flip()
