import pygame
import time
import constants

pygame.init()
screen = pygame.display.set_mode(constants.SCREEN)
clock = pygame.time.Clock()
running = True

game_state = [["", "", ""], ["", "", ""], ["", "", ""]]


def winning(m):
    if (
        (
            game_state[0][0] == game_state[0][1]
            and game_state[0][1] == game_state[0][2]
            and game_state[0][2] != ""
        )
        or (
            game_state[1][0] == game_state[1][1]
            and game_state[1][1] == game_state[1][2]
            and game_state[1][2] != ""
        )
        or (
            game_state[2][0] == game_state[2][1]
            and game_state[2][1] == game_state[2][2]
            and game_state[2][2] != ""
        )
        or (
            game_state[0][0] == game_state[1][0]
            and game_state[1][0] == game_state[2][0]
            and game_state[2][0] != ""
        )
        or (
            game_state[0][1] == game_state[1][1]
            and game_state[1][1] == game_state[2][1]
            and game_state[2][1] != ""
        )
        or (
            game_state[0][2] == game_state[1][2]
            and game_state[1][2] == game_state[2][2]
            and game_state[2][2] != ""
        )
        or (
            game_state[0][0] == game_state[1][1]
            and game_state[1][1] == game_state[2][2]
            and game_state[2][2] != ""
        )
        or (
            game_state[0][2] == game_state[1][1]
            and game_state[1][1] == game_state[2][0]
            and game_state[2][0] != ""
        )
    ):
        if m % 2 == 0:
            print("x won")
            return "X"

        else:
            print("o won")
            return "O"

    elif m == 9:
        return "Draw"
    else:
        return None


k = 1
font = pygame.font.SysFont("Arial", 54)


c = True
while running:
    # date boyd
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            g = pygame.mouse.get_pos()
            position_x = int((g[0] - constants.FRAME_X) / constants.box_width)
            position_y = int((g[1] - constants.FRAME_Y) / constants.box_height)
            print(position_x, position_y)
            if game_state[position_y][position_x] == "":
                if k % 2 == 0:
                    print("x turn")
                    game_state[position_y][position_x] = "X"

                else:
                    print("o turn")

                    game_state[position_y][position_x] = "O"

                k += 1
    screen.fill(constants.back_colour)

    for i in range(len(game_state)):
        for j in range(len(game_state[i])):
            Y = i * constants.box_height + constants.FRAME_Y
            X = j * constants.box_width + constants.FRAME_X
            # print(X, Y)
            pygame.draw.rect(
                screen,
                constants.color,
                pygame.Rect(
                    X,
                    Y,
                    constants.box_width,
                    constants.box_height,
                ),
                2,
            )

            if game_state[i][j] != "":
                text = font.render(
                    game_state[i][j],
                    True,
                    constants.green,
                )
                screen.blit(
                    text,
                    (
                        X + constants.box_width / 2 - text.get_width() / 2,
                        Y + constants.box_height / 2 - text.get_height() / 2,
                    ),
                )

    pygame.display.flip()
    result = winning(k - 1)
    if result != None:
        pygame.draw.rect(
            screen,
            constants.back_colour,
            pygame.Rect(0, 0, constants.SCREEN[0], constants.SCREEN[1]),
        )
        text = font.render(
            f"{result} {('Won' if result != 'Draw' else '')}", True, constants.color
        )
        screen.blit(
            text,
            (
                constants.SCREEN[0] / 2 - text.get_width() / 2,
                constants.SCREEN[1] / 2 - text.get_height() / 2,
            )
            # pygame.Rect(
            #     (constants.SCREEN[0] - 240) / 2, (constants.SCREEN[1] - 100 / 2), 240, 100
            # )
        )
        pygame.display.flip()
        time.sleep(3)
        game_state = [["", "", ""], ["", "", ""], ["", "", ""]]
        k = 1
        # running = result == None
    clock.tick(60)
pygame.quit()
