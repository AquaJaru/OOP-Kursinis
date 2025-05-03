class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pieces = []

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, piece):
        self.pieces.remove(piece)