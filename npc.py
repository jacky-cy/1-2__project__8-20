import pygame
import math
import os
from settings import *
from backpack import *
import sys
import os
from importlib import reload

# current_path = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(current_path, "shooting"))
# sys.path.append(os.path.join(current_path + '/shooting', 'img'))

imported_money_or_not = 0
imported_shooting_or_not = 0
imported_snake_or_not = 0

end_result_money_rgb = 0
end_result_shooting_rgb = 0
end_result_snake_rgb = 0


class NPC:
    def __init__(self, image, name, x, y, pos_change_x, pos_change_y):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.center = (x + pos_change_x, y + pos_change_y)
        self.words = talk_sentense
        self.x = x
        self.y = y
        self.range = 100
        pass

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def distance(self):
        npc_x, npc_y = self.rect.center
        player_x = 500 / 2 - PLAYER_WIDTH / 2
        player_y = 600 / 2 - PLAYER_HEIGHT / 2
        distance = math.sqrt((npc_x - player_x)**2 + (npc_y - player_y)**2)
        if distance <= self.range:
            return True
        else:
            return False

    @classmethod
    def Doctor(cls, x, y, pos_change_x, pos_change_y):
        dt = cls(doctor_image, "Doctor", x, y, pos_change_x, pos_change_y)
        dt.words = talk_sentense
        return dt

    @classmethod
    def Nurse(cls, x, y, pos_change_x, pos_change_y):
        nur = cls(nurse_image, "Nurse", x, y, pos_change_x, pos_change_y)
        nur.words = talk_sentense_2
        return nur

    @classmethod
    def OpenJun(cls, x, y, pos_change_x, pos_change_y):
        oj = cls(openjun_image, "Open Jun", x, y, pos_change_x, pos_change_y)
        oj.words = talk_sentense_3
        return oj

    @classmethod
    def Enemy1(cls, x, y, pos_change_x, pos_change_y):
        en1 = cls(enemy1_image, "Jacky", x, y, pos_change_x, pos_change_y)
        en1.words = talk_sentense_4
        return en1

    @classmethod
    def Enemy2(cls, x, y, pos_change_x, pos_change_y):
        en2 = cls(enemy2_image, "Sky", x, y, pos_change_x, pos_change_y)
        en2.words = talk_sentense_5
        return en2

    @classmethod
    def Enemy3(cls, x, y, pos_change_x, pos_change_y):
        en3 = cls(enemy3_image, "Sandy", x, y, pos_change_x, pos_change_y)
        en3.words = talk_sentense_6
        return en3


class NPC_Group:
    def __init__(self):
        self.pos_change_x = 0
        self.pos_change_y = 0
        self.npc_list = []
        self.selected = None
        self.selected_task = False
        self.doctor_task = False
        self.nurse_task = False
        self.openjun_task = False
        self.enemy1_task = False
        self.enemy2_task = False
        self.enemy3_task = False

        self.doctor_start = False  # props can be picked or not
        self.nurse_start = False  # props can be picked or not
        self.openjun_start = False
        self.enemy1_start = False
        self.enemy2_start = False
        self.enemy3_start = False

        self.enemy3_show = False
        self.game_over = False
        self.sentence = 0
        pass

    def update(self):
        self.npc_list = [NPC.Doctor(500, 300, self.pos_change_x, self.pos_change_y),
                         NPC.Nurse(1400, 2030, self.pos_change_x,
                                   self.pos_change_y),
                         NPC.OpenJun(1680, 270, self.pos_change_x,
                                     self.pos_change_y),
                         NPC.Enemy1(1500, 1000, self.pos_change_x,
                                    self.pos_change_y),
                         NPC.Enemy2(950, 2150, self.pos_change_x,
                                    self.pos_change_y),
                         NPC.Enemy3(1000, 900, self.pos_change_x, self.pos_change_y), ]

    def hint(self, win):
        if self.is_selected() != None:
            if self.nurse_task == True and self.selected.name == "Sandy":
                win.blit(hint_image, (230, 220))

    def is_selected(self):
        for npc in self.npc_list:
            if npc.distance() == True:
                self.selected = npc
                return self.selected
        return None

    def which_is_selected(self):
        if self.is_selected() != None:
            if self.selected.name == "Doctor":
                self.selected_task = self.doctor_task
                self.doctor_start = True
            elif self.selected.name == "Nurse":
                self.selected_task = self.nurse_task
                if self.enemy2_task == True:
                    self.nurse_start = True
            elif self.selected.name == "Open Jun":
                self.selected_task = self.openjun_task
                if self.enemy1_task == True:
                    self.openjun_start = True
            elif self.selected.name == "Jacky":
                self.selected_task = self.enemy1_task
                if self.doctor_task == True:
                    self.enemy1_start = True
            elif self.selected.name == "Sky":
                self.selected_task = self.enemy2_task
                if self.openjun_task == True:
                    self.enemy2_start = True
            elif self.selected.name == "Sandy":
                self.selected_task = self.enemy3_task
                if self.nurse_task == True:
                    self.enemy3_start = True

    def open_dialog(self):
        self.which_is_selected()
        if self.is_selected() != None and self.game_over == False:
            if self.selected.name == "Open Jun" and self.openjun_start == False:
                if self.sentence == 0 and self.selected_task == False:
                    self.sentence += 1
                    return True
                elif self.sentence == 1 and self.selected_task == False:
                    self.sentence = 0
                    return False
            elif self.selected.name == "Nurse" and self.nurse_start == False:
                if self.sentence == 0 and self.selected_task == False:
                    self.sentence += 1
                    return True
                elif self.sentence == 1 and self.selected_task == False:
                    self.sentence = 0
                    return False
            elif self.selected.name == "Jacky" and self.enemy1_start == False:
                if self.sentence == 0 and self.selected_task == False:
                    self.sentence += 1
                    return True
                elif self.sentence == 1 and self.selected_task == False:
                    self.sentence = 0
                    return False
            elif self.selected.name == "Sky" and self.enemy2_start == False:
                if self.sentence == 0 and self.selected_task == False:
                    self.sentence += 1
                    return True
                elif self.sentence == 1 and self.selected_task == False:
                    self.sentence = 0
                    return False
            elif self.selected.name == "Sandy" and self.enemy3_start == False:
                return False
            else:
                if self.sentence < len(self.selected.words) - 1 and self.selected_task == False:
                    self.sentence += 1
                    return True
                elif self.selected_task == False:
                    self.sentence = 0
                    return False

                if self.sentence == 0 and self.selected_task == True:
                    self.sentence += 1
                    return True
                elif self.sentence == 1 and self.selected_task == True:
                    self.sentence = 0
                    return False
        else:
            return False

    def open_pick_money(self):
        if self.selected.name == "Sky" and self.sentence == len(self.selected.words) - 1:
            # if self.selected.name == "Doctor":
            global imported_money_or_not
            if imported_money_or_not == 0:
                import pick_money
                imported_money_or_not += 1
            else:
                global pick_money
                reload(pick_money)
            # resume music
            pygame.mixer.music.load(
                os.path.join(MUSIC_PATH, "opening.wav"))
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

            global end_result_money_rgb
            end_result_money_rgb += pick_money.end_result
            # print('the game result from pick-money is',
            #       pick_money.end_result)
            if end_result_money_rgb > 0:
                #print('Money game is completed')
                self.enemy2_task = True
                self.selected_task = self.enemy2_task
                self.sentence = 1
            #else:
                #print('Money game is Failed')
        pass

    def open_shooting_game(self):
        if self.selected.name == "Jacky" and self.sentence == len(self.selected.words) - 1:
            # if self.selected.name == "Enemy 1":
            global imported_shooting_or_not
            if imported_shooting_or_not == 0:
                import shooting_game
                imported_shooting_or_not += 1
            else:
                global shooting_game
                reload(shooting_game)
            # resume music
            pygame.mixer.music.load(
                os.path.join(MUSIC_PATH, "opening.wav"))
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

            global end_result_shooting_rgb
            end_result_shooting_rgb += shooting_game.end_result
            # print('the game result from shooting is',
            #      shooting_game.end_result)
            if end_result_shooting_rgb > 0:
                #print('shooting game is completed')
                self.enemy1_task = True
                self.selected_task = self.enemy1_task
                self.sentence = 1
            #else:
                #print('Shooting game is Failed')
        pass

    def open_snake_game(self):
        if self.selected.name == "Sandy" and self.sentence == len(self.selected.words) - 1:
            # if self.selected.name == "Enemy":
            global imported_snake_or_not
            global snake
            if imported_snake_or_not == 0:
                import snake
                snake.main()
                imported_snake_or_not += 1
            else:
                reload(snake)
                snake.main()

            global end_result_snake_rgb
            end_result_snake_rgb += snake.end_result
            # print('the game result from shooting is',
            #      shooting_game.end_result)
            if end_result_snake_rgb > 0:
                print('Snake game is completed')
                self.enemy3_task = True
                self.selected_task = self.enemy3_task
                self.sentence = 1
            else:
                pygame.mixer.music.load(
                    os.path.join(MUSIC_PATH, "opening.wav"))
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)
                #print('snake game is Failed')
        pass

    def dialog_sentence(self, win):
        # print(self.sentence)
        if self.selected != None and self.selected_task == False:
            if self.selected.name == "Open Jun" and self.openjun_start == False:
                font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                font = pygame.font.Font(font_name, 16)
                text_surface = font.render(
                    "Always open, seven eleven~", True, WHITE)
                win.blit(text_surface, (160, 40))
            elif self.selected.name == "Nurse" and self.nurse_start == False:
                font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                font = pygame.font.Font(font_name, 16)
                text_surface = font.render(
                    "I'm busy. Don't bother me!", True, WHITE)
                win.blit(text_surface, (160, 40))
            elif self.selected.name == "Jacky" and self.enemy1_start == False:
                font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                font = pygame.font.Font(font_name, 16)
                text_surface = font.render(
                    "Haha. I'll kill you, little boy.", True, WHITE)
                win.blit(text_surface, (160, 40))
            elif self.selected.name == "Sky" and self.enemy2_start == False:
                font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                font = pygame.font.Font(font_name, 16)
                text_surface = font.render(
                    "I'm hungry. I want to eat healthy human!", True, WHITE)
                win.blit(text_surface, (160, 40))

            else:
                if self.sentence < len(self.selected.words):
                    font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                    font = pygame.font.Font(font_name, 16)
                    text_surface = font.render(
                        self.selected.words[self.sentence - 1], True, WHITE)
                    win.blit(text_surface, (160, 40))
                    if self.selected.name == "Sandy":
                        self.enemy3_show = True
        elif self.selected_task == True:
            font_name = os.path.join(CURRENT_PATH, "arial.ttf")
            font = pygame.font.Font(font_name, 16)
            text_surface = font.render(
                self.selected.words[len(self.selected.words) - 1], True, WHITE)
            win.blit(text_surface, (160, 40))

    def draw_dialog(self, win):
        if self.selected != None:
            win.blit(dialog_image, (10, 10))
            win.blit(self.selected.image, (40, 30))
            if self.selected.name != "Sky" and self.selected.name != "Open Jun":
                font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                font = pygame.font.Font(font_name, 16)
                text_name = font.render(self.selected.name, True, WHITE)
                win.blit(text_name, (60, 127))
            elif self.selected.name == "Sky":
                font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                font = pygame.font.Font(font_name, 16)
                text_name = font.render(self.selected.name, True, WHITE)
                win.blit(text_name, (70, 127))
            elif self.selected.name == "Open Jun":
                font_name = os.path.join(CURRENT_PATH, "arial.ttf")
                font = pygame.font.Font(font_name, 16)
                text_name = font.render(self.selected.name, True, WHITE)
                win.blit(text_name, (55, 127))


    def draw_NPC(self, win):
        for npc in self.npc_list:
            if npc.name != "Sandy":
                npc.draw(win)
            elif npc.name == "Sandy" and self.enemy3_show == True:
                npc.draw(win)
