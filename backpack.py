import pygame
import math
import os
from settings import *

props_picked = None

class PROPS:
    def __init__(self, image, name, x, y, pos_change_x, pos_change_y):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.center = (x + pos_change_x, y + pos_change_y)
        self.words = talk_sentense
        self.dis = 0
        self.x = x
        self.y = y
        self.range = 100
        pass

    def draw(self, win):
        win.blit(self.image , (self.x, self.y))

    def distance(self):
        props_x, props_y = self.rect.center
        player_x = 500/2 - PLAYER_WIDTH/2
        player_y = 600/2 - PLAYER_HEIGHT/2
        distance = math.sqrt((props_x-player_x)**2+(props_y-player_y)**2)
        self.dis = distance
        if distance <= self.range:
            return True
        else:
            return False

    @classmethod
    def Alcohol(cls, x, y, pos_change_x, pos_change_y):
        al = cls(alcohol_image, "Alcohol", x, y, pos_change_x, pos_change_y)
        al.words = alcohol_sentence
        return al

    @classmethod
    def ForeheadGun(cls, x, y, pos_change_x, pos_change_y):
        fhg = cls(forehead_gun_image, "Forehead Gun", x, y, pos_change_x, pos_change_y)
        fhg.words = forehead_gun_sentence
        return fhg

    @classmethod
    def QRcode(cls, x, y, pos_change_x, pos_change_y):
        qr = cls(QRcode_image, "QRcode", x, y, pos_change_x, pos_change_y)
        qr.words = QRcode_sentence
        return qr

    @classmethod
    def Vaccine(cls, x, y, pos_change_x, pos_change_y):
        va = cls(vaccine_image, "Vaccine", x, y, pos_change_x, pos_change_y)
        va.words = vaccine_sentence
        return va

    @classmethod
    def Mask(cls, x, y, pos_change_x, pos_change_y):
        ma = cls(mask_image, "Mask", x, y, pos_change_x, pos_change_y)
        ma.words = mask_sentence
        return ma


class PROPS_Group:
    def __init__(self):
        self.pos_change_x = 0
        self.pos_change_y = 0
        self.props_list = []
        self.selected = None
        self.picked = False
        self.alcohol_picked = False
        self.foreheadgun_picked = False
        self.QRcode_picked = False
        self.vaccine_picked = False
        self.mask_picked = False

        self.alcohol_start = False
        self.foreheadgun_start = False
        self.QRcode_start = False
        self.vaccine_start = False
        self.mask_start = False

        self.start = False
        self.sentence = 0
        pass

    def update(self):
        self.props_list = [PROPS.Alcohol(1000, 340, self.pos_change_x, self.pos_change_y),
                           PROPS.ForeheadGun(650, 800, self.pos_change_x, self.pos_change_y),
                           PROPS.QRcode(1500, 780, self.pos_change_x, self.pos_change_y),
                           PROPS.Vaccine(1500, 2200, self.pos_change_x, self.pos_change_y),
                           PROPS.Mask(550, 1900, self.pos_change_x, self.pos_change_y)]

    def is_selected(self):
        for props in self.props_list:
            if props.distance() == True:
                self.selected = props
                return self.selected
        return None

    def hint(self, win):
        self.which_is_picked()
        if self.is_selected() != None and self.start == True:
            win.blit(hint_image, (230, 220))

    def which_is_picked(self):
        if self.is_selected()!= None:
            if self.selected.name == "Alcohol":
                self.picked = self.alcohol_picked
                self.start = self.alcohol_start
            elif self.selected.name == "Forehead Gun":
                self.picked = self.foreheadgun_picked
                self.start = self.foreheadgun_start
            elif self.selected.name == "QRcode":
                self.picked = self.QRcode_picked
                self.start = self.QRcode_start
            elif self.selected.name == "Vaccine":
                self.picked = self.vaccine_picked
                self.start = self.vaccine_start
            elif self.selected.name == "Mask":
                self.picked = self.mask_picked
                self.start = self.mask_start
        else:
            return None

    def open_dialog(self):
        self.which_is_picked()
        global props_picked
        if self.start == True:
            props_picked = self.selected

        if self.is_selected()!= None and self.picked == False and self.start == True:
            if self.sentence <= len(self.selected.words)-1:
                self.sentence += 1
                return True
            else:
                if self.selected.name == "Alcohol":
                    self.alcohol_picked = True
                elif self.selected.name == "Forehead Gun":
                    self.foreheadgun_picked = True
                elif self.selected.name == "QRcode":
                    self.QRcode_picked = True
                elif self.selected.name == "Vaccine":
                    self.vaccine_picked = True
                elif self.selected.name == "Mask":
                    self.mask_picked = True
                self.sentence = 0
                return False
        if self.is_selected() != None and self.picked == True:
            if self.sentence == 0:
                self.sentence += 1
                return True
            else:
                self.sentence = 0
                return False
        else:
            return False

    def dialog_sentence(self, win):
        if self.selected != None:
            if self.sentence <= len(self.selected.words) and self.picked == False:
                font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                font = pygame.font.Font(font_name, 16)
                text_surface = font.render(self.selected.words[self.sentence-1], True, WHITE)
                win.blit(text_surface, (160, 40))
            elif self.picked == True:
                font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                font = pygame.font.Font(font_name, 16)
                text_surface = font.render("You have picked it.", True, WHITE)
                win.blit(text_surface, (160, 40))

    def draw_dialog(self, win):
        if self.selected != None:
            win.blit(dialog_image, (10, 10))
            win.blit(self.selected.image, (55, 43))
            if self.selected.name != "Forehead Gun":
                font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                font = pygame.font.Font(font_name, 16)
                text_name = font.render(self.selected.name, True, WHITE)
                win.blit(text_name, (60, 127))
            elif self.selected.name == "Forehead Gun":
                font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                font = pygame.font.Font(font_name, 16)
                text_name = font.render(self.selected.name, True, WHITE)
                win.blit(text_name, (38, 127))

    def draw_PROPS(self, win):
        for props in self.props_list:
            if props.name != "QRcode" and props.name != "Vaccine":
                props.draw(win)


class Backpack:
    def __init__(self):
        self.props_list = []
        self.props_num = 0
        self.props_new = None
        pass

    def add_props(self):
        global props_picked
        if props_picked != None and self.props_list != []:
            repeat = 0
            for i in self.props_list:
                if props_picked.name == i.name:
                    repeat += 1
            if repeat == 0:
                self.props_list.append(props_picked)
                self.props_num += 1
        elif props_picked != None and self.props_list == []:
            self.props_list.append(props_picked)
            self.props_num += 1

    def draw(self, win):
        win.blit(backpack_image, (60, 60))
        if self.props_list != []:
            for i in range(self.props_num):
                if i < 3:
                    win.blit(self.props_list[i].image, (130 + i * 90, 205))
                else:
                    win.blit(self.props_list[i].image, (130 + (i-3) * 90, 285))