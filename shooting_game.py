# covid 19 shooting game
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
pygame.display.set_caption("covid 19 shooting")
clock = pygame.time.Clock()

# 載入圖片
background_img = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "blood.png")).convert(), (500, 600))
player_img = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "player.png")).convert(), (60, 70))
player_mini_img = pygame.transform.scale(player_img, (25, 25))
life_img = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "head.png")).convert(), (30, 30))
life_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(os.path.join(
    IMG_PATH, "bullet.png")).convert()
# 載入病毒圖片，並改變大小
virus_imgs = []
virus_img1 = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy1.png")).convert(), (28, 28))
virus_imgs.append(virus_img1)
virus_img2 = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy2.png")).convert(), (43, 43))
virus_img2.set_colorkey(WHITE)
virus_imgs.append(virus_img2)
virus_img3 = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy3.png")).convert(), (58, 58))
virus_img3.set_colorkey(WHITE)
virus_imgs.append(virus_img3)
virus_img4 = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy1.png")).convert(), (73, 73))
virus_img4.set_colorkey(WHITE)
virus_imgs.append(virus_img4)
virus_img5 = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy2.png")).convert(), (88, 88))
virus_img5.set_colorkey(WHITE)
virus_imgs.append(virus_img5)
virus_img6 = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy3.png")).convert(), (103, 103))
virus_img6.set_colorkey(WHITE)
virus_imgs.append(virus_img6)
virus_img7 = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy1.png")).convert(), (118, 118))
virus_img7.set_colorkey(WHITE)
virus_imgs.append(virus_img7)
virus_img8 = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "enemy2.png")).convert(), (133, 133))
virus_img8.set_colorkey(WHITE)
virus_imgs.append(virus_img8)

pygame.display.set_icon(virus_img1)

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
# 建立掉寶
power_imgs = {}
power_imgs['gun'] = pygame.image.load(
    os.path.join(IMG_PATH, "gun.png")).convert()
power_imgs['alcohol'] = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_PATH, "vaccine.png")).convert(), (35, 35))

# 載入音樂、音效
shoot_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "shoot.wav"))
gun_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "pow1.wav"))
alcohol_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "pow0.wav"))
die_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "rumble.ogg"))
expl_sounds = []
expl0_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "expl0.wav"))
expl1_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "expl1.wav"))
expl_sounds.append(expl0_sound)
expl_sounds.append(expl1_sound)
expl0_sound.set_volume(0.18)
expl1_sound.set_volume(0.18)
expl_sounds.append(expl0_sound)
expl_sounds.append(expl1_sound)
shoot_sound.set_volume(0.18)
gun_sound.set_volume(0.18)
alcohol_sound.set_volume(0.18)
die_sound.set_volume(0.18)
pygame.mixer.music.load(os.path.join(SOUND_PATH, "background_shoot.wav"))
pygame.mixer.music.set_volume(0.33)

font_name = os.path.join(CURRENT_PATH, "font.ttf")


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
    draw_text(screen, '病毒防衛戰!', 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, '擊敗病毒獲取十罐疫苗即可過關！', 22, WIDTH / 2, HEIGHT * 2 / 5)
    draw_text(screen, '← →移動人物 空白鍵發射子彈~', 22, WIDTH / 2, HEIGHT * 2 / 3)
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
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8
        self.health = 100
        self.lives = 3
        self.hidden = False
        self.hide_time = 0
        self.gun = 1
        self.gun_time = 0

    def update(self):
        now = pygame.time.get_ticks()
        if self.gun > 1 and now - self.gun_time > 5000:
            self.gun = 1
            self.gun_time = now

        if self.hidden and now - self.hide_time > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        if not(self.hidden):
            if self.gun == 1:
                bullet = Bullet0(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            elif self.gun == 3:
                bullet0 = Bullet0(self.rect.centerx, self.rect.centery)
                bullet1 = Bullet1(self.rect.left, self.rect.centery)
                bullet2 = Bullet2(self.rect.right, self.rect.centery)
                all_sprites.add(bullet0)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet0)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 500)

    def gunup(self):
        self.gun = 3
        self.gun_time = pygame.time.get_ticks()


class Virus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = random.choice(virus_imgs)
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-180, -100)
        self.speedy = random.randrange(2, 5)
        self.speedx = random.randrange(-3, 3)
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
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)


class Bullet0(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Bullet1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
        self.speedx = -3

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0 or self.rect.right < 0:
            self.kill()


class Bullet2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
        self.speedx = 3

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0 or self.rect.left > WIDTH:
            self.kill()


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


class Power(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['gun', 'alcohol'])
        self.image = power_imgs[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 4

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()


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
show_win = False
show_lose = False
shoot_time = 0
while running:
    if show_init:
        close = draw_init()
        if close:
            break
        show_init = False
        all_sprites = pygame.sprite.Group()
        virus = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powers = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            new_virus()
        score = 0

    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            running = False

        if player.lives <= 0 and not(death_expl.alive()):
            pygame.mixer.music.stop()
            #running = False
            show_lose = True

        # adjust this to adjust the difficulty level
        if score >= 10:
            pygame.mixer.music.stop()
            #running = False
            end_result += 1
            show_win = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                now = pygame.time.get_ticks()
                if now - shoot_time > 250:
                    shoot_time = now
                    player.shoot()

    # 更新遊戲
    all_sprites.update()
    # 判斷病毒 子彈相撞
    hits = pygame.sprite.groupcollide(virus, bullets, True, True)
    for hit in hits:
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        new_virus()

    # 判斷病毒 人物相撞
    hits = pygame.sprite.spritecollide(
        player, virus, True, pygame.sprite.collide_circle)
    for hit in hits:
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

    # 判斷寶物 人物相撞
    hits = pygame.sprite.spritecollide(player, powers, True)
    for hit in hits:
        if hit.type == 'gun':
            player.gunup()
            gun_sound.play()
        elif hit.type == 'alcohol':
            alcohol_sound.play()
            score += 1

    # 畫面顯示
    screen.fill(BLACK)
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    draw_text(screen, "目前分數：", 18, WIDTH / 2 - 25, 10)
    draw_text(screen, str(score), 18, WIDTH / 2 + 25, 10)
    draw_health(screen, player.health, 5, 15)
    draw_lives(screen, player.lives, life_img, WIDTH - 100, 15)
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

# pygame.quit()
