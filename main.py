import pygame
import time
import math
from detector import *
from settings import *
from pictures import *
from npc import *
from backpack import *
from wall import *
from start_menu import *
from area import *
from changeplace import *
WIN_WIDTH = 500
WIN_HEIGHT = 600
FPS = 80

# initialize
pygame.init()
pygame.mixer.init()
# clock
clock = pygame.time.Clock()

#set icon
icon_image = pygame.transform.scale(
    pygame.image.load(os.path.join(
        IMAGES_PATH, "player22.png")), (2208, 2582))
pygame.display.set_icon(icon_image)

# set the title
pygame.display.set_caption("Hospytall")

# set the window
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

bg_images = pygame.transform.scale(
    pygame.image.load(os.path.join(
        IMAGES_PATH, "hospital2.png")), (2208, 2582))
fg_images = player_18
menu_images = pygame.transform.scale(pygame.image.load(os.path.join(IMAGES_PATH, "start_menu.png")),
                                     (WIN_WIDTH, WIN_HEIGHT))

tool_images = pygame.transform.scale(pygame.image.load(os.path.join(IMAGES_PATH, "tool.png")),
                                     (480, 80))

class Game:
    def __init__(self):
        self.figure = Figure()
        self.next_frame = 0
        self.frame = 0
        self.open_npc = False
        self.open_props = False
        self.open_bp = 0
        self.open_tool = 0
        self.NPC = NPC_Group()
        self.PROPS = PROPS_Group()
        self.backpack = Backpack()
        self.menu = menu_images
        self.counter = 0
        # touch botton
        self.start_btn = Buttons(150, 290, 200, 60)
        self.sound_btn = Buttons(380, 520, 40, 30)
        self.mute_btn = Buttons(420, 545, 40, 30)
        self.bag_btn = Buttons(305, 520, 60, 60)
        self.tool_btn = Buttons(225, 520, 60, 60)
        self.buttons = [self.start_btn]
        # opening music
        self.openings = pygame.mixer.Sound(
            os.path.join(MUSIC_PATH, "opening.wav"))
        self.start = pygame.mixer.Sound(
            os.path.join(MUSIC_PATH, "start_sound.wav"))
        self.start.set_volume(0.22)
        self.change = pygame.mixer.Sound(
            os.path.join(MUSIC_PATH, "change_place.wav"))
        self.change.set_volume(0.22)
        self.muse = pygame.mixer.Sound(
            os.path.join(MUSIC_PATH, "muse.wav"))
        self.muse.set_volume(0.22)
        self.sound = pygame.mixer.Sound(
            os.path.join(MUSIC_PATH, "sound.wav"))
        self.sound.set_volume(0.22)
        self.backpack_sound = pygame.mixer.Sound(
            os.path.join(MUSIC_PATH, "backpack.wav"))
        self.backpack_sound.set_volume(0.22)
        self.tool_sound = pygame.mixer.Sound(
            os.path.join(MUSIC_PATH, "tool.wav"))
        self.tool_sound.set_volume(0.22)
        self.foot_sound = pygame.mixer.Sound(
            os.path.join(MUSIC_PATH, "foot.wav"))
        self.foot_sound.set_volume(0.1)
        self.pick_sound = pygame.mixer.Sound(
            os.path.join(MUSIC_PATH, "pick.wav"))
        self.pick_sound.set_volume(0.3)
        pass

    def play_music(self):
        pygame.mixer.music.load(
            os.path.join(MUSIC_PATH, "opening.wav"))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.openings.set_volume(0.2)

    def game_run(self):
        global bg_x, bg_y, fg_images
        # 中心位置
        centerx, centery = (235, 320)
        # opening music
        self.play_music()
        window.blit(self.menu, (bg_x, bg_y))

        run = True
        while run:
            clock.tick(FPS)
            if self.counter == 0:
                window.blit(self.menu, (bg_x, bg_y))

            elif self.counter == 1:
                self.buttons = [self.sound_btn, self.mute_btn,
                                self.bag_btn, self.tool_btn]
                window.blit(bg_images, (bg_x, bg_y))
                window.blit(fg_images, (250 - PLAYER_WIDTH /
                                        2, 300 - PLAYER_HEIGHT / 2))
                self.NPC.draw_NPC(bg_images)
                self.PROPS.draw_PROPS(bg_images)
                window.blit(tool_images, (10, 510))

            x, y = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if hit start btn
                    if self.start_btn.clicked(x, y) and self.counter == 0:
                        self.counter += 1
                        self.start.play()
                    elif self.sound_btn.clicked(x, y) and self.counter != 0:
                        self.sound.play()
                        pygame.mixer.music.unpause()
                    elif self.mute_btn.clicked(x, y) and self.counter != 0:
                        self.muse.play()
                        pygame.mixer.music.pause()
                    elif self.bag_btn.clicked(x, y) and self.counter != 0:
                        self.backpack_sound.play()
                        self.open_bp += 1
                    elif self.tool_btn.clicked(x, y) and self.counter != 0:    
                        self.tool_sound.play()
                        self.open_tool += 1
                        pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.open_npc = self.NPC.open_dialog()
                        self.open_props = self.PROPS.open_dialog()
                        self.backpack.add_props()
                        if self.PROPS.sentence == 1:
                            self.pick_sound.play()
                        if self.open_npc == False:
                            self.figure.clock_run = True
                        if Change_place(centerx, centery).iscollide_place1():
                            self.change.play()
                            centerx -= 60
                            centery += 1310
                            bg_x += 60
                            bg_y -= 1310
                            self.NPC.pos_change_x += 60
                            self.NPC.pos_change_y -= 1310
                            self.PROPS.pos_change_y += 60
                            self.PROPS.pos_change_y -= 1310
                        elif Change_place(centerx, centery).iscollide_place2():
                            self.change.play()
                            centerx += 60
                            centery -= 1270
                            bg_x -= 60
                            bg_y += 1270
                            self.NPC.pos_change_x -= 60
                            self.NPC.pos_change_y += 1270
                            self.PROPS.pos_change_y -= 60
                            self.PROPS.pos_change_y += 1270

                    if event.key == pygame.K_b:
                        self.backpack_sound.play()
                        self.open_bp += 1
                    if event.key == pygame.K_t:
                        self.tool_sound.play()
                        self.open_tool += 1
                    if event.key == pygame.K_y and self.open_npc == True:
                        self.figure.clock_run = False
                        self.NPC.open_pick_money()
                        self.NPC.open_shooting_game()
                        self.NPC.open_snake_game()
                        pass
                    if event.key == pygame.K_n:
                        self.open_npc = self.NPC.open_dialog()

            for btn in self.buttons:  # 用for檢查每一個按鈕是否有按到~
                btn.create_frame(x, y)  # 利用已經創造了功能畫出邊框(創造邊框)
                btn.draw_frame(window)  # 利用已經創造了功能畫出邊框(劃出邊框)

            self.NPC.hint(window)
            self.PROPS.hint(window)  # 提示圖顯示與否

            if self.open_npc == True:
                self.NPC.draw_dialog(window)
                self.NPC.dialog_sentence(window)

            if self.open_props == True:
                self.PROPS.draw_dialog(window)
                self.PROPS.dialog_sentence(window)

            if self.open_bp % 2 == 1:
                self.backpack.draw(window)

            if self.open_tool % 2 == 1:
                window.blit(tool_picture_image,(25,25))


            if self.figure.clock() > self.next_frame:
                self.frame = (self.frame + 1) % 8
                self.next_frame += 100
            if self.figure.clock() == 0:
                self.next_frame = 0

            if self.open_npc == False and self.open_props == False and self.open_bp % 2 == 0\
                    and self.NPC.enemy3_task == False:
                if keyPressed("right"):
                    fg_images = figure[0 * 8 + self.frame]
                    if Wall(centerx, centery).iscollide_right() == -1 and self.counter != 0:
                        bg_x -= 5
                        self.NPC.pos_change_x -= 5
                        self.PROPS.pos_change_x -= 5
                        centerx += 5
                    if pygame.mixer.get_busy() == False:
                        self.foot_sound.play()

                if keyPressed("left") :
                    fg_images = figure[1 * 8 + self.frame]
                    if Wall(centerx, centery).iscollide_left() == -1 and self.counter != 0:
                        bg_x += 5
                        self.NPC.pos_change_x += 5
                        self.PROPS.pos_change_x += 5
                        centerx -= 5
                    if pygame.mixer.get_busy() == False:
                        self.foot_sound.play()
                    
                if keyPressed("down") :
                    fg_images = figure[2 * 8 + self.frame]
                    if Wall(centerx, centery).iscollide_down() == -1 and self.counter != 0:
                        bg_y -= 5
                        self.NPC.pos_change_y -= 5
                        self.PROPS.pos_change_y -= 5
                        centery += 5
                    if pygame.mixer.get_busy() == False:
                        self.foot_sound.play()
                    
                if keyPressed("up") :
                    fg_images = figure[3 * 8 + self.frame]
                    if Wall(centerx, centery).iscollide_up() == -1 and self.counter != 0:
                        bg_y += 5
                        self.NPC.pos_change_y += 5
                        self.PROPS.pos_change_y += 5
                        centery -= 5
                    if pygame.mixer.get_busy() == False:
                        self.foot_sound.play()
                    
            if self.open_npc == False and self.NPC.enemy3_task == True:
                window.blit(game_over_image, (0, 0))
                self.NPC.game_over = True

            self.PROPS.alcohol_start = self.NPC.doctor_start
            self.PROPS.QRcode_start = self.NPC.openjun_start
            self.PROPS.mask_start = self.NPC.openjun_start
            self.PROPS.foreheadgun_start = self.NPC.nurse_start
            self.PROPS.vaccine_start = self.NPC.nurse_start

            self.NPC.doctor_task = self.PROPS.alcohol_picked
            if self.PROPS.QRcode_picked and self.PROPS.mask_picked:
                self.NPC.openjun_task = True
            if self.PROPS.foreheadgun_picked and self.PROPS.vaccine_picked:
                self.NPC.nurse_task = True

            self.NPC.update()
            self.PROPS.update()
            

            # 偵測background邊界
            Detector(bg_images, bg_x, bg_y, WIN_WIDTH, WIN_HEIGHT).detect()

            Area(centerx, centery, window).in_this_area()

            pygame.display.update()
        pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_RPG = Game()
    test_RPG.game_run()
