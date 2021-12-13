import pygame
from constant import w, h
import sys
import os
import setBGM
import role
import monster
import bj
import obj
from Mylibrary import *
from Weapon_Bullet_class import *
import tools

pygame.init()
font = "static/font/ka1.ttf"

PATHS = {
    "button": [
        os.path.join("static", "images", "background", filename)
        for filename in ["background.png", "start.png", "menu.png", "exit.png"]
    ],
    "setting": [
        os.path.join("static", "images", "setting", filename)
        for filename in ["on.png", "off.png", "continue.png", "return.png", "menu.png"]
    ],
    "pause": [
        os.path.join("static", "images", "pause", filename)
        for filename in ["pause.png", "on.png", "off.png", "continue.png", "return.png"]
    ],
    "end": [
        os.path.join("static", "images", "end", filename)
        for filename in ["end.png", "replay.png", "return.png"]
    ]
}

FONTS = [
    pygame.font.Font(font, size) for size in [29, 28, 18]
]

TEXTS = {
    "start-title": "Welcome to Pixel Knight",
    "setting": "Settings",
    "music": "Music",
    "pause": "Pause",
    "win": "Win",
    "lose": "Game Over"
}

COLORS = {
    "bg": (0, 0, 0),
    "bg1": (100, 100, 100),
    "button": (200, 200, 100),
}

# size
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 45

BUTTON_SIZE = [(w, h), (230, 135), (169, 50), (179, 58)]
SETTING_SIZE = [(48, 48), (48, 48), (48, 48), (48, 48), (401, 480)]
PAUSE_SIZE = [(401, 480), (48, 48), (48, 48), (48, 48), (48, 48)]
END_SIZE = [(401, 480), (48, 48), (48, 48)]

# place position
TITLE_HEIGHT = 90
Bullet_type = 0


class Menu():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.count = 0

        pygame.display.set_mode((w, h))
        self.w = w
        self.h = h
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("Main window")

        self.win_status = "menu"  # menu, setting, start(game),

        self.info = {
            "music": {"on": True}
        }
        self.button_rects = {}

        self.bloodView = pygame.image.load("static/background/bloodvisualization.jpg").convert()
        self.bloodView = tools.get_image(self.bloodView, 0, 0, 80, 16, (255, 255, 255), h / 15 / 16)
        self.monsBbloodView = pygame.image.load("static/background/bloodvisualization.jpg").convert()
        self.monsBbloodView = tools.get_image(self.monsBbloodView, 0, 0, 80, 16, (255, 255, 255), h / 15 / 16)

        self.main_role = role.Role()
        self.monster1 = monster.slime(3 / 4 * w, h / 4, 'Pictures/monster', "slime")
        self.load_all_pics()
        self.bg = bj.bg(w / 40, -h / 4, 'Pictures/bck', 'bgimage2')
        self.bg_wall = bj.bg(w / 48, -h / 4, 'Pictures/bck', 'bgimage2_wall')
        self.enemy_group = pygame.sprite.Group(self.monster1)

        self.ticks = 0
        self.bullets = list()
        self.mouse_x = self.mouse_y = 0
        global Bullet_type
        self.weapon = Weapon(Bullet_type)
        self.weapon.float_pos = Point(49 * w / 100, 52 * h / 100)

        self.crosshair = MySprite(self.screen)
        self.crosshair.load("Pictures/weapons/crosshair_1.png", 16, 16, 1)
        self.crosshair_group = pygame.sprite.GroupSingle()
        self.crosshair_group.add(self.crosshair)
        self.angle = 0

        self.esc = False


    def load_all_pics(self):
        self.pics = {}
        for p in PATHS:
            self.pics[p] = [
                pygame.image.load(filepath) for filepath in PATHS[p]
            ]

    def draw_button(self, text, height, bi=0):
        button_img = pygame.image.load(PATHS[text][bi])
        if text == "button":
            button_img = pygame.transform.scale(button_img, BUTTON_SIZE[bi])
        elif text == "setting":
            button_img = pygame.transform.scale(button_img, SETTING_SIZE[bi])
        elif text == "pause":
            button_img = pygame.transform.scale(button_img, PAUSE_SIZE[bi])
        elif text == "end":
            button_img = pygame.transform.scale(button_img, END_SIZE[bi])
        button_rect = button_img.get_rect(center=(self.w / 2, height))
        self.screen.blit(button_img, button_rect)

        return button_rect

    def draw_status_menu(self):
        self.button_rects["start"] = self.draw_button("button", h / 2, 0)

        title = FONTS[0].render(TEXTS["start-title"], True, COLORS["bg"])
        text_rect = title.get_rect(center=(self.w / 2, TITLE_HEIGHT))
        self.screen.blit(title, text_rect)

        self.button_rects = {}

        self.button_rects["start"] = self.draw_button("button", 200, 1)
        self.button_rects["setting"] = self.draw_button("button", 300, 2)
        self.button_rects["quit"] = self.draw_button("button", 365, 3)

    def draw_status_game(self):
        self.bj_group = pygame.sprite.Group(self.bg)
        self.bj_group.add(self.bg_wall)
        self.main_role.update(self.count)
        self.enemy_group.update(self.count, (
        pygame.sprite.spritecollide(self.main_role, self.enemy_group, False), self.main_role.rect.center, self.bg.stop))
        self.bj_group.update((pygame.sprite.collide_rect(self.main_role, self.bg),
                              pygame.sprite.spritecollide(self.main_role, self.enemy_group, False)))

        self.crosshair.position = (self.mouse_x, self.mouse_y)
        self.crosshair_group.update(self.ticks)
        self.angle = target_angle(self.weapon.X, self.weapon.Y, self.crosshair.X + self.crosshair.frame_width / 2,
                                  self.crosshair.Y + self.crosshair.frame_height / 2)
        self.weapon.rotation = self.angle

        self.weapon.update(self.ticks)

        for bullet in self.bullets:
            bullet.update(self.ticks)
            if bullet.owner == "weapon":
                attacker = None
                attacker = pygame.sprite.spritecollideany(bullet, self.enemy_group)
                if attacker != None:
                    if pygame.sprite.collide_rect(bullet, attacker):
                        bullet.alive = False
                        self.monster1.blood-=1
                        if self.monster1.blood==0:
                            self.enemy_group.remove(attacker)
                            self.win_status = 'end'
                else:
                    attacker = None

        self.bj_group.draw(self.screen)
        self.screen.blit(self.main_role.image, (self.main_role.x, self.main_role.y))
        pygame.draw.rect(self.screen, (250, 0, 0),
                         (w / 11, h / 16, self.bloodView.get_width() / 65 * self.main_role.blood, h / 22), 0)
        self.screen.blit(self.bloodView, (w / 20, h / 20))
        # monster role blood
        pygame.draw.rect(self.screen, (50, 205, 50),
                         (w * 65 / 80, h / 16, self.monsBbloodView.get_width() / 72 * self.monster1.blood, h / 22), 0)
        self.screen.blit(self.monsBbloodView, (w * 16 / 20, h / 20))

        self.enemy_group.draw(self.screen)
        self.weapon.draw(self.screen)
        self.crosshair_group.draw(self.screen)
        for bullet in self.bullets:
            bullet.rotation = self.angle
            bullet.draw(self.screen)
            if bullet.alive == False:
                self.bullets.remove(bullet)

    def draw_status_setting(self):
        self.button_rects["start"] = self.draw_button("button", h / 2, 0)
        self.button_rects["setting"] = self.draw_button("setting", 250, 4)

        title = FONTS[0].render(TEXTS["setting"], True, COLORS["bg1"])

        label = FONTS[1].render(TEXTS["music"], True, COLORS["bg1"])
        label_rect = title.get_rect(center=(self.w / 2 - 40, 160))
        self.screen.blit(label, label_rect)

        music_on = self.info.get("music", {}).get("on", False)
        if music_on:
            pic = self.pics["setting"][0]
        else:
            pic = self.pics["setting"][1]

        pic_rect = pic.get_rect(center=(self.w / 2 + 100, 160))
        self.screen.blit(pic, pic_rect)

        close_pic = self.pics["setting"][3]
        close_rect = close_pic.get_rect(center=(self.w / 2, 400))
        self.screen.blit(close_pic, close_rect)

        title = FONTS[0].render("up - W        ", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 46, 200))
        self.screen.blit(title, text_rect)

        title = FONTS[0].render("down - S  ", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 46, 240))
        self.screen.blit(title, text_rect)

        title = FONTS[0].render("left - A  ", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 46, 280))
        self.screen.blit(title, text_rect)

        title = FONTS[0].render("right - D", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 46, 320))
        self.screen.blit(title, text_rect)

        self.button_rects = {
            "music": pic_rect,
            "return": close_rect,
        }

    def draw_status_pause(self):
        self.button_rects["pause"] = self.draw_button("pause", 250, 0)

        title = FONTS[0].render(TEXTS["pause"], True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2, TITLE_HEIGHT))
        self.screen.blit(title, text_rect)

        label = FONTS[1].render(TEXTS["music"], True, COLORS["bg1"])
        label_rect = title.get_rect(center=(self.w / 2 - 100, 160))
        self.screen.blit(label, label_rect)

        music_on = self.info.get("music", {}).get("on", False)
        if music_on:
            pic = self.pics["pause"][1]
        else:
            pic = self.pics["pause"][2]

        pic_rect = pic.get_rect(center=(self.w / 2 + 100, 160))
        self.screen.blit(pic, pic_rect)

        title = FONTS[0].render("Continue", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 70, 250))
        self.screen.blit(title, text_rect)

        continue_pic = self.pics["pause"][3]
        continue_rect = continue_pic.get_rect(center=(self.w / 2 + 100, 250))
        self.screen.blit(continue_pic, continue_rect)

        title = FONTS[0].render("Quit             ", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 70, 350))
        self.screen.blit(title, text_rect)

        close_pic = self.pics["pause"][4]
        close_rect = close_pic.get_rect(center=(self.w / 2 + 100, 350))
        self.screen.blit(close_pic, close_rect)

        self.button_rects = {
            "music": pic_rect,
            "continue": continue_rect,
            "pause_return": close_rect

        }

    def draw_status_end(self, i):
        self.button_rects["end"] = self.draw_button("end", 250, 0)
        if i == 0:
            title = FONTS[0].render(TEXTS["lose"], True, COLORS["bg"])
        elif i == 1:
            title = FONTS[0].render(TEXTS["win"], True, COLORS["bg"])

        text_rect = title.get_rect(center=(self.w / 2, TITLE_HEIGHT))
        self.screen.blit(title, text_rect)

        title = FONTS[0].render("Replay    ", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 70, 250))
        self.screen.blit(title, text_rect)

        replay_pic = self.pics["end"][1]
        replay_rect = replay_pic.get_rect(center=(self.w / 2 + 100, 250))
        self.screen.blit(replay_pic, replay_rect)

        title = FONTS[0].render("Quit             ", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 70, 350))
        self.screen.blit(title, text_rect)

        close_pic = self.pics["end"][2]
        close_rect = close_pic.get_rect(center=(self.w / 2 + 100, 350))
        self.screen.blit(close_pic, close_rect)

        self.button_rects = {
            "end_replay": replay_rect,
            "end_return": close_rect,
        }

    def draw_all(self):
        self.screen.fill(COLORS["bg"])

        if self.win_status == "menu":
            self.draw_status_menu()
        elif self.win_status == "start":
            self.draw_status_game()  # into game
        elif self.win_status == "setting":
            self.draw_status_setting()
        elif self.win_status == "pause":
            self.draw_status_pause()
        elif self.win_status == "end":
            setBGM.play_sound(1)
            self.draw_status_end(1)

    def get_clicked_button(self, event):
        for bt_name in self.button_rects:
            bt_rect = self.button_rects[bt_name]
            if bt_rect.collidepoint(event.pos):
                return bt_name

        return ""

    def handle_button(self, bt_name):
        if self.win_status != "start":
            if bt_name == "start":
                self.win_status = "start"
                self.weapon.fire_timer = pygame.time.get_ticks() + 1500
                if self.info["music"]["on"]:
                    setBGM.play_music(1)

            elif bt_name == "setting":
                self.win_status = "setting"
            elif bt_name == "music":
                self.info["music"]["on"] = not self.info["music"]["on"]
                if self.info["music"]["on"]:
                    if self.win_status == 'pause':
                        setBGM.play_music(1)
                    else:
                        setBGM.play_music(0)
                else:
                    setBGM.stop_sound()
            elif bt_name == "return":
                self.win_status = "menu"
            elif bt_name == "continue":
                self.win_status = "start"
            elif bt_name == "pause_return":
                setBGM.stop_sound()
                self.monster1 = monster.slime(3 / 4 * w, h / 4, 'Pictures/monster', "slime")
                self.load_all_pics()
                self.bg = bj.bg(w / 40, -h / 4, 'Pictures/bck', 'bgimage2')
                self.bg_wall = bj.bg(w / 48, -h / 4, 'Pictures/bck', 'bgimage2_wall')
                self.enemy_group = pygame.sprite.Group(self.monster1)
                self.monster1.blood=65
                self.win_status = "menu"
                setBGM.play_music(0)
            elif bt_name == "end_return":
                setBGM.stop_sound()
                self.win_status = "menu"
                setBGM.play_music(0)
            elif bt_name == "end_replay":
                # menu = Menu()
                global Bullet_type
                Bullet_type=0
                self.weapon.load("Pictures/weapons/weapon_0.png", 19, 29, 1)
                self.monster1 = monster.slime(3 / 4 * w, h / 4, 'Pictures/monster', "slime")
                self.load_all_pics()
                self.bg = bj.bg(w / 40, -h / 4, 'Pictures/bck', 'bgimage2')
                self.bg_wall = bj.bg(w / 48, -h / 4, 'Pictures/bck', 'bgimage2_wall')
                self.enemy_group = pygame.sprite.Group(self.monster1)
                self.monster1.blood=65
                self.win_status = "start"
                setBGM.play_music(1)

            elif bt_name == "end_return":
                self.win_status = "menu"
            elif bt_name == "quit":
                pygame.quit()
                sys.exit()

    def fire_cannon(self, charactor):
        global Bullet_type
        position = Point(49 * w / 100, 52 * h / 100)
        bullet = BulletSP(position, self.w, self.h, Bullet_type)
        bullet.rotation = self.angle
        bullet.velocity = angular_velocity(self.angle)  #
        self.bullets.append(bullet)
        return bullet

    def player_fire_cannon(self):
        bullet = self.fire_cannon(self.weapon)  # derive parameter for changing Bullets_i
        bullet.owner = "weapon"
        bullet.color = (30, 250, 30)

    def Bullet_read_event(self, event):
        global Bullet_type
        mouse_up = mouse_down = 0
        mouse_up_x = mouse_up_y = 0
        mouse_down_x = mouse_down_y = 0

        if event.type == MOUSEBUTTONDOWN:
            mouse_down = event.button
            mouse_down_x, mouse_down_y = event.pos
        elif event.type == MOUSEBUTTONUP:
            mouse_up = event.button
            mouse_up_x, mouse_up_y = event.pos
        b1, b2, b3 = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()  # press1/2/3/4/5/6  and change Bullets_i parameter
        if keys[K_0]:
            Bullet_type = 0
            self.weapon.load("Pictures/weapons/weapon_0.png", 19, 29, 1)
        elif keys[K_1]:
            Bullet_type = 1
            self.weapon.load("Pictures/weapons/weapon_1.png", 20, 29, 1)
        elif keys[K_2]:
            Bullet_type = 2
            self.weapon.load("Pictures/weapons/weapon_2.png", 39, 16, 1)

        elif keys[K_3]:
            Bullet_type = 3
            self.weapon.load("Pictures/weapons/weapon_3.png", 15, 42, 1)

        if keys[K_SPACE] or mouse_up > 0 and (Bullet_type == 0 or Bullet_type == 1):
            if self.ticks > self.weapon.fire_timer + 200:
                self.weapon.fire_timer = self.ticks
                self.player_fire_cannon()

        elif keys[K_SPACE] or mouse_up > 0 and (Bullet_type == 2):
            if self.ticks > self.weapon.fire_timer + 100:
                self.weapon.fire_timer = self.ticks
                self.player_fire_cannon()

        elif keys[K_SPACE] or b1 > 0 and (Bullet_type == 3):
            if self.ticks > self.weapon.fire_timer + 50:
                self.weapon.fire_timer = self.ticks
                self.player_fire_cannon()

    def handle_event(self, event):
        if self.win_status == "start":
            self.main_role.read_event(event)
            self.monster1.read_event(event)
            self.bg.read_event(event)
            self.bg_wall.read_event(event)
            self.Bullet_read_event(event)


    def run(self):
        setBGM.play_music(0)
        while True:
            self.count += 1
            self.ticks = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    bt_name = self.get_clicked_button(event)
                    self.handle_button(bt_name)

                if event.type == MOUSEMOTION:
                    self.mouse_x, self.mouse_y = event.pos
                # judge if the user wants to enter pause interface
                if self.win_status == 'start' or self.win_status == 'pause':
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            for i in self.bg.long_press:
                                self.bg.long_press[i] = False
                            for i in self.bg.long_press:
                                self.monster1.long_press[i] = False
                            for i in self.bg_wall.long_press:
                                self.bg_wall.long_press[i] = False
                            self.main_role.run=0
                            self.esc = not self.esc
                            if self.esc:
                                self.win_status = "pause"
                            else:
                                self.win_status = "start"

                self.handle_event(event)
            self.draw_all()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    menu = Menu()
    menu.run()



