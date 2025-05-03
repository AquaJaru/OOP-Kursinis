from abc import ABC, abstractmethod


class AbstractPiece(ABC):
    @abstractmethod
    def move(self, new_position):
        pass


class Piece(AbstractPiece):
    def __init__(self, color, position):
        self._color = color
        self.position = position  # (row, col)

    def move(self, new_position):
        self.position = new_position

    def get_color(self):
        return self._color

    def __str__(self):
        return f"{self._color[0].upper()}P"