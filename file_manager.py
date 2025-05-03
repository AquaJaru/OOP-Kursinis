from piece import Piece
from piece_factory import PieceFactory

class FileManager:
    @staticmethod
    def save_game(board, filename="savegame.txt"):
        with open(filename, 'w') as file:
            for row in range(8):
                for col in range(8):
                    piece = board.grid[row][col]
                    if piece:
                        file.write(f"{piece.get_color()},{row},{col}\n")

    @staticmethod
    def load_game(board, piece_factory, filename="savegame.txt"):
        board.grid = [[None for _ in range(8)] for _ in range(8)]
        
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    color, row, col = parts
                    row = int(row)
                    col = int(col)
                    piece = piece_factory.create_piece(color, (row, col))
                    board.place_piece(piece)