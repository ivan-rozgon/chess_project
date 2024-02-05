import os
import sys

import pygame

from data.classes.Board import Board

pygame.init()

geometry = (600, 600)
screen = pygame.display.set_mode(geometry)
board = Board(geometry[0], geometry[1])


def load_image(name):
    fullname = os.path.join('data/images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def draw(scr):
    scr.fill('white')
    board.draw(scr)
    if board.is_in_checkmate('black'):
        img = load_image('white_win.jpg')
        img1 = pygame.transform.scale(img, (400, 400))
        screen.blit(img1, (100, 100))

        # running = False
    elif board.is_in_checkmate('white'):
        img = load_image('black_win.jpg')
        img1 = pygame.transform.scale(img, (400, 400))
        screen.blit(img1, (100, 100))

    pygame.display.update()


if __name__ == '__main__':
    running = True
    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.handle_click(mouse_x, mouse_y)

        if board.is_in_checkmate('black'):
            img = load_image('white_win.jpg')
            screen.blit(img, (10, 10))

            #running = False
        elif board.is_in_checkmate('white'):
            img = load_image('black_win.jpg')
            screen.blit(img, (10, 10))

            #running = False

        draw(screen)
