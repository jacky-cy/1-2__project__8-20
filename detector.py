#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import math
import os
from settings import *


class Detector:
    """ensure the background in (0,0)"""

    def __init__(self, something, bg_x, bg_y, win_width, win_height):
        self.bg_x = bg_x
        self.bg_y = bg_y
        self.something = something
        self.win_width = win_width
        self.win_height = win_height

    def detect(self):
        if self.bg_x > 0:
            self.bg_x = 0
        elif self.bg_x < -1788 + self.win_width:
            self.bg_x = -1788 + self.win_width
        elif self.bg_y > 0:
            self.bg_y = 0
        elif self.bg_y < -1116 + self.win_height:
            self.bg_y = -1116 + self.win_height




             

