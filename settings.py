import pygame
import math
import os
from pictures import *

# 基本參數設定
bg_x = 0  # 背景圖座標
bg_y = 0
WIN_WIDTH = 500  # 視窗大小
WIN_HEIGHT = 500
WHITE = (255, 255, 255)

# path
CURRENT_PATH = os.path.dirname(__file__)
IMAGES_PATH = os.path.join(os.path.dirname(__file__), 'images')
IMG_PATH = os.path.join(os.path.dirname(__file__), 'img')
MUSIC_PATH = os.path.join(os.path.dirname(__file__), 'music')
SOUND_PATH = os.path.join(os.path.dirname(__file__), 'sound')

# NPC talk sentence
talk_sentense = ["Hi!", "I am Doctor Junny.", "Welcome to Hospytall!",
                 "Please sanitize your hands with alcohol.", "Wait! Where is it?",
                 "Can you help me find alcohol?", "Not liqueur, which is sold in the market.",
                 "Is it in Lobby? Try to find it.", "Thanks! Try to talk to others. Good luck."]
talk_sentense_2 = ["Hello!", "I'm Nurse Chen.", "I can't find forehead gun and vaccine.",
                   "One of them really disappeared!", "You can find it everywhere.",
                   "(TIPS: My last name without 'n')", "Well done! Find out Sandy, and beat it!"]
talk_sentense_3 = ["I'm Open Jun.", "Always open~ Seven Eleven~", "Wait! Have you scanned the QRcode?",
                   "OH NO!! My QRcode was gone.", "And... Why aren't you wearing mask?",
                   "OMG!! Go to find the QRcode and mask!", "Find them for me. Hurry!!",
                   "(TIPS: Try to look for more information)", "Good job! Try to help others."]
talk_sentense_4 = ["Hey!", "I'm En.. En...", "En... Enemy Jacky...",
                   "Do you want to play a game with me?",
                   "Enter (Y) to start, or enter (N) to leave.", "Oh no! Sky will revenge for me!"]
talk_sentense_5 = ["Bonjour!", "Wa da si wa Enemy Sky des.", "How terrible! Did you defeat Jacky?",
                   "Unbelievable!!!", "Over my dead body!!",
                   "Enter (Y) to start, or enter (N) to leave.", "Shxt! Sandy will revenge for us!"]
talk_sentense_6 = ["Anniu ha se yo~", "Wa si Enemy Sandy Jun ><", "If two enemies are not enough, defeat me!!",
                   "Come on baby, come on!", "Enter (Y) to start, or enter (N) to leave.",
                   "You have overcome the epidemic battle."]

# PROPS talk sentence
alcohol_sentence = ["You get alcohol.", "Please check your backpack."]
forehead_gun_sentence = ["You get a forcehead gun.", "Please check your backpack."]
QRcode_sentence = ["You get a QRcode.", "Please check your backpack."]
vaccine_sentence = ["You get vaccine.", "Please check your backpack."]
mask_sentence = ["You get a mask.", "Please check your backpack."]

# 按鍵設定
keydict = {"up": pygame.K_UP, "down": pygame.K_DOWN,
           "left": pygame.K_LEFT, "right": pygame.K_RIGHT}


def keyPressed(keyCheck=""):
    global keydict
    keys = pygame.key.get_pressed()
    if sum(keys) > 0:
        if keyCheck == "" or keys[keydict[keyCheck.lower()]]:
            return True
    return False


class Figure:
    def __init__(self):
        self.clock_run = True
        self.current_time = 0
        pass

    def clock(self):
        if self.clock_run == True:
            self.current_time += 6
        elif self.clock_run == False:
            self.current_time = 0
        return self.current_time
