from tkinter import *
from typing import List

from game_engine import Board, Piece, Move, PieceType
from helper_funcs import get_checker_pattern

class DraughtsUI:
    def __init__(self):
        self._root = Tk()
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._root.title("Draughts")
        self._root.resizable(width=False, height=False)
        self._root.geometry('{}x{}'.format(800, 420))

        self._canvas = Canvas(self._root)
        self._canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        self._canvas.config(background="lemon chiffon")

        self._pieces = {
            PieceType.White: [],  # type: List[int]
            PieceType.Black: []  # type: List[int]
        }

        moveTextBox = StringVar()
        moveTextBox = Entry(self._root, width=30)
        # moveTextBox.place(x=10, y=10, width=100)
        moveTextBox.grid(row=0, column=0, sticky=(S, E), pady=60, padx=60)

        moveButton = None  # TODO: add a button and receive input

        self._draw_main_ui()
        #self.set_pieces_black()

    def launch(self):
        self._root.mainloop()

    def apply_move(self, move: Move):
        """
        Moves the ovals on the gui such that a certain move is applied
        """
        raise NotImplementedError()

    def draw_board(self, board: Board):
        """
        Renders piece_by_type from a board from a blank ui state
        """
        for piece in board.piece_by_type[PieceType.Black] + board.piece_by_type[PieceType.White]:
            self.draw_piece(piece)

    def draw_piece(self, piece: Piece):
        """
        Renders a piece from a blank ui square
        """
        oval = self._canvas.create_oval(self._get_board_to_ui_coords(piece.x, piece.y),
                                        fill="black" if piece.type == PieceType.Black else "white")

        self._pieces[piece.type].append(oval)

    def _on_text_move_entered(self):
        # parse in a board class/another class, apply as a move
        pass

    def _get_board_to_ui_coords(self, row, col):
        return row * 40 + 10, col * 40 + 10, row * 40 + 50, col * 40 + 50

    def _draw_board_background(self):
        for (row, col) in get_checker_pattern(init_offset=0, init_row=0, rows=10, max_col=10):
            self._canvas.create_rectangle(self._get_board_to_ui_coords(row, col), fill="brown")

        for (row, col) in get_checker_pattern(init_offset=1, init_row=0, rows=10, max_col=10):
            self._canvas.create_rectangle(self._get_board_to_ui_coords(row, col), fill="orange")

    def _draw_main_ui(self):
        self._canvas.create_text((600, 50), text="Draughts", font=("Edwardian Script ITC", 60))
        self._canvas.create_text((520, 150), text="Player 1 Taken Pieces", font=("Times new roman", 16))
        self._canvas.create_text((520, 250), text="Player 2 Taken Pieces", font=("Times new roman", 16))
        self._canvas.create_text((480, 350), text="Enter Move", font=("Times new roman", 16))
        self._canvas.create_rectangle((10, 10, 410, 410), fill="lightgoldenrod")

        self._draw_board_background()


if __name__ == "__main__":
    ui = DraughtsUI()

    board = Board()

    board.init_default_state()
    ui.draw_board(board)

    ui.launch()
