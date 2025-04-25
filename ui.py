from game import *

def play_game():
    rows = int(input("Rows:"))
    cols = int(input("Columns:"))

    game = Game(rows, cols)

    print(game.create_field())