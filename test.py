import tkinter as tk
import random
import time

# Set up the game board
rows = 20
cols = 10
board = [[0] * cols for _ in range(rows)]


# Define the tetrominoes
tetrominoes = [
    [[1, 1, 1, 1]], # I
    [[2, 0, 0], [2, 2, 2]], # J
    [[0, 0, 3], [3, 3, 3]], # L
    [[4, 4], [4, 4]], # O
    [[0, 5, 5], [5, 5, 0]], # S
    [[0, 6, 0], [6, 6, 6]], # T
    [[7, 7, 0], [0, 7, 7]], # Z
]




class TetrisGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Tetris Game")
        self.master.geometry("400x600")
        self.master.resizable(False, False)

        self.canvas = tk.Canvas(self.master, bg="#ECECEC", width=300, height=600, bd=0, highlightthickness=0)
        self.canvas.pack(side=tk.LEFT)

        self.next_shape_canvas = tk.Canvas(self.master, bg="#ECECEC", width=100, height=100, bd=0, highlightthickness=0)
        self.next_shape_canvas.pack(side=tk.RIGHT)

        self.score_label = tk.Label(self.master, text="Score: 0", font=("Helvetica", 16))
        self.score_label.pack(side=tk.TOP)

        self.level_label = tk.Label(self.master, text="Level: 1", font=("Helvetica", 16))
        self.level_label.pack(side=tk.TOP)

        self.game_over_label = tk.Label(self.master, text="Game Over!", font=("Helvetica", 24), fg="red")

        self.initialize_game()


    def initialize_game(self):
        self.board = TetrisBoard(self.canvas, self.next_shape_canvas, self.score_label,
                                 self.level_label, self.game_over_label)
        self.board.pack()

        self.master.bind("<Left>", self.board.move_left)
        self.master.bind("<Right>", self.board.move_right)
        self.master.bind("<Down>", self.board.move_down)
        self.master.bind("<Up>", self.board.rotate_shape)
        self.master.bind("<space>", self.board.drop_shape)


class TetrisBoard:
    def __init__(self, canvas, next_shape_canvas, score_label, level_label, game_over_label):
        self.canvas = canvas
        self.next_shape_canvas = next_shape_canvas
        self.score_label = score_label
        self.level_label = level_label
        self.game_over_label = game_over_label

        self.width = 10
        self.height = 20
        self.cell_size = 30

        self.board = [[0] * self.width for _ in range(self.height)]
        self.current_shape = None
        self.current_shape_coords = []
        self.next_shape = None

        self.score = 0
        self.level = 1
        self.lines_cleared = 0