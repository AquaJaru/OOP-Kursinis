from piece import Piece


class PieceFactory:
    @staticmethod
    def create_piece(color, position):
        return Piece(color, position)