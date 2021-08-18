#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pygame
from settings import *

class Area():
    """area of map"""
    def __init__(self, centerx, centery, win):
        #中心點
        self.rect0=pygame.Rect(centerx, centery, 30, 20)
        self.win=win
        
        self.area1=pygame.Rect(310,220,110,480)
        self.area2=pygame.Rect(420,220,950,470)
        self.area3=pygame.Rect(1370,220,270,470)
        self.area4=pygame.Rect(1640,220,250,470)
        self.area5=pygame.Rect(560,690,240,250)
        self.area6=pygame.Rect(800,690,470,510)
        self.area7=pygame.Rect(1270,690,470,510)
        self.area8=pygame.Rect(480,1490,260,600)##2
        self.area9=pygame.Rect(740,1490,600,400)##2
        self.area10=pygame.Rect(740,1890,470,470)##2
        self.area11=pygame.Rect(1340,1490,270,420)##2
        self.area12=pygame.Rect(1210,1890,400,470)##2
    def in_this_area(self):
        
        color=(94,38,18)
        font_name = os.path.join(CURRENT_PATH, "arial.ttf")
        font = pygame.font.Font(font_name, 20)
        #render方法返回Surface物件
        text = font.render('Door',True,color,None)
        
        textRect = text.get_rect()
        textRect.center=(70,555)
               
        if pygame.Rect.contains(self.area1, self.rect0):
            
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area2, self.rect0):
            text = font.render('Lobby',True,color,None)
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area3, self.rect0):
            text = font.render('Elevator(1F)',True,color,None)
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area4, self.rect0):
            text = font.render('7-11',True,color,None)
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area5, self.rect0):
            text = font.render('Toilet',True,color,None)
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area6, self.rect0):
            text = font.render('Consulting Room',True,color,None)
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area7, self.rect0):
            text = font.render('Ward',True,color,None)
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area8, self.rect0):
            text = font.render('Waiting Room',True,color,None)
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area9, self.rect0):
            text = font.render('Waiting Room',True,color,None)
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area10, self.rect0):
            text = font.render('Operating Room',True,color,None)
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area11, self.rect0):
            text = font.render('Elevator(2F)',True,color,None)
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area12, self.rect0):
            text = font.render('Check Room',True,color,None)
            self.win.blit(text, textRect)
        else:
            None
            
            
            
"""

            self.area1=pygame.Rect(310,220,110,480)
            pygame.draw.rect(bg_images, (255,255,255), self.area1, 0)
            self.area2=pygame.Rect(420,220,950,470)
            pygame.draw.rect(bg_images, (0,0,0), self.area2, 0)
            self.area3=pygame.Rect(1370,220,270,470)
            pygame.draw.rect(bg_images, (255,0,0), self.area3, 0)
            self.area4=pygame.Rect(1640,220,250,470)
            pygame.draw.rect(bg_images, (255,255,0), self.area4, 0)
            self.area5=pygame.Rect(560,690,240,250)
            pygame.draw.rect(bg_images, (255,255,0), self.area5, 0)
            self.area6=pygame.Rect(800,690,470,510)
            pygame.draw.rect(bg_images, (128,128,128), self.area6, 0)
            self.area7=pygame.Rect(1270,690,470,510)
            pygame.draw.rect(bg_images, (200,200,100), self.area7, 0)
            self.area8=pygame.Rect(480,1490,260,600)
            pygame.draw.rect(bg_images, (255,255,255), self.area8, 0)
            self.area9=pygame.Rect(740,1490,600,400)
            pygame.draw.rect(bg_images, (255,255,255), self.area9, 0)
            self.area10=pygame.Rect(740,1890,470,470)
            pygame.draw.rect(bg_images, (255,0,0), self.area10, 0)
            self.area11=pygame.Rect(1340,1490,270,420)
            pygame.draw.rect(bg_images, (255,255,0), self.area11, 0)
            self.area12=pygame.Rect(1210,1890,400,470)
            pygame.draw.rect(bg_images, (0,0,0), self.area12, 0)
"""