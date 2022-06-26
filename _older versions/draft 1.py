import pygame, pgzero, pgzrun

HEIGHT = 1050
WIDTH = 1980

top_left_x = 575
top_left_y = 550

background = "light grey"
TILE_SIZE = 180
GAP_SIZE = 40

mouse_pos = [0, 0]
mouse_x = mouse_pos[0]
mouse_y = mouse_pos[1]


def on_mouse_down(pos):
    global mouse_pos, mouse_x, mouse_y

    mouse_pos = pos
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]


class Button:
    def __init__(self,
                 design):

        self.design = design

        self.index = 0
        self.image = self.design[0]
        self.images = self.design[1]
        self.x = self.design[2]
        self.y = self.design[3]
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def draw(self):
        draw_image(self.image, self.x - int(self.width/2), self.y - int(self.height/2))


    def call(self):
        if (self.x - (self.width / 2)) < mouse_x + self.width + top_left_x/TILE_SIZE < (self.x + (self.width / 2)) \
                and (self.y - (self.height / 2)) < mouse_y + self.height + top_left_y/TILE_SIZE < (self.y + (self.height / 2)):
            self.command()

    def command(self):
        draw_rect(self.x - self.width, self.y - self.height, self.width, self.height, background, None)

        if self.images != self.design[0]:
            self.index += 1

            if self.index == len(self.images):
                self.index = 0

            self.image = self.images[self.index]

            self.draw()
        else:
            self.images = self.images[self.index]




buttons = []

for y in range(int(HEIGHT/2) - (TILE_SIZE + GAP_SIZE)*3 + top_left_y, int(HEIGHT/2) + (TILE_SIZE + GAP_SIZE)*0 + top_left_y, (TILE_SIZE + GAP_SIZE)):
    for x in range(int(WIDTH/2) - (TILE_SIZE + GAP_SIZE)*3 + top_left_x, int(WIDTH/2) + (TILE_SIZE + GAP_SIZE)*0 + top_left_x, (TILE_SIZE + GAP_SIZE)):
        buttons.append(Button((images.a, [images.x, images.o], x, y))
                       )

        # clock.schedule_interval(_older versions[len(_older versions) - 1].command, 0.1)


def draw():
    screen.fill(background)

    for x in range(2):
        draw_rect(top_left_x + 200*x + 270, top_left_y - 90, int(GAP_SIZE/2), 700, "white", None)
    for y in range(2):
        draw_rect(top_left_x + 355, top_left_y + 210*y - 205, 700, int(GAP_SIZE/2), "white", None)

    for button in buttons:
        button.draw()
        button.call()


def draw_image(image, x, y):
    screen.blit(image,
                (x - image.get_width(),
                 y - image.get_height()))


def draw_rect(x, y,
              width, height,
              colour="white",
              outline=None):
    if outline is not None:
        BOX2 = Rect((x - int(width / 2) - 2, y - int(height / 2) - 2),
                    (width + 4, height + 4)
                    )
        screen.draw.rect(BOX2, outline)

    if colour is not None:
        BOX = Rect((x - int(width / 2), y - int(height / 2)),
                   (width, height)
                   )
        screen.draw.filled_rect(BOX, colour)


def show_text(text_to_show, rect, colour):
    screen.draw.textbox(text_to_show, rect, color=colour)

pgzrun.go()
