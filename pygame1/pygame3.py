import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))


def ghost(x_coordinate, y_coordinate, start_proportion_x, start_proportion_y, side, color_body):  # призрак side выбирает направление взгляда :1 налево, 0 направо

    proportion_x = start_proportion_x / 6
    proportion_y = start_proportion_y / 10
    place = pygame.Surface((start_proportion_x, start_proportion_y), pygame.SRCALPHA)  # создаем полупрозрачную область для каждого призрака
    pygame.draw.ellipse(
                        place,
                        color_body,
                        (
                         proportion_x, 0,
                         4 * proportion_x, 6 * proportion_y
                        )
    )  # голова
    pygame.draw.polygon(
                        place,
                        color_body,
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
    if side == 1:  # лицо если смотрит налево
        pygame.draw.ellipse(
                            place,
                            (230, 0, 0, 200),
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
                            (230, 0, 0, 200),
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
                            (230, 0, 0, 200),
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
                            (230, 0, 0, 200),
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

    screen.blit(place, (x_coordinate, y_coordinate))


def cloud(color, x_start, y_start, x_size, y_size):  # облако
    pygame.draw.ellipse(screen, color, (x_start, y_start, x_size, y_size))


def house(x_start, y_start, x_size, y_size):  # отрисовка дома
    pygame.draw.rect(
                     screen,
                     (70, 0, 0),
                     (
                      x_start, y_start,
                      x_size, y_size
                     ),
                     0
    )  # корпус дома
    pygame.draw.rect(
                     screen,
                     (0, 0, 50),
                     (
                      (x_start + x_size / 13), (y_start + 3 * y_size / 7),
                      ((3 * x_size) / 13), (y_size / 3)
                     ),
                     0
    )  # левое нижнее окно
    pygame.draw.rect(
                     screen,
                     (0, 0, 50),
                     (
                      (x_start + 5 * x_size / 13), (y_start + 3 * y_size / 7),
                      (3 * x_size / 13), (y_size / 3)
                     ),
                     0
    )  # среднее нижнее окно
    pygame.draw.rect(
                     screen,
                     (250, 240, 0),
                     (
                      (x_start + 9 * x_size / 13), (y_start + 3 * y_size / 7),
                      (3 * x_size / 13), (y_size / 3)
                     ),
                     0
    )  # правое нижнее окно
    pygame.draw.line(
                     screen,
                     (70, 0, 0),
                     (
                      (x_start + x_size / 13),
                      (y_start + 3 * y_size / 7 + y_size / 6)
                     ),
                     (
                      (x_start + 12 * x_size / 13),
                      (y_start + 3 * y_size / 7 + y_size / 6)
                     ),
                     3
    )  # горизонтальный импост для нижних окон
    for i in range(3):  # вертикальные импосты
        pygame.draw.line(
                         screen,
                         (70, 0, 0),
                         (
                          (x_start + (5 + 8 * i) * x_size / 26),
                          (y_start + 3 * y_size / 7)
                         ),
                         (
                          (x_start + (5 + 8 * i) * x_size / 26),
                          (y_start + y_size / 3 + 3 * y_size / 7)
                         ),
                         3
        )  #

    pygame.draw.rect(screen, (250, 240, 0), ((x_start + x_size / 5), (y_start + y_size / 20), (3 * x_size / 5), (5 * y_size / 30)), 0)  # верхнее окно
    pygame.draw.rect(screen, (0, 0, 0), ((x_start + x_size / 10), (y_start + y_size / 10), (4 * x_size / 5), (y_size / 6)), 3)  # кортур балкончика
    for i in range(10):  # перекладины балкончика
        pygame.draw.line(screen, (0, 0, 0), ((x_start + x_size / 10 + i * (4 * x_size / 5) / 10), (y_start + y_size / 10)),
                         ((x_start + x_size / 10 + i * (4 * x_size / 5) / 10), (y_size / 6 + y_start + y_size / 10)), 3)
    pygame.draw.polygon(screen, (40, 0, 0),
                        [[x_start - x_size / 10, y_start], [x_size + x_start + x_size / 10, y_start], [x_size + x_start - x_size / 10, y_start - y_size / 10],
                         [x_start + x_size / 10, y_start - y_size / 10]])  # крыша
    pygame.draw.rect(screen, (40, 0, 0), ((x_start + x_size / 5), (y_start - y_size / 5), (x_size / 10), (y_size / 10)), 0)  # труба 1
    pygame.draw.rect(screen, (40, 0, 0), ((x_start + 2 * x_size / 5), (y_start - y_size / 5), (x_size / 10), (y_size / 10)), 0)  # труба 2


pygame.draw.rect(screen, (130, 130, 130), (0, 0, 400, 250), 0)  # небо
pygame.draw.circle(screen, (255, 255, 255), (350, 50), 35, 0)  # луна
cloud((50, 50, 50), 100, 50, 300, 60)
cloud((40, 40, 40), 50, 100, 250, 50)
cloud((80, 80, 80), 150, 20, 150, 50)
cloud((70, 70, 70), 150, 150, 250, 50)
cloud((40, 40, 40), 20, 170, 180, 50)
house(140, 150, 100, 140)
house(10, 300, 170, 220)
house(310, 180, 120, 160)
ghost(30, 430, 90, 140, 0, (255, 255, 255, 160))
ghost(190, 260, 80, 120, 0, (0, 200, 100, 160))
ghost(150, 300, 80, 120, 1, (0, 200, 100, 160))
ghost(250, 200, 40, 70, 1, (0, 200, 100, 160))
ghost(100, 150, 40, 70, 0, (0, 200, 100, 160))
ghost(200, 300, 400, 600, 1, (0, 200, 100, 160))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
