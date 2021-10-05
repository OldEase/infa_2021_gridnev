import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))


def ghost_head(
        screen_for_place,
        proportion_x, proportion_y,
        color
        ):
    '''
    Function for drawing ghost's head
    screen_for_place - surface for '''
    pygame.draw.ellipse(
        screen_for_place,
        color,
        (
            proportion_x, 0,
            4 * proportion_x, 6 * proportion_y
        )
    )


def ghost_body(
        place,
        color,
        proportion_x, proportion_y
        ):
    pygame.draw.polygon(
        place,
        color,
        [
            (proportion_x, 3 * proportion_y),
            (0, 9 * proportion_y),
            (proportion_x, 8 * proportion_y),
            (2 * proportion_x, 10 * proportion_y),
            (2 * proportion_x, 7 * proportion_y),
            (3 * proportion_x, 9 * proportion_y),
            (3 * proportion_x, 8 * proportion_y),
            (4 * proportion_x, 10 * proportion_y),
            (4 * proportion_x, 8 * proportion_y),
            (5 * proportion_x, 9 * proportion_y),
            (5 * proportion_x, 8 * proportion_y),
            (6 * proportion_x, 10 * proportion_y),
            (5 * proportion_x, 3 * proportion_y)
        ]
    )  # тело


def ghost_orient(
        place,
        proportion_x, proportion_y,
        color_eye,
        side
        ):
    if side == 1:  # лицо если смотрит налево
        pygame.draw.ellipse(
            place,
            color_eye,
            (
                7 * proportion_x / 4, 2 * proportion_y,
                proportion_x / 2, proportion_y
            )
        )
        pygame.draw.ellipse(
            place,
            (0, 0, 0, 200),
            (
                7 * proportion_x / 4, 2 * proportion_y,
                proportion_x / 2, proportion_y
            ),
            2
        )
        pygame.draw.ellipse(
            place,
            color_eye,
            (
                11 * proportion_x / 4, 2 * proportion_y,
                proportion_x / 2, proportion_y
            )
        )
        pygame.draw.ellipse(
            place,
            (0, 0, 0, 200),
            (
                11 * proportion_x / 4, 2 * proportion_y,
                proportion_x / 2, proportion_y
            ),
            2
        )
        pygame.draw.lines(
            place,
            (0, 0, 0, 200),
            False,
            [
                [2 * proportion_x, 7 * proportion_y / 2],
                [2.25 * proportion_x, 4 * proportion_y],
                [2.5 * proportion_x, 3.75 * proportion_y],
                [2.75 * proportion_x, 4 * proportion_y],
                [3 * proportion_x, 3.5 * proportion_y]
            ],
            2
        )
    elif side == 0:  # лицо если смотрит направо
        pygame.draw.ellipse(
            place,
            color_eye,
            (
                proportion_x + 7 * proportion_x / 4, 2 * proportion_y,
                proportion_x / 2, proportion_y
            )
        )
        pygame.draw.ellipse(
            place,
            (0, 0, 0, 200),
            (
                proportion_x + 7 * proportion_x / 4,
                2 * proportion_y, proportion_x / 2,
                proportion_y
            ),
            2
        )
        pygame.draw.ellipse(
            place,
            color_eye,
            (
                proportion_x + 11 * proportion_x / 4,
                2 * proportion_y, proportion_x / 2,
                proportion_y
            )
        )
        pygame.draw.ellipse(
            place,
            (0, 0, 0, 200),
            (
                proportion_x + 11 * proportion_x / 4,
                2 * proportion_y, proportion_x / 2,
                proportion_y
            ),
            2
        )
        pygame.draw.lines(
            place,
            (0, 0, 0, 200),
            False,
            [
                [proportion_x + 2 * proportion_x, 7 * proportion_y / 2],
                [proportion_x + 2.25 * proportion_x, 4 * proportion_y],
                [proportion_x + 2.5 * proportion_x, 3.75 * proportion_y],
                [proportion_x + 2.75 * proportion_x, 4 * proportion_y],
                [proportion_x + 3 * proportion_x, 3.5 * proportion_y]
            ],
            2
        )


def ghost(
        screen_for_place,
        x_coordinate, y_coordinate,
        start_proportion_x, start_proportion_y,
        side,
        color_body,
        color_eye
        ):  # призрак side выбирает направление взгляда :1 налево, 0 направо

    proportion_x = start_proportion_x / 6
    proportion_y = start_proportion_y / 10

    place = pygame.Surface((start_proportion_x, start_proportion_y),
                           pygame.SRCALPHA)  # создаем полупрозрачную область для каждого призрака

    ghost_head(
        place,
        proportion_x,
        proportion_y,
        color_body
    )

    ghost_body(
        place,
        color_body,
        proportion_x,
        proportion_y
    )

    ghost_orient(
        place,
        proportion_x,
        proportion_y,
        color_eye,
        side
    )

    screen_for_place.blit(place, (x_coordinate, y_coordinate))


def cloud(
        color,
        x_start, y_start,
        x_size, y_size
        ):  # облако
    pygame.draw.ellipse(
        screen,
        color,
        (
            x_start, y_start,
            x_size, y_size
        )
    )


def house_body(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_body
        ):
    pygame.draw.rect(
        screen_for_place,
        color_body,
        (
            x_start, y_start,
            x_size, y_size
        )
    )


def house_window_left(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_window_left
        ):
    pygame.draw.rect(
        screen_for_place,
        color_window_left,
        (
            (x_start + x_size / 13), (y_start + 3 * y_size / 7),
            ((3 * x_size) / 13), (y_size / 3)
        )
    )


def house_window_middle(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_window_middle
        ):
    pygame.draw.rect(
        screen_for_place,
        color_window_middle,
        (
            (x_start + 5 * x_size / 13), (y_start + 3 * y_size / 7),
            (3 * x_size / 13), (y_size / 3)
        )
    )


def house_window_right(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_window_right
        ):
    pygame.draw.rect(
        screen_for_place,
        color_window_right,
        (
            (x_start + 9 * x_size / 13), (y_start + 3 * y_size / 7),
            (3 * x_size / 13), (y_size / 3)
        )
    )


def house_horizontal_impost(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    pygame.draw.line(
        screen_for_place,
        color,
        (
            (x_start + x_size / 13),
            (y_start + 3 * y_size / 7 + y_size / 6)
        ),
        (
            (x_start + 12 * x_size / 13),
            (y_start + 3 * y_size / 7 + y_size / 6)
        ),
        3
    )


def house_vertical_impost(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    for i in range(3):  # вертикальные импосты
        pygame.draw.line(
            screen_for_place,
            color,
            (
                (x_start + (5 + 8 * i) * x_size / 26),
                (y_start + 3 * y_size / 7)
            ),
            (
                (x_start + (5 + 8 * i) * x_size / 26),
                (y_start + y_size / 3 + 3 * y_size / 7)
            ),
            3
        )


def house_impost(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    house_horizontal_impost(screen_for_place, x_start, y_start, x_size, y_size, color)
    # горизонтальный импост для нижних окон
    house_vertical_impost(screen_for_place, x_start, y_start, x_size, y_size, color)
    # вертикальный импост для нижних окон


def house_balcony_window(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    pygame.draw.rect(
        screen_for_place,
        color,
        (
            (x_start + x_size / 5), (y_start + y_size / 20),
            (3 * x_size / 5), (5 * y_size / 30)
        )
    )


def house_balcony_circuit(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    pygame.draw.rect(
        screen_for_place,
        color,
        (
            (x_start + x_size / 10), (y_start + y_size / 10),
            (4 * x_size / 5), (y_size / 6)
        ),
        3
    )


def house_balcony_lattice(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    for i in range(10):  # перекладины балкончика
        pygame.draw.line(
            screen_for_place,
            color,
            (
                (x_start + x_size / 10 + i * (4 * x_size / 5) / 10),
                (y_start + y_size / 10)
            ),
            (
                (x_start + x_size / 10 + i * (4 * x_size / 5) / 10),
                (y_size / 6 + y_start + y_size / 10)
            ),
            3
        )


def house_balcony(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    house_balcony_circuit(screen_for_place, x_start, y_start, x_size, y_size, color)

    house_balcony_lattice(screen_for_place, x_start, y_start, x_size, y_size, color)


def house_roof(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    pygame.draw.polygon(
        screen_for_place,
        color,
        [
            (x_start - x_size / 10, y_start),
            (x_size + x_start + x_size / 10, y_start),
            (x_size + x_start - x_size / 10, y_start - y_size / 10),
            (x_start + x_size / 10, y_start - y_size / 10)
        ]
    )


def house_pipe_left(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    pygame.draw.rect(
        screen_for_place,
        color,
        (
            (x_start + x_size / 5), (y_start - y_size / 5),
            (x_size / 10), (y_size / 10)
        )
    )


def house_pipe_right(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    pygame.draw.rect(
        screen_for_place,
        color,
        (
            (x_start + 2 * x_size / 5), (y_start - y_size / 5),
            (x_size / 10), (y_size / 10)
        )
    )


def house_pipes(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    house_pipe_right(screen_for_place, x_start, y_start, x_size, y_size, color)
    house_pipe_left(screen_for_place, x_start, y_start, x_size, y_size, color)


def house(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_body, color_window_left,
        color_window_middle, color_window_right,
        color_window_up, color_balcony, color_roof, color_pipe
        ):  # отрисовка дома
    house_body(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_body
    )
    house_window_left(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_window_left
    )
    # левое нижнее окно
    house_window_middle(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_window_middle
    )
    # среднее нижнее окно
    house_window_right(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_window_right
    )
    # правое нижнее окно
    house_impost(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_body
    )
    # импосты окон
    house_balcony_window(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_window_up
    )
    # верхнее окно
    house_balcony(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_balcony
    )
    # контур балкончика
    house_roof(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_roof
    )
    # крыша
    house_pipes(
        screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color_pipe
    )
    # трубы


def sky(screen_for_place,
        x_start, y_start,
        x_size, y_size,
        color
        ):
    pygame.draw.rect(
        screen_for_place,
        color,
        (x_start, y_start,
         x_size, y_size,)
    )  # небо


def moon(screen_for_place,
         x_start, y_start,
         radius,
         color
         ):
    pygame.draw.circle(
        screen_for_place,
        color,
        (x_start, y_start),
        radius
    )


sky(
    screen,
    0, 0,
    400, 250,
    (130, 130, 130)
)
moon(
    screen,
    350, 50, 
    35,
    (255, 255, 255)
)
cloud(
    (50, 50, 50),
    100, 50,
    300, 60
)
cloud(
    (40, 40, 40),
    50, 100,
    250, 50
)
cloud(
    (80, 80, 80),
    150, 20,
    150, 50
)
cloud(
    (70, 70, 70),
    150, 150,
    250, 50
)
cloud(
    (40, 40, 40),
    20, 170,
    180, 50
)
house(
    screen,
    140, 150,
    100, 140,
    (70, 0, 0), (0, 0, 50),
    (250, 240, 0), (0, 0, 50),
    (250, 240, 0), (0, 0, 100),
    (255, 0, 0), (100, 0, 0)
)
house(
    screen,
    10, 300,
    170, 220,
    (70, 0, 0), (250, 240, 0),
    (0, 0, 50), (0, 0, 50),
    (0, 0, 50), (0, 0, 0),
    (40, 0, 0), (40, 0, 0)
)
house(
    screen,
    310, 180,
    120, 160,
    (70, 0, 0), (250, 240, 0),
    (0, 0, 50), (250, 240, 0),
    (250, 240, 0), (0, 0, 0),
    (40, 0, 0), (40, 0, 0)
)
ghost(
    screen,
    30, 430,
    90, 140,
    0,
    (
        255, 255,
        255, 160
    ),
    (
        230, 0,
        0, 200
    )
)
ghost(
    screen,
    190, 260,
    80, 120,
    0,
    (0, 200, 100, 160),
    (230, 0, 0, 200)
)
ghost(
    screen,
    150, 300,
    80, 120,
    1,
    (0, 200, 100, 160),
    (230, 0, 0, 200)
)
ghost(
    screen,
    250, 200,
    40, 70,
    1,
    (0, 200, 100, 160),
    (230, 0, 0, 200)
)
ghost(
    screen,
    100, 150,
    40, 70,
    0,
    (0, 200, 100, 160),
    (230, 0, 0, 200)
)
ghost(
    screen,
    200, 300,
    400, 600,
    1,
    (0, 200, 100, 160),
    (230, 0, 0, 200)
)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
