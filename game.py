import pygame, pgzero, pgzrun

HEIGHT = 1050
WIDTH = 1980

top_left_x = 575
top_left_y = 550

TILE_SIZE = 180
GAP_SIZE = 40

player = "o"

dict_images = {0: images.a,
               1: images.x,
               2: images.o}

height = 3
width = 3

mouse_pos = [0, 0]
mouse_x = mouse_pos[0]
mouse_y = mouse_pos[1]


def on_mouse_down(pos):
    global mouse_pos, mouse_x, mouse_y

    mouse_pos = pos
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]

    sounds.click.play()


class Button:
    def __init__(self,
                 design):

        self.design = design

        self.index = 0
        self.image = self.design[0]
        self.x = self.design[1]
        self.y = self.design[2]
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def draw(self):
        draw_image(self.image, self.x - int(self.width/2), self.y - int(self.height/2))


    def call(self):
        global player, comment

        if game_over:
            return

        if (self.x - (self.width / 2)) < mouse_x + self.width + top_left_x/TILE_SIZE < (self.x + (self.width / 2)) \
                and (self.y - (self.height / 2)) < mouse_y + self.height + top_left_y/TILE_SIZE < (self.y + (self.height / 2)) \
                and self.image == dict_images[0]:
            if player == "o":
                player = "x"
            else:
                player = "o"

            self.command()

    def command(self):
        global comment

        if player == "o":
            self.image = dict_images[2]
            comment = "Player X turn."

        else:
            self.image = dict_images[1]
            comment = "Player O turn."

        self.draw()
        check()

game_over = False
comment = "Player X turn."

board = []
for row in range(height):
    board.append([])
    for column in range(width):
        board[len(board) - 1].append(0)


buttons = []

for y in range(int(HEIGHT/2) - (TILE_SIZE + GAP_SIZE)*height + top_left_y, int(HEIGHT/2) + (TILE_SIZE + GAP_SIZE)*0 + top_left_y, (TILE_SIZE + GAP_SIZE)):
    buttons.append([])
    for x in range(int(WIDTH/2) - (TILE_SIZE + GAP_SIZE)*width + top_left_x, int(WIDTH/2) + (TILE_SIZE + GAP_SIZE)*0 + top_left_x, (TILE_SIZE + GAP_SIZE)):
        buttons[len(buttons) - 1].append(Button((dict_images[0], x, y))
                       )


def read_board():
    global board

    board = []
    for row in buttons:
        board.append([])
        for button in row:
            if button.image == dict_images[0]:
                num = 0
            elif button.image == dict_images[1]:
                num = 1
            else:
                num = 2
            board[len(board) - 1].append(num)

    # for row in range(len(board)):
    #     for column in range(len(board[0])):
    #         print(board[row][column], end=" ")
    #     print()
    # print("--------------- \n")


def check():
    global comment, game_over

    # Otherwise, proceed with the following checks.

    # Gather your info first.
    read_board()

    # ...
    winner = None

    # Check horizontal rows

    #      ____________________
    # rows |                  |
    #  0   |   |   |   |   |  |
    #  1   |   | x | x | x |  |
    #  2   |   |   |   |   |  |
    #      |__________________|
    #  columns   0   1   2

    for row in range(height):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            winner = board[row][0]


    # Check vertical columns

    #      ____________________
    # rows |                  |
    #  0   |   |   | x |   |  |
    #  1   |   |   | x |   |  |
    #  2   |   |   | x |   |  |
    #      |__________________|
    #  columns   0   1   2

    for column in range(width):
        if board[0][column] == board[1][column] == board[2][column] != 0:
            winner = board[0][column]


    # Check diagonals

    #      ____________________
    # rows |                  |
    #  0   |   | x |   | x |  |
    #  1   |   |   | x |   |  |
    #  2   |   | x |   | x |  |
    #      |__________________|
    #  columns   0   1   2

    if board[0][0] == board[1][1] == board[2][2] != 0 \
        or board[2][0] == board[1][1] == board[0][2] != 0:
        winner = board[1][1]

    # Check that all the squares are not already filled.
    all_filled = True
    for row in range(height):
        for column in range(width):
            if board[row][column] == 0:
                all_filled = False
                break
        if all_filled is False:
            break

    if winner is not None:
        if winner == 1:
            comment = "Player X wins!"
        if winner == 2:
            comment = "Player O wins!"
        game_over = True

    elif all_filled:
        comment = "Tie!"
        game_over = True


    # sum = 0
    # for y in range(height):
    #     for x in range(width):
    #         sum += int(board[y][x])
    #
    # if sum == ((5*1) + (4*2)):
    #     # If so, the game has now ended.
    #     game_over = True
    #     comment = "TIE!"
    #     return


def draw():
    draw_image(images.background, WIDTH, HEIGHT/2 + top_left_y - 20)

    for x in range(2):
        draw_rect(top_left_x + 200*x + 270, top_left_y - 90, int(GAP_SIZE/2), 700, "tan", None)
    for y in range(2):
        draw_rect(top_left_x + 355, top_left_y + 210*y - 205, 700, int(GAP_SIZE/2), "tan", None)

    for row in buttons:
        for button in row:
            button.draw()
            button.call()

    show_text(comment, int(top_left_x/2) - 80, int(top_left_y/2) + 20, "tan", 75)


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


def show_text(text_to_show, x, y,
              colour="white",
              size=75):
    screen.draw.text(text_to_show,
                     (top_left_x + x, top_left_y + y),
                     fontsize=size, color=colour)

pgzrun.go()
