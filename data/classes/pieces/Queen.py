import pygame

from data.classes.Piece import Piece


class Queen(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)

        img_path = 'data/images/' + color[0] + 'Queen.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 10, board.tile_height - 10))

        self.char = 'Q'

    def get_possible_moves(self, board):
        all_moves = []

        moves_upwards = []
        for y in range(self.y)[::-1]:
            moves_upwards.append(board.get_square_from_pos(
                (self.x, y)
            ))
        all_moves.append(moves_upwards)

        moves_upwards_right = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y - i < 0:
                break
            moves_upwards_right.append(board.get_square_from_pos(
                (self.x + i, self.y - i)
            ))
        all_moves.append(moves_upwards_right)

        moves_right = []
        for x in range(self.x + 1, 8):
            moves_right.append(board.get_square_from_pos(
                (x, self.y)
            ))
        all_moves.append(moves_right)

        moves_downwards_right = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y + i > 7:
                break
            moves_downwards_right.append(board.get_square_from_pos(
                (self.x + i, self.y + i)
            ))
        all_moves.append(moves_downwards_right)

        moves_downwards = []
        for y in range(self.y + 1, 8):
            moves_downwards.append(board.get_square_from_pos(
                (self.x, y)
            ))
        all_moves.append(moves_downwards)

        moves_downwards_left = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y + i > 7:
                break
            moves_downwards_left.append(board.get_square_from_pos(
                (self.x - i, self.y + i)
            ))
        all_moves.append(moves_downwards_left)

        moves_left = []
        for x in range(self.x)[::-1]:
            moves_left.append(board.get_square_from_pos(
                (x, self.y)
            ))
        all_moves.append(moves_left)

        moves_upwards_left = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y - i < 0:
                break
            moves_upwards_left.append(board.get_square_from_pos(
                (self.x - i, self.y - i)
            ))
        all_moves.append(moves_upwards_left)

        return all_moves
