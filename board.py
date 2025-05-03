class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.last_moved_pos = None

    def place_piece(self, piece):
        row, col = piece.position
        self.grid[row][col] = piece

    def move_piece(self, piece, new_position):
        old_row, old_col = piece.position
        new_row, new_col = new_position
        self.grid[old_row][old_col] = None
        piece.move(new_position)
        self.grid[new_row][new_col] = piece
        self.last_moved_pos = (new_row, new_col)


    def display(self):
        # Emojis
        white_piece_emoji = "⚪"
        black_piece_emoji = "⚫"
        white_highlight = "🔵"
        black_highlight = "🔴"
        empty_tile = "⬜"

        print("\n    0  1  2  3  4  5  6  7")
        print("   -------------------------")
        for row_idx, row in enumerate(self.grid):
            line = f"{row_idx} | "
            for col_idx, piece in enumerate(row):
                if piece is None:
                    line += empty_tile + " "
                else:
                    is_last_moved = self.last_moved_pos == (row_idx, col_idx)
                    color = piece.get_color()

                    if color == "white":
                        emoji = white_piece_emoji
                        if is_last_moved:
                            emoji = white_highlight
                    else:
                        emoji = black_piece_emoji
                        if is_last_moved:
                            emoji = black_highlight

                    line += emoji + " "
            print(line)
        print()
