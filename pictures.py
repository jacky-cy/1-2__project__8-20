import pygame
import math
import os
# from settings import *

CURRENT_PATH = os.path.dirname(__file__)
IMAGES_PATH = os.path.join(os.path.dirname(__file__), 'images')
IMG_PATH = os.path.join(os.path.dirname(__file__), 'img')
MUSIC_PATH = os.path.join(os.path.dirname(__file__), 'music')
SOUND_PATH = os.path.join(os.path.dirname(__file__), 'sound')

# 參數設定
PLAYER_WIDTH = 90  # 玩家圖示大小
PLAYER_HEIGHT = 90

# 玩家圖示
player_1 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player1.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_2 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player2.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_3 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player3.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_4 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player4.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_5 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player5.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_6 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player6.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_7 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player7.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_8 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player8.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_9 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player9.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_10 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player10.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_11 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player11.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_12 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player12.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_13 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player13.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_14 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player14.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_15 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player15.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_16 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player16.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_17 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player17.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_18 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player18.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_19 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player19.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_20 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player20.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_21 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player21.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_22 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player22.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_23 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player23.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_24 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player24.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_25 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player25.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_26 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player26.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_27 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player27.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_28 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player28.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_29 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player29.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_30 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player30.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_31 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player31.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_32 = pygame.transform.scale(pygame.image.load(os.path.join(
    IMAGES_PATH, "player32.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))

figure = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8,
          player_9, player_10, player_11, player_12, player_13, player_14, player_15, player_16,
          player_17, player_18, player_19, player_20, player_21, player_22, player_23, player_24,
          player_25, player_26, player_27, player_28, player_29, player_30, player_31, player_32]
fg_images = player_18

# NPC picture
doctor_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "doctor.png")), (90, 90))
nurse_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "nurse.png")), (90, 90))
openjun_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "open jun.png")), (90, 90))
enemy1_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "enemy1.png")), (90, 90))
enemy2_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "enemy2.png")), (90, 90))
enemy3_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "enemy3.png")), (90, 90))

# PROPS pictuse
alcohol_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "alcohol.png")), (61, 61))
forehead_gun_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "forehead gun.png")), (61, 61))
QRcode_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "QRcode.png")), (61, 61))
vaccine_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "vaccine.png")), (61, 61))
mask_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "mask.png")), (61, 61))

# dialog picture
dialog_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "talk_bg.png")), (475, 150))

# backpack picture
backpack_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "backpack.png")), (380, 380))

# 提示符號
hint_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "hint.png")), (43, 43))

# game over picture
game_over_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGES_PATH, "game_over.png")), (500, 600))


tool_picture_image = pygame.transform.scale(pygame.image.load(os.path.join(IMAGES_PATH, "tool_menu.png")),
                                     (450, 460))