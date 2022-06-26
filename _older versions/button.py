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
    def __init__(self, x, y,
                 width, height,
                 colour, text,
                 code):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.fill_colour = colour

        self.text = text
        self.text_colour = "white"

        self.code = code


    def draw(self):
        draw_rect(self.x, self.y,
                  self.width, self.height,
                  self.fill_colour,
                  None)
        show_text(self.text,
                  (self.x - int(self.width/2), self.y - int(self.height/5), self.width, self.height/2),
                  self.text_colour)


    def call(self):
        global active_button

        if (self.x - (self.width / 2)) < mouse_x < (self.x + (self.width / 2)) \
                and (self.y - (self.height / 2)) < mouse_y < (self.y + (self.height / 2)):
            active_button = self.code
            self.command()


    def command(self):
        global buttons

        if active_button >= 0:
            self.text = "you clicked me!"
            self.text_colour = "blue"


buttons = []
active_button = -1

buttons.append(Button(0, 290, 400, 120, "black", "click me!", 0)
               )
buttons.append(Button(420, 290, 400, 120, "black", "click me!", 1)
               )
buttons.append(Button(840, 290, 400, 120, "black", "click me!", 2)
               )
buttons.append(Button(0, 130, 400, 120, "black", "click me!", 3)
               )
buttons.append(Button(420, 130, 400, 120, "black", "click me!", 4)
               )
buttons.append(Button(840, 130, 400, 120, "black", "click me!", 5)
               )
buttons.append(Button(0, 450, 400, 120, "black", "click me!", 6)
               )
buttons.append(Button(420, 450, 400, 120, "black", "click me!", 7)
               )
buttons.append(Button(840, 450, 400, 120, "black", "click me!", 8)
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
