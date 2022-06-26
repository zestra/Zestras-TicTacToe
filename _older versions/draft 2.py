import pygame, pgzero, pgzrun

HEIGHT = 1050
WIDTH = 1980

top_left_x = 575
top_left_y = 550

background = "light grey"
TILE_SIZE = 180
GAP_SIZE = 40

player = "o"

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
        global player, comment
        if (self.x - (self.width / 2)) < mouse_x + self.width + top_left_x/TILE_SIZE < (self.x + (self.width / 2)) \
                and (self.y - (self.height / 2)) < mouse_y + self.height + top_left_y/TILE_SIZE < (self.y + (self.height / 2)) \
                and self.image == images.a:
            if player == "o":
                player = "x"
            else:
                player = "o"

            self.command()

    def command(self):
        global comment
        draw_rect(self.x - self.width, self.y - self.height, self.width, self.height, background, None)

        if player == "o":
            self.image = images.o
            comment = "Player X turn."

        else:
            self.image = images.x
            comment = "Player O turn."

        self.draw()


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
        buttons[len(buttons) - 1].append(Button((images.a, [], x, y))
                       )


def read_board():
    global board

    board = []
    for row in buttons:
        board.append([])
        for button in row:
            if button.image == images.a:
                num = 0
            elif button.image == images.x:
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

    # If the game is already known as over, we need not check that it be over.
    if game_over:
        return

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
        first_column = board[row][0]
        for column in board[row]:
            if column != first_column:
                winner = None
                break
            else:
                winner = column

        if winner is not None and winner != 0:
            if winner == 1:
                comment = "Player X wins!"
            else:
                comment = "Player O wins!"

            game_over = True


    # Check vertical columns

    #      ____________________
    # rows |                  |
    #  0   |   |   | x |   |  |
    #  1   |   |   | x |   |  |
    #  2   |   |   | x |   |  |
    #      |__________________|
    #  columns   0   1   2

    for column in range(width):
        first_column = board[0][column]
        for row in range(height):
            if board[row][column] != first_column:
                winner = None
                break
            else:
                winner = board[row][column]

        if winner is not None and winner != 0:
            if winner == 1:
                comment = "Player X wins!"
            else:
                comment = "Player O wins!"

            game_over = True


    # Check that all the squares are not already filled.
    sum = 0
    for y in range(height):
        for x in range(width):
            sum += int(board[y][x])

    if sum == ((5*1) + (4*2)):
        # If so, the game has now ended.
        game_over = True
        comment = "TIE!"
        return


def draw():
    screen.fill(background)

    for x in range(2):
        draw_rect(top_left_x + 200*x + 270, top_left_y - 90, int(GAP_SIZE/2), 700, "white", None)
    for y in range(2):
        draw_rect(top_left_x + 355, top_left_y + 210*y - 205, 700, int(GAP_SIZE/2), "white", None)

    for row in buttons:
        for button in row:
            button.draw()
            if game_over is False:
                button.call()

    show_text(comment, int(top_left_x/2) - 80, int(top_left_y/2) + 20, "black", 75)


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


clock.schedule_interval(check, 0.01)

pgzrun.go()
