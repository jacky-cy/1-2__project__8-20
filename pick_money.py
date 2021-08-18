# covid 19 pick money game
import pygame
import random
import os
from settings import *

FPS = 60
WIDTH = 500
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# 遊戲初始化 and 創建視窗
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("covid 19 pick money game")
clock = pygame.time.Clock()

# 載入圖片
background_img = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "blood.png")).convert(), (500, 600))
player_img = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "life.png")).convert(), (80, 100))
player_img.set_colorkey(BLACK)
life_img = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "head.png")).convert(), (25, 25))
life_img.set_colorkey(BLACK)


# 載入掉落物圖片（病毒、錢），並改變大小
virus_imgs = []
virus_imgs.append(pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy3.png")).convert(), (58, 58)))
virus_imgs.append(pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy1.png")).convert(), (75, 75)))
virus_imgs.append(pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy2.png")).convert(), (80, 80)))
virus_imgs.append(pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy3.png")).convert(), (50, 50)))

money_imgs = []
money_imgs.append(pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "bigmoney.png")).convert(), (40, 40)))
money_imgs.append(pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "midmoney.png")).convert(), (30, 30)))
money_imgs.append(pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "smallmoney.png")).convert(), (20, 20)))

virus_img3 = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy3.png")).convert(), (58, 58))
pygame.display.set_icon(virus_img3)

# 設定爆炸
expl_anim = {}
expl_anim['lg'] = []
expl_anim['sm'] = []
expl_anim['player'] = []
for i in range(9):
    expl_img = pygame.image.load(os.path.join(
        IMG_PATH, f"expl{i}.png")).convert()
    expl_img.set_colorkey(BLACK)
    expl_anim['lg'].append(pygame.transform.scale(expl_img, (75, 75)))
    expl_anim['sm'].append(pygame.transform.scale(expl_img, (30, 30)))
    player_expl_img = pygame.image.load(
        os.path.join(IMG_PATH, f"player_expl{i}.png")).convert()
    player_expl_img.set_colorkey(BLACK)
    expl_anim['player'].append(player_expl_img)

# 載入音樂、音效
die_sound = pygame.mixer.Sound(os.path.join(
    SOUND_PATH, "rumble.ogg"))
die_sound.set_volume(0.1)
expl0_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "expl0.wav"))
expl0_sound.set_volume(0.1)
gun_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "pow1.wav"))
gun_sound.set_volume(0.1)
pygame.mixer.music.load(os.path.join(
    SOUND_PATH, "pick_money_background.wav"))
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

font_name = os.path.join(os.path.dirname(__file__), "font.ttf")


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


def new_virus():
    v = Virus()
    all_sprites.add(v)
    virus.add(v)


def new_money():
    m = Ｍoney()
    all_sprites.add(m)
    money.add(m)


def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 130
    BAR_HEIGHT = 15
    fill = (hp / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def draw_lives(surf, lives, img, x, y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 32 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def draw_init():
    screen.blit(background_img, (0, 0))
    draw_text(screen, '撿金幣遊戲!', 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, '上下左右移動人物 蒐集5000金幣即可過關~', 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, '按任意鍵開始遊戲!', 18, WIDTH / 2, HEIGHT * 3 / 4)
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


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (45, 60))
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speedx = 5
        self.speedy = 5
        self.health = 100
        self.lives = 3
        self.hidden = False
        self.hide_time = 0

    def update(self):
        now = pygame.time.get_ticks()

        if self.hidden and now - self.hide_time > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.centery = HEIGHT / 2

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if key_pressed[pygame.K_UP]:
            self.rect.y -= self.speedy
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


# 設定落下的病毒
class Virus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ran_image = random.choice(virus_imgs)
        self.ran_image.set_colorkey(BLACK)
        self.image = self.ran_image.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        # 隨機選擇從地圖的哪個位置出現
        self.position = random.randrange(0, 4)
        # 地圖上方
        if self.position == 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-180, -100)
            self.speedy = random.randrange(2, 5)
            self.speedx = random.randrange(-3, 3)
            self.total_degree = 0
            self.rot_degree = random.randrange(-3, 3)
        # 地圖下方
        if self.position == 1:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(700, 780)
            self.speedy = random.randrange(-5, -2)
            self.speedx = random.randrange(-3, 3)
            self.total_degree = 0
            self.rot_degree = random.randrange(-3, 3)
        # 地圖左方
        if self.position == 2:
            self.rect.x = random.randrange(-180, -100)
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.speedy = random.randrange(-3, 3)
            self.speedx = random.randrange(2, 5)
            self.total_degree = 0
            self.rot_degree = random.randrange(-3, 3)
        # 地圖右方
        if self.position == 3:
            self.rect.x = random.randrange(700, 780)
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.speedy = random.randrange(-3, 3)
            self.speedx = random.randrange(-5, -2)
            self.total_degree = 0
            self.rot_degree = random.randrange(-3, 3)

    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree = self.total_degree % 360
        self.image = pygame.transform.rotate(self.ran_image, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.position == 0:
            if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
                self.rect.x = random.randrange(0, WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(2, 5)
                self.speedx = random.randrange(-3, 3)
        if self.position == 1:
            if self.rect.bottom < 0 or self.rect.left > WIDTH or self.rect.right < 0:
                self.rect.x = random.randrange(0, WIDTH - self.rect.width)
                self.rect.y = random.randrange(700, 780)
                self.speedy = random.randrange(-5, -2)
                self.speedx = random.randrange(-3, 3)
        if self.position == 3:
            if self.rect.right < 0 or self.rect.top < 0 or self.rect.bottom > HEIGHT:
                self.rect.x = random.randrange(700, 780)
                self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
                self.speedy = random.randrange(-3, 3)
                self.speedx = random.randrange(-5, -2)
        if self.position == 2:
            if self.rect.left > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
                self.rect.x = random.randrange(-180, -100)
                self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
                self.speedy = random.randrange(-3, 3)
                self.speedx = random.randrange(2, 5)


# 設定落下的金錢
class Ｍoney(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = random.choice(money_imgs)
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        # 隨機選擇從地圖的哪個位置出現
        self.position = random.randrange(0, 4)
        # 地圖上方
        if self.position == 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-180, -100)
            self.speedy = random.randrange(2, 5)
            self.speedx = random.randrange(-3, 3)
            self.total_degree = 0
            self.rot_degree = random.randrange(-3, 3)
        # 地圖下方
        if self.position == 1:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(700, 780)
            self.speedy = random.randrange(-5, -2)
            self.speedx = random.randrange(-3, 3)
            self.total_degree = 0
            self.rot_degree = random.randrange(-3, 3)
        # 地圖左方
        if self.position == 2:
            self.rect.x = random.randrange(-180, -100)
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.speedy = random.randrange(-3, 3)
            self.speedx = random.randrange(2, 5)
            self.total_degree = 0
            self.rot_degree = random.randrange(-3, 3)
        # 地圖右方
        if self.position == 3:
            self.rect.x = random.randrange(700, 780)
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.speedy = random.randrange(-3, 3)
            self.speedx = random.randrange(-5, -2)
            self.total_degree = 0
            self.rot_degree = random.randrange(-3, 3)

    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree = self.total_degree % 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.position == 0:
            if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
                self.rect.x = random.randrange(0, WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(2, 5)
                self.speedx = random.randrange(-3, 3)
        if self.position == 1:
            if self.rect.bottom < 0 or self.rect.left > WIDTH or self.rect.right < 0:
                self.rect.x = random.randrange(0, WIDTH - self.rect.width)
                self.rect.y = random.randrange(700, 780)
                self.speedy = random.randrange(-5, -2)
                self.speedx = random.randrange(-3, 3)
        if self.position == 3:
            if self.rect.right < 0 or self.rect.top < 0 or self.rect.bottom > HEIGHT:
                self.rect.x = random.randrange(700, 780)
                self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
                self.speedy = random.randrange(-3, 3)
                self.speedx = random.randrange(-5, -2)
        if self.position == 2:
            if self.rect.left > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
                self.rect.x = random.randrange(-180, -100)
                self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
                self.speedy = random.randrange(-3, 3)
                self.speedx = random.randrange(2, 5)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = expl_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(expl_anim[self.size]):
                self.kill()
            else:
                self.image = expl_anim[self.size][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center

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
pygame.mixer.music.play(-1)

# 遊戲迴圈
end_result = 0
show_init = True
running = True
pause = False
show_lose = False
show_win = False
while running:
    if show_init:
        close = draw_init()
        if close:
            break
        show_init = False
        all_sprites = pygame.sprite.Group()
        money = pygame.sprite.Group()
        virus = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powers = pygame.sprite.Group()
        bollets_sibling = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(4):
            new_money()
        for j in range(6):
            new_virus()
        score = 0

    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.mixer.music.stop()
            running = False
        if player.lives == 0 and not(death_expl.alive()):
            # pygame.mixer.music.stop()
            show_lose = True
            #running = False
            # money_end_result += 0
        # adjust this for different difficulty levels
        if score >= 5000:
            # pygame.mixer.music.stop()
            #running = False
            end_result += 1
            show_win = True
        if pause == False and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = True
        elif pause == True and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = False

    # 更新遊戲
    all_sprites.update()
    # 判斷金錢 人物相撞
    hits = pygame.sprite.spritecollide(
        player, money, True, pygame.sprite.collide_circle)
    for hit in hits:
        gun_sound.play()
        new_money()
        if hit.radius == 8:
            score += 100
        elif hit.radius == 12:
            score += 300
        elif hit.radius == 17:
            score += 500

    # 判斷病毒 人物相撞
    hits = pygame.sprite.spritecollide(
        player, virus, True, pygame.sprite.collide_circle)
    for hit in hits:
        expl0_sound.play()
        new_virus()
        player.health -= hit.radius
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        if player.health <= 0:
            death_expl = Explosion(player.rect.center, 'player')
            all_sprites.add(death_expl)
            die_sound.play()
            player.lives -= 1
            player.health = 100
            player.hide()

    # 畫面顯示
    screen.fill(BLACK)
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    draw_text(screen, "目前分數：", 18, WIDTH / 2 - 35, 10)
    draw_text(screen, str(score), 18, WIDTH / 2 + 35, 10)
    draw_health(screen, player.health, 5, 15)
    draw_lives(screen, player.lives, life_img, WIDTH - 100, 15)
    pygame.display.update()

    if show_win :
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
    

# pygame.quit()
