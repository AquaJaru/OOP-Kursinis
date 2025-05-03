from board import Board
from player import Player
from piece_factory import PieceFactory
from file_manager import FileManager
from piece import Piece


class Game:
    def __init__(self):
        self.board = Board()
        self.factory = PieceFactory()
        self.players = [
            Player("Player 1", "white"),
            Player("Player 2", "black")
        ]
        self.current_player_index = 0

    def setup(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    piece = self.factory.create_piece("white", (row, col))
                    self.players[0].add_piece(piece)
                    self.board.place_piece(piece)

        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    piece = self.factory.create_piece("black", (row, col))
                    self.players[1].add_piece(piece)
                    self.board.place_piece(piece)

    def switch_turn(self):
        self.current_player_index = 1 - self.current_player_index

    def get_current_player(self):
        return self.players[self.current_player_index]

    def save(self):
        FileManager.save_game(self.board)

    def load(self):
        FileManager.load_game(self.board, self.factory)

    def input_move(self):
        while True:
            move = input("Enter your move (from_row from_col to_row to_col) or 'save': ").strip()
            if move.lower() == 'save':
                self.save()
                print("Game saved.")
                continue

            parts = move.split()
            if len(parts) != 4:
                print("Invalid input! Enter four numbers separated by spaces.")
                continue

            try:
                from_row, from_col, to_row, to_col = map(int, parts)
                return (from_row, from_col), (to_row, to_col)
            except ValueError:
                print("Invalid input! Make sure to enter numbers.")
                continue

    def is_capture_move(self, piece, to_pos):
        from_row, from_col = piece.position
        to_row, to_col = to_pos
        row_diff = to_row - from_row
        col_diff = to_col - from_col

        if abs(row_diff) == 2 and abs(col_diff) == 2:
            jumped_row = (from_row + to_row) // 2
            jumped_col = (from_col + to_col) // 2
            jumped_piece = self.board.grid[jumped_row][jumped_col]

            if jumped_piece and jumped_piece.get_color() != piece.get_color():
                return (jumped_row, jumped_col)   
        return None

    def validate_move(self, piece, to_pos):
        new_row, new_col = to_pos
        if not (0 <= new_row < 8 and 0 <= new_col < 8):
            return False
        if self.board.grid[new_row][new_col] is not None:
            return False

        from_row, from_col = piece.position
        row_diff = new_row - from_row
        col_diff = new_col - from_col

        # Regular move
        if abs(row_diff) == 1 and abs(col_diff) == 1:
            if piece.get_color() == "white" and row_diff == 1:
                return True
            if piece.get_color() == "black" and row_diff == -1:
                return True

        # Capture move
        if self.is_capture_move(piece, to_pos):
            return True

        return False

    def has_additional_capture(self, piece):
        row, col = piece.position
        directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if self.validate_move(piece, (new_row, new_col)) and self.is_capture_move(piece, (new_row, new_col)):
                    return True
        return False

    def play(self):
        self.setup()
        print("Starting Checkers!")

        while True:
            self.board.display()
            player = self.get_current_player()
            print(f"{player.name}'s turn ({player.color})")

            from_pos, to_pos = self.input_move()
            from_row, from_col = from_pos
            piece = self.board.grid[from_row][from_col]

            if piece is None:
                print("No piece at that position!")
                continue
            if piece.get_color() != player.color:
                print("That's not your piece!")
                continue
            if not self.validate_move(piece, to_pos):
                print("Invalid move!")
                continue

            captured = self.is_capture_move(piece, to_pos)

            if captured:
                captured_row, captured_col = captured
                captured_piece = self.board.grid[captured_row][captured_col]
                self.board.grid[captured_row][captured_col] = None
                opponent = self.players[1 - self.current_player_index]
                if captured_piece in opponent.pieces:
                    opponent.remove_piece(captured_piece)
                print(f"{player.name} captured a piece at ({captured_row}, {captured_col})!")

            self.board.move_piece(piece, to_pos)

            if captured:
                print("You captured! You get another turn.")
                continue


            self.switch_turn()


if __name__ == "__main__":
    game = Game()
    game.play()
