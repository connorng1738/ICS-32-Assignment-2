from game import Game
from ui import UI

def main ():
    rows = int(input(""))
    cols = int(input(""))  

    game = Game(rows,cols)

    config = input("")

    if config == "CONTENTS":
        contents = []
        for i in range(rows):
            line = input()
            contents.append(list(line))
        print(contents)
        game.create_content_field(contents)
        

    while True:
        UI.display_field(game)
        if game.check_virus():
            print('LEVEL CLEARED')
        command = input()

        if command.startswith("Q"):
            break
        if command.startswith("F"): 
            game.create_faller(command)
        if not command:
            game.apply_gravity()
        if command.startswith("A"):
            pass

if __name__ == "__main__":
    main()


    