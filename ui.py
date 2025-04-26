from game import *

def play_game():

    command = int(input())
    rows = int(input("Rows:"))
    cols = int(input("Columns:"))

    game = Game(rows, cols)
    
    while True:
        print(game.create_field())

        if command == 'Q':
            break
        if command == 'F':
            pass