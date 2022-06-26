import pygame, pgzero, pgzrun

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
                 design, type):
        self.design = design
        self.type = type

        if self.type == "rect":
            self.x = design[0]
            self.y = design[1]
            self.width = design[2]
            self.height = design[3]
            self.fill_colour = design[4]
            self.text = design[5]
            self.text_colour = design[6]

        elif self.type == "img":
            self.image = design[0]
            self.x = design[1]
            self.y = design[2]
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            #
            # print(self.width, self.height)
            # print((self.x - (self.width / 2)), self.x, (self.x + (self.width / 2)))
            # print((self.y - (self.height / 2)), self.y, (self.y + (self.height / 2)))


    def draw(self):
        if self.type == "rect":
            draw_rect(self.x, self.y,
                      self.width, self.height,
                      self.fill_colour,
                      None)
            show_text(self.text,
                      (self.x - int(self.width/2), self.y - int(self.height/5), self.width, self.height/2),
                      self.text_colour)
        elif self.type == "img":
            draw_image(self.image, self.x - int(self.width/2), self.y - int(self.height/2))


    def call(self):
        print(mouse_x + self.width, mouse_y + self.width)
        print((self.x - (self.width / 2)), self.x, (self.x + (self.width / 2)))
        print((self.y - (self.height / 2)), self.y, (self.y + (self.height / 2)))

        if (self.x - (self.width / 2)) < mouse_x + self.width < (self.x + (self.width / 2)) \
                and (self.y - (self.height / 2)) < mouse_y + self.width < (self.y + (self.height / 2)):
            print("hi")
            self.command()

        print(":::::::::::::::::::::::::::::::::")



    def command(self):
        if self.image == images.black:
            self.image = images.white
        else:
            self.image = images.black
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.draw()



buttons = []
active_button = -1

buttons.append(Button((images.black, 420, 290), "img")
               )


def draw():
    screen.fill("grey")

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
