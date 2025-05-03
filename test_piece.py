import unittest
from piece import Piece


class TestPiece(unittest.TestCase):
    def test_piece_creation(self):
        p = Piece("white", (0, 1))
        self.assertEqual(p.get_color(), "white")
        self.assertEqual(p.position, (0, 1))

    def test_move_piece(self):
        p = Piece("white", (2, 3))
        p.move((3, 4))
        self.assertEqual(p.position, (3, 4))


if __name__ == "__main__":
    unittest.main()