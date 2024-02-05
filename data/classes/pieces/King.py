import pygame

from data.classes.Piece import Piece


class King(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color)

        img_path = 'data/images/' + color[0] + 'King.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 10, board.tile_height - 10))

        self.char = 'K'

    def get_possible_moves(self, board):
        output = []
        moves = [
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
        ]

        for move in moves:
            new_pos = (self.x + move[0], self.y + move[1])
            if 0 <= new_pos[0] < 8 and 0 <= new_pos[1] < 8:
                output.append([board.get_square_from_pos(new_pos)])

        return output

    def can_castle(self, board):
        if not self.has_moved:
            if self.color == 'white':
                queenside_rook = board.get_piece_from_pos((0, 7))
                kingside_rook = board.get_piece_from_pos((7, 7))
                if queenside_rook != None:
                    if not queenside_rook.has_moved and not board.is_in_check('white', board_change=[self.pos, (2, 7)]):
                        if [board.get_piece_from_pos((i, 7)) for i in range(1, 4)] == [None, None,
                                                                                       None] and not board.is_in_check:
                            return 'queenside'
                if kingside_rook != None:
                    if not kingside_rook.has_moved and not board.is_in_check('white', board_change=[self.pos, (6, 7)]):
                        if [board.get_piece_from_pos((i, 7)) for i in range(5, 7)] == [None,
                                                                                       None] and not board.is_in_check:
                            return 'kingside'

            elif self.color == 'black':
                queenside_rook = board.get_piece_from_pos((0, 0))
                kingside_rook = board.get_piece_from_pos((7, 0))
                if queenside_rook != None:
                    if not queenside_rook.has_moved and not board.is_in_check('black', board_change=[self.pos, (2, 0)]):
                        if [board.get_piece_from_pos((i, 0)) for i in range(1, 4)] == [None, None,
                                                                                       None] and not board.is_in_check:
                            return 'queenside'
                if kingside_rook != None:
                    if not kingside_rook.has_moved and not board.is_in_check('black', board_change=[self.pos, (6, 0)]):
                        if [board.get_piece_from_pos((i, 0)) for i in range(5, 7)] == [None,
                                                                                       None] and not board.is_in_check:
                            return 'kingside'

    def get_valid_moves(self, board):
        output = []
        for square in self.get_moves(board):
            if not board.is_in_check(self.color, board_change=[self.pos, square.pos]):
                output.append(square)

        if self.can_castle(board) == 'queenside':
            output.append(board.get_square_from_pos((self.x - 2, self.y)))
        if self.can_castle(board) == 'kingside':
            output.append(board.get_square_from_pos((self.x + 2, self.y)))

        return output
