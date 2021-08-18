import pygame
import random
import os
from settings import *
# 基本定義
FPS = 5
WIDTH = 500
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
font_name = os.path.join(CURRENT_PATH, "font.ttf")

pygame.init()
screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('covid 19 Snake')
clock = pygame.time.Clock()


# 載入圖片
background_img = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "blood.png")).convert(), (500, 600))
food_img = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy1.png")).convert(), (50, 50))
snake_img = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "head.png")).convert(), (40, 40))
snake_img.set_colorkey(BLACK)
shit_img = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy2.png")).convert(), (50, 50))
shit_img.set_colorkey(BLACK)
double_img = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy3.png")).convert(), (50, 50))
double_img.set_colorkey(BLACK)

pygame.display.set_icon(shit_img)

# 載入音樂、音效
pygame.mixer.music.load(os.path.join(
    SOUND_PATH, "background_snake.wav"))
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
green_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "pow1.wav"))
gray_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "pow0.wav"))
die_sound = pygame.mixer.Sound(os.path.join(
    SOUND_PATH, "rumble.ogg"))
shit_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "expl0.wav"))
green_sound.set_volume(0.23)
gray_sound.set_volume(0.25)
die_sound.set_volume(0.25)
shit_sound.set_volume(0.25)

# 定義蛇


class Snake:
    def __init__(self):
        # 將遊戲剛開始的方向定為向右
        self.direction = pygame.K_DOWN
        self.body = []
        for x in range(5):
            self.addbody()
    # 在前方增加方塊

    def addbody(self):
        left = 0
        top = 0
        if self.body:
            (left, top) = (self.body[0].left, self.body[0].top)

        body = pygame.Rect(left, top, 50, 50)
        if self.direction == pygame.K_LEFT:
            body.left -= 50
        elif self.direction == pygame.K_RIGHT:
            body.left += 50
        elif self.direction == pygame.K_UP:
            body.top -= 50
        elif self.direction == pygame.K_DOWN:
            body.top += 50

        self.body.insert(0, body)
    # 刪掉尾巴最後一個方塊

    def delete_body(self):
        self.body.pop()

    # 判斷死亡
    def is_dead(self):
        # 判斷撞牆
        if self.body[0].x not in range(WIDTH):
            isdead = True
            return isdead
        if self.body[0].y not in range(HEIGHT):
            isdead = True
            return isdead
        # 撞倒自己身體
        if self.body[0] in self.body[1:]:
            isdead = True
            return isdead
        isdead = False
        return isdead

    # 移動
    def move(self):
        self.addbody()
        self.delete_body()
    # 改變方向，且避免方向被逆向改變

    def change_direction(self, curkey):
        LEFT_RIGHT = [pygame.K_LEFT, pygame.K_RIGHT]
        UP_DOWN = [pygame.K_UP, pygame.K_DOWN]
        if curkey in LEFT_RIGHT + UP_DOWN:
            if (curkey in LEFT_RIGHT) and (self.direction in LEFT_RIGHT):
                return
            if (curkey in UP_DOWN) and (self.direction in UP_DOWN):
                return
            self.direction = curkey

    def mybody(self):
        return self.body[:]


class Food:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(food_img, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = pygame.Rect(-50, 0, 50, 50)

    def remove(self):
        self.rect.x = -50

    def set(self):
        if self.rect.x == -50:
            allpos = []
            # 不靠牆太近 50 ~ WIDTH-50 之間
            for pos in range(50, WIDTH - 50, 50):
                allpos.append(pos)
            self.rect.x = random.choice(allpos)
            self.rect.y = random.choice(allpos)

            return [self.rect.x, self.rect.y]
    # 畫出食物

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Shit:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(shit_img, (40, 40))
        self.image.set_colorkey(BLACK)
        self.rect = pygame.Rect(-50, 0, 50, 50)

    def remove(self):
        self.rect.x = -50

    def set(self):
        if self.rect.x == -50:
            allpos = []
            # 不靠牆太近 50 ~ WIDTH-50 之間
            for pos in range(50, WIDTH - 50, 50):
                allpos.append(pos)
            self.rect.x = random.choice(allpos)
            self.rect.y = random.choice(allpos)
            return [self.rect.x, self.rect.y]
    # 畫出食物

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Double:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(double_img, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = pygame.Rect(-50, 0, 50, 50)

    def remove(self):
        self.rect.x = -50

    def set(self):
        if self.rect.x == -50:
            allpos = []
            # 不靠牆太近 50 ~ WIDTH-50 之間
            for pos in range(50, WIDTH - 50, 50):
                allpos.append(pos)
            self.rect.x = random.choice(allpos)
            self.rect.y = random.choice(allpos)
            return [self.rect.x, self.rect.y]
    # 畫出食物

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


def draw_init():
    screen.blit(background_img, (0, 0))
    draw_text(screen, '爆吃病毒吧！', 64, WIDTH / 2, HEIGHT / 5)
    draw_text(screen, '上下左右移動 分數“剛好”達到15即可過關', 22, WIDTH / 2, HEIGHT * 2 / 5)
    draw_text(screen, '藍色 : 分數加1｜紅色 : 分數加2｜黃色 : 分數除2',
              22, WIDTH / 2, HEIGHT * 4 / 7)
    draw_text(screen, '按任意鍵開始遊戲!', 18, WIDTH / 2, HEIGHT * 4 / 5)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        # 取得輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                waiting = False
                return False


def draw_win():
    screen.blit(background_img, (0, 0))
    draw_text(screen, 'YOU WIN！', 70, WIDTH / 2, HEIGHT / 5)
    draw_text(screen, '按esc鍵離開遊戲!', 18, WIDTH / 2, HEIGHT * 4 / 5)
    pygame.display.update()
    waiting1 = True
    while waiting1:
        clock.tick(FPS)
        # 取得輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting1 = False
                    return False


def draw_lose():
    screen.blit(background_img, (0, 0))
    draw_text(screen, 'YOU LOSE！', 70, WIDTH / 2, HEIGHT / 5)
    draw_text(screen, '按esc鍵離開遊戲!', 18, WIDTH / 2, HEIGHT * 4 / 5)
    pygame.display.update()
    waiting2 = True
    while waiting2:
        clock.tick(FPS)
        # 取得輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting2 = False
                    return False


def main():
    pygame.mixer.music.play(-1)
    snake = Snake()
    food = Food(screen)
    shit = Shit(screen)
    double = Double(screen)
    FPS = 5

    running = True
    isdead = False
    scores = 0
    show_init = True
    show_win = False
    show_lose = False
    # 輸贏
    global end_result
    end_result = 0
    pause = False

    while running:
        if show_init:
            close = draw_init()
        if close:
            break
        show_init = False
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # end = False
                return end_result
            if event.type == pygame.KEYDOWN:
                snake.change_direction(event.key)
            if pause == False and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = True
            elif pause == True and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False

            if scores == 15:
                #running = False
                end_result += 1
                show_win = True
                return end_result

        isdead = snake.is_dead()
        if isdead:
            die_sound.play()
            #running = False
            show_lose = True

            # 死后按space重新
            # if event.key == pygame.K_SPACE and isdead:
            # return main()

        if not pause:
            screen.fill(WHITE)
            screen.blit(background_img, (0, 0))

            # 畫蛇身
            if not isdead:
                snake.move()
            for rect in snake.body:
                screen.blit(snake_img, rect)

            # 食物處理 / 吃到1分 /速度加快
            # 當食物rect與蛇頭重合,吃掉 -> Snake增加一個body
            if food.rect == snake.body[0]:
                green_sound.play()
                scores += 1
                if FPS <= 10:
                    FPS += 0.5
                food.remove()
                snake.addbody()

            if food.set():
                if food.rect.x == shit.rect.x and food.rect.y == shit.rect.y :
                    food.set()
                elif food.rect.x == double.rect.x and food.rect.y == double.rect.y :
                    food.set()
            # 繪製這個食物
            food.blitme()
            #吃到屎/ 分數砍半
            if shit.rect == snake.body[0]:
                shit_sound.play()
                if FPS > 5:
                    FPS -= 1
                scores = int(scores / 2)
                shit.remove()
                snake.addbody()

            if shit.set() :
                if food.rect.x == shit.rect.x and food.rect.y == shit.rect.y :
                    shit.set()
                elif shit.rect.x == double.rect.x and shit.rect.y == double.rect.y :
                    shit.set()
            # 繪製這個食物
            shit.blitme()

            #吃到+2 /長度+2
            if double.rect == snake.body[0]:
                gray_sound.play()
                scores += 2
                double.remove()
                snake.addbody()

            if double.set():
                if double.rect.x == shit.rect.x and double.rect.y == shit.rect.y :
                    double.set()
                elif food.rect.x == double.rect.x and food.rect.y == double.rect.y :
                    double.set()
            # 繪製這個食物
            double.blitme()

            # 顯示分數文字
            draw_text(screen, '目前分數: ' + str(scores), 25, WIDTH / 2, 0)

            pygame.display.update()

        if pause:
            # 顯示分數文字
            draw_text(screen, '目前分數: ' + str(scores), 25, WIDTH / 2, 0)
            draw_text(screen, "按下空白鍵即可繼續遊戲", 24, WIDTH / 2, HEIGHT / 2)
            pygame.display.update()

        if show_win:
            close = draw_win()
            if close:
                break
            show_win = False
            running = False

        if show_lose:
            close = draw_lose()
            if close:
                break
            show_lose = False
            running = False


if __name__ == '__main__':
    main()
