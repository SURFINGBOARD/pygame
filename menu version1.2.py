import pygame
from constant import w,h
import sys
import os
import setBGM
import role


pygame.init()
font = "static/font/ka1.ttf"


PATHS = {
    "button": [
        os.path.join("static", "images", "background", filename)
        for filename in ["background.png","start.png","menu.png","exit.png"]
    ],
    "setting": [
        os.path.join("static", "images", "setting", filename)
        for filename in ["on.png","off.png","continue.png","return.png","menu.png"]
    ],
    "pause": [
            os.path.join("static", "images", "pause", filename)
            for filename in ["pause.png","on.png","off.png","continue.png","return.png"]
    ],
    "end": [
            os.path.join("static", "images", "end", filename)
            for filename in ["win.png","game over.png"]
    ]
}

FONTS = [
    pygame.font.Font(font, size) for size in [29, 28, 18]
]

TEXTS = {
    "start-title": "Welcome to Pixel Knight",
    "setting": "Settings",
    "music": "Music",
    "pause":"Pause"
}

COLORS = {
    "bg": (0, 0, 0),
    "bg1": (100, 100, 100),
    "button": (200, 200, 100),
}

# size
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 45

# 新size
BUTTON_START_WIDTH = 230
BUTTON_START_HEIGHT = 135
BUTTON_MENU_WIDTH = 169
BUTTON_MENU_HEIGHT = 50
BUTTON_EXIT_WIDTH = 300
BUTTON_EXIT_HEIGHT = 85
BUTTON_SIZE=[(500,500),(230,135),(169,50),(179,58)]
SETTING_SIZE=[(48,48),(48,48),(48,48),(48,48),(401,480)]
PAUSE_SIZE=[(401,480),(48,48),(48,48),(48,48),(48,48)]
END_SIZE=[(201,275),(201,275)]


# place position
TITLE_HEIGHT = 90


class Menu():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.count = 0
        # 设置窗口
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

        bgpic = pygame.image.load("图片/背景/bg.jpg")
        self.bgpic = pygame.transform.scale(bgpic, (w, h))

        self.main_role = role.Role()
        self.load_all_pics()

    def load_all_pics(self):
        self.pics = {}
        for p in PATHS:
            self.pics[p] = [
                pygame.image.load(filepath) for filepath in PATHS[p]
            ]


    def draw_button(self, text, height, bi=0):
        button_img = pygame.image.load(PATHS[text][bi])
        # button_img = pygame.transform.scale(button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
        if text=="button":
            button_img = pygame.transform.scale(button_img, BUTTON_SIZE[bi])
        elif text=="setting":
            button_img = pygame.transform.scale(button_img, SETTING_SIZE[bi])
        elif text=="pause":
            button_img = pygame.transform.scale(button_img, PAUSE_SIZE[bi])
        button_rect = button_img.get_rect(center=(self.w / 2, height))
        self.screen.blit(button_img, button_rect)

        # button_text = FONTS[2].render(text, True, COLORS["button"])
        # text_rect = button_text.get_rect(center=(self.w / 2, height))
        # self.screen.blit(button_text, text_rect)

        return button_rect

    def draw_status_menu(self):
        self.button_rects["start"] = self.draw_button("button", 250, 0)

        # title = FONTS[0].render(TEXTS["start-title"], True, COLORS["bg1"])
        title = FONTS[0].render(TEXTS["start-title"], True, COLORS["bg"])
        text_rect = title.get_rect(center=(self.w / 2, TITLE_HEIGHT))
        self.screen.blit(title, text_rect)

        self.button_rects = {}

        self.button_rects["start"] = self.draw_button("button", 200, 1)
        self.button_rects["setting"] = self.draw_button("button", 300, 2)
        self.button_rects["quit"] = self.draw_button("button", 365, 3)

    def draw_status_game(self):
        self.main_role.animation()

        self.main_role.change_speed()
        #   改变位置
        self.main_role.update_pos(self.count)
        # rendering
        self.screen.blit(self.bgpic, (0, 0))
        self.screen.blit(self.main_role.image, (self.main_role.x, self.main_role.y))

    def draw_status_setting(self):
        self.button_rects["start"] = self.draw_button("button", 250, 0)
        self.button_rects["setting"] = self.draw_button("setting", 250, 4)
        # pic = self.pics["setting"][4] # 画menu菜单
        # pic_rect = pic.get_rect(center=(self.w / 2, 200))
        # self.screen.blit(pic, pic_rect)

        title = FONTS[0].render(TEXTS["setting"], True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2, TITLE_HEIGHT))
        # self.screen.blit(title, text_rect) # 不显示setting字样

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

        # 键位
        title = FONTS[0].render("up - W", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 77, 200))
        self.screen.blit(title, text_rect)

        title = FONTS[0].render("down - S", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 53, 240))
        self.screen.blit(title, text_rect)

        title = FONTS[0].render("left - A", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 53, 280))
        self.screen.blit(title, text_rect)

        title = FONTS[0].render("right - R", True, COLORS["bg1"])
        text_rect = title.get_rect(center=(self.w / 2 - 46, 320))
        self.screen.blit(title, text_rect)

        self.button_rects = {
            "music": pic_rect,
            "return1": close_rect,
        }

    def draw_status_pause(self):
        # self.button_rects["start"] = self.draw_button("button", 250, 0)
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

        # 按下continue的键位判断还没写
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
            "return1": close_rect,
        }


    def draw_all(self):
        self.screen.fill(COLORS["bg"])

        if self.win_status == "menu":
            self.draw_status_menu()
        elif self.win_status == "start":
            self.draw_status_game()  # into game

        elif self.win_status == "setting":
            # self.draw_status_setting()
            # 先测试pause
            self.draw_status_pause()

    def get_clicked_button(self, event):
        for bt_name in self.button_rects:
            bt_rect = self.button_rects[bt_name]
            if bt_rect.collidepoint(event.pos):
                return bt_name

        return ""

    def handle_button(self, bt_name):
        if bt_name == "start":
            self.win_status = "start"
            if self.info["music"]["on"]:
                setBGM.play_music(1)

        elif bt_name == "setting":
            self.win_status = "setting"
        elif bt_name == "music":
            self.info["music"]["on"] = not self.info["music"]["on"]
            if self.info["music"]["on"]:
                setBGM.play_music(0)
            else:
                setBGM.stop_sound()
        elif bt_name == "return1":
            self.win_status = "menu"
        elif bt_name == "quit":
            pygame.quit()
            sys.exit()


    def handle_event(self, event):
        if self.win_status == "start":
            self.main_role.read_event(event)

    def run(self):
        setBGM.play_music(0)
        while True:

            self.count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    bt_name = self.get_clicked_button(event)
                    self.handle_button(bt_name)

                self.handle_event(event)

            self.draw_all()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    menu = Menu()
    menu.run()



