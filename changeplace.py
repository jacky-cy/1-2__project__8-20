#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import math



class Change_place():
    def __init__(self, centerx, centery):
        self.rect0=pygame.Rect(centerx, centery, 30, 20)
        
        self.place1=pygame.Rect(1420,220,200,120)
        self.place2=pygame.Rect(1360,1500,210,160)
        
    def iscollide_place1(self):
        return pygame.Rect.colliderect(self.rect0, self.place1)
    def iscollide_place2(self):
        return pygame.Rect.colliderect(self.rect0, self.place2)
    
    
    
    
"""
            
            
            self.place1=pygame.Rect(1420,220,200,120)
            pygame.draw.rect(bg_images, (0, 0, 0), self.place1, 0)
            self.place2=pygame.Rect(1360,1500,210,230)
            pygame.draw.rect(bg_images, (0, 0, 0), self.place2, 0)
            
"""