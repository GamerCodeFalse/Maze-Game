import pygame
import pygame as game
import numpy

width = 800
height = 800
size = 80


def setup():
    setup.title = "A* Algorithm"
    try:
        print("Project run is Successful!\n")
        print("Pygame project", setup.title, "is starting")
    except ImportError or FileNotFoundError:
        print("Project run is failed!")
        print(ImportError)
    setup.screen = game.display.set_mode((width, height))
    setup.run = True
    game.display.set_caption(setup.title)
    setup.screen.fill((255, 255, 255))
    game.init()


def draw():
    draw.x = (2 * size) + 10
    draw.y = (1 * size) + 10
    while setup.run:
        for event in game.event.get():
            if event.type == game.QUIT:
                setup.run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                draw.x -= size
            if keys[pygame.K_RIGHT]:
                draw.x += size
            if keys[pygame.K_UP]:
                draw.y -= size
            if keys[pygame.K_DOWN]:
                draw.y += size
        if draw.y < 0:
            draw.x = (2 * size) + 10
            draw.y = (1 * size) + 10
        if draw.y >= height:
            draw.x = (2 * size) + 10
            draw.y = (1 * size) + 10
        if draw.x < 0:
            draw.x = (2 * size) + 10
            draw.y = (1 * size) + 10
        if draw.x >= width:
            draw.x = (2 * size) + 10
            draw.y = (1 * size) + 10
        if draw.x == 570 and draw.y == 730:
            print("You Win!")
            setup.run = False
        setup.screen.fill((255, 255, 255))
        draw_start_point(2, 1)
        draw_end_point(7, 9)
        draw_player(draw.x, draw.y)
        draw_wall(1, 1, draw.x, draw.y)
        draw_wall(1, 2, draw.x, draw.y)
        draw_wall(2, 2, draw.x, draw.y)
        draw_wall(3, 2, draw.x, draw.y)
        draw_wall(3, 1, draw.x, draw.y)
        draw_wall(3, 0, draw.x, draw.y)
        draw_wall(6, 2, draw.x, draw.y)
        draw_wall(6, 1, draw.x, draw.y)
        draw_wall(7, 2, draw.x, draw.y)
        draw_wall(7, 1, draw.x, draw.y)
        draw_wall(6, 8, draw.x, draw.y)
        draw_wall(6, 7, draw.x, draw.y)
        draw_wall(6, 6, draw.x, draw.y)
        draw_wall(6, 5, draw.x, draw.y)
        draw_wall(7, 5, draw.x, draw.y)
        draw_wall(8, 5, draw.x, draw.y)
        draw_wall(9, 5, draw.x, draw.y)
        draw_wall(0, 6, draw.x, draw.y)
        draw_wall(1, 6, draw.x, draw.y)
        draw_wall(2, 6, draw.x, draw.y)
        draw_wall(3, 6, draw.x, draw.y)
        draw_wall(4, 6, draw.x, draw.y)
        draw_wall(4, 7, draw.x, draw.y)
        draw_wall(4, 8, draw.x, draw.y)
        draw_grid()
        game.display.update()


def draw_grid():
    for i in range(int(width/size)):
        for j in range(int(height/size)):
            game.draw.rect(setup.screen, (25, 25, 25), [i*size, j*size, size, 10])
            game.draw.rect(setup.screen, (25, 25, 25), [i * size, j * size, 10, size])


def draw_start_point(x, y):
    x_ = (x*size)+10
    y_ = (y*size)+10
    game.draw.rect(setup.screen, (0, 255, 0), [x_, y_, size-10, size-10])


def draw_end_point(x, y):
    x_ = (x*size)+10
    y_ = (y*size)+10
    game.draw.rect(setup.screen, (255, 0, 0), [x_, y_, size-10, size-10])


def draw_wall(x, y, player_x, player_y):
    draw_wall.x_ = (x*size)+10
    draw_wall.y_ = (y*size)+10
    game.draw.rect(setup.screen, (0, 0, 0), [draw_wall.x_, draw_wall.y_, size-10, size-10])
    if player_x == draw_wall.x_ and player_y == draw_wall.y_:
        print("Oops you hit a wall!")
        draw.x = (2 * size) + 10
        draw.y = (1 * size) + 10


def draw_player(x, y):
    draw_player.x = x
    draw_player.y = y
    game.draw.rect(setup.screen, (0, 0, 255), (draw_player.x, draw_player.y, size, size))


def run():
    setup()
    draw()


if __name__ == '__main__':
    run()
