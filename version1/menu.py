import pygame
from constant import w,h
import sys
import os

pygame.init()
font = "static/font/ka1.ttf"

# PATHS = {
#     "button": [os.path.join("static", "images", "Buttons", "Button{:0>2d}.png".format(i))
#                for i in range(1, 17) ]
# }
# print(PATHS)

# PATHS = {
#     "button": [os.path.join("static", "images", "background",i for i in ["background.png","menu.png","start.png"])]
# }
# print(PATHS) #这个要怎么写才不报错？

PATHS = {
    "button": [os.path.join("static", "images", "background","background.png"),
        os.path.join("static", "images", "background","start.png"),
        os.path.join("static", "images", "background","menu.png"),
        os.path.join("static", "images", "background","exit.png")] # 可以写成上面那种for循环吗？
}
print(PATHS)

FONTS = [
    pygame.font.Font(font, 29) for size in [30, 28, 18] # 这句什么意思,后面三个数的作用？
]

TEXTS = {
    "start-title": "Welcome to Pixel Knight"
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


# place position
TITLE_HEIGHT = 50


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

        self.win_status = "menu"
        self.button_rects = {}

    def draw_button(self, text, height, bi=0):
        button_img = pygame.image.load(PATHS["button"][bi])
        # button_img = pygame.transform.scale(button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
        button_img = pygame.transform.scale(button_img, BUTTON_SIZE[bi])
        button_rect = button_img.get_rect(center=(self.w / 2, height))
        self.screen.blit(button_img, button_rect)

        # button_text = FONTS[2].render(text, True, COLORS["button"])
        # text_rect = button_text.get_rect(center=(self.w / 2, height))
        # self.screen.blit(button_text, text_rect)

        return button_rect

    def draw_all(self):  #
        self.screen.fill(COLORS["bg"])

        if self.win_status == "menu":
            self.button_rects["start"] = self.draw_button("Background", 250, 0)

            # title = FONTS[0].render(TEXTS["start-title"], True, COLORS["bg1"])
            title = FONTS[0].render(TEXTS["start-title"], True, COLORS["bg"])
            text_rect = title.get_rect(center=(self.w / 2, TITLE_HEIGHT))
            self.screen.blit(title, text_rect)

            self.button_rects = {}

            self.button_rects["start"] = self.draw_button("Start game", 200,1)
            self.button_rects["setting"] = self.draw_button("Setting", 300, 2)
            self.button_rects["quit"] = self.draw_button("Quit", 365, 3)

        elif self.win_status == "start":
            pass  # into game

        elif self.win_status == "setting":
            pass



    def get_clicked_button(self, event):
        for bt_name in self.button_rects:
            bt_rect = self.button_rects[bt_name]
            if bt_rect.collidepoint(event.pos):
                return bt_name

        return ""

    def handle_button(self, bt_name):
        if bt_name == "start":
            self.win_status = "start"
        elif bt_name == "setting":
            self.win_status = "setting"
        elif bt_name == "quit":
            pygame.quit()
            sys.exit()

    def run(self):
        while True:
            self.count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    bt_name = self.get_clicked_button(event)
                    self.handle_button(bt_name)

            self.draw_all()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    menu = Menu()
    menu.run()



