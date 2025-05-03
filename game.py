import shlex

class Game:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.field = self.create_empty_field()
        self.faller = None
    
    def create_empty_field(self) -> list[list]: #is this the right type hint for a 2d array
        """"
        Creates the game field

        Returns:
          list[list]: Empty 2D array
        """
        return [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
    
    def create_content_field(self, contents: list) -> None: #work on this once you figure out empty field
        """
        Given lines of input, initializes a field with specific content

        Arguments:
          contents: list of lines from user input #maybe be more specific later
        """

        self.field = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                print(contents[r][c])
                self.field[r][c] = contents[r][c]

    def create_faller(self, command: str) -> None:
        """
        Creates a faller symbol in middle of field

        Arguments:
          command: list of user input
        """
        parts = shlex.split(command)
        left, right = parts[1], parts[2]
        
        if self.cols % 2 == 1:
            left_col = self.cols // 2 - 1
            right_col = self.cols // 2
            parity = 'odd'
            print('odd')
        else:
            left_col = self.cols // 2 - 1
            right_col = left_col + 1
            print('even')
            parity = 'even'
            
        self.faller = { 
            'row': 1,
            'left_col': left_col,
            'right_col': right_col, 
            'left_color': left,
            'right_color': right,
            'parity': parity,
            'state': 'falling',
            'rotation': 0
        }

    def apply_gravity(self) -> None:
        """
        Keeps track of faller state, and also moves faller down everytime 'Enter' is input.
        """
        if not self.faller: 
            return
        
        row = self.faller['row']
        left_col = self.faller['left_col']
        right_col = self.faller['right_col']

        if row + 1 < self.rows and self.field[row + 1][left_col] == ' ' and self.field[row + 1][right_col] == ' ':
            self.faller['row'] += 1
            self.faller['state'] = 'falling'
            print('falling')
        elif self.faller['state'] == 'falling':
            self.faller['state'] = 'landed'
            print('landed')
        elif self.faller['state'] == 'landed':
            self.faller['state'] = 'frozen'
            self.freeze_faller()
            print('frozen')

    def freeze_faller(self) -> None: #perhaps move this to ui.py
        """
        When faller is frozen, saves faller instance onto field.
        """

        if not self.faller:
            return
        
        print("Freeze", self.faller)

        row = self.faller['row']
        left_col = self.faller['left_col']
        right_col = self.faller['right_col']
        left_color = self.faller['left_color']
        right_color = self.faller['right_color']
        rotation = self.faller['rotation']

        if rotation == 0:
            self.field[row][left_col] = f"{left_color}-"
            self.field[row][right_col] = f"-{right_color}"
        if rotation == 90:
            self.field[row - 1][left_col] = f"{left_color}"
            self.field[row][left_col] = f"{right_color}"
        if rotation == 180:
            self.field[row][left_col] = f"{right_color}-"
            self.field[row][right_col] = f"-{left_color}"
        if rotation == 270:
            self.field[row - 1][left_col] = f"{right_color}"
            self.field[row][left_col] = f"{left_color}"


        self.faller = None

    def check_virus(self) -> bool:
        """
        Iterates through created field to check if a virus exists

        Returns:
          bool: True or False #should i be more specific about this
        
        """
        for row in self.field:
            for cell in row:
                if cell in ['r', 'y', 'b']:
                    return False
                else:
                    return True

    def rotate_clockwise(self) -> None:
        """
        Rotates faller clockwise, and keeps track of rotated position
        """
        self.faller['rotation'] = (self.faller['rotation'] + 90) % 360

    def rotate_counter(self) -> None: #implement a method later to check if position is available
        """
        Rotates faller counter clockwise, and keeps track of rotated position
        """
        self.faller['rotation'] = (self.faller['rotation'] + 270) % 360
    
    def move_left(self) -> bool: #have to fix logic, why is the empty cell not actually empty
        """
        Shifts faller to the left if adjacent cell is available

        Returns:
          bool: True or False
        """
        if not self.faller:
            return False
        
        left_col = self.faller['left_col']
        right_col = self.faller['right_col']
        row = self.faller['row']
        
        if left_col > 0:
            if self.field[row][left_col - 1] == ' ' and self.field[row][right_col - 1] == ' ':
                self.faller['left_col'] -= 1
                self.faller['right_col'] -= 1
        return True
    
    def move_right(self) -> bool: #when moving right, why is the empty cell not actually empty
        """
        Shifts faller to the right if adjacent cell is available

        Returns:
          bool: True or False
        """
        if not self.faller:
            return False
        
        left_col = self.faller['left_col']
        right_col = self.faller['right_col']
        row = self.faller['row']
        
        print('l' + str(left_col))
        print('r' + str(right_col))
        if right_col < self.cols - 1:
            if self.field[row][left_col + 1] == ' ' and self.field[row][right_col + 1] == ' ': #this logic works for a horizontal faller
                self.faller['left_col'] += 1
                self.faller['right_col'] += 1
        return True

    def create_virus(self, command) -> None:
        """
        Given user-specificed position, creates a virus within the field
        """
        parts = shlex.split(command)
        row = int(parts[1])
        col = int(parts[2])
        color = parts[3].lower()

        self.field[row][col] = color

    def find_matches(self) -> bool:
        match = False
        for row in self.rows:
            for col in self.cols:
                if str(self.field[row][col]).lower() in 'ryb':
                    if self.find_horizontal_match(row, col):
                        match = True
                    if self.find_vertical_match(row, col):
                        match = True
        return match


    def find_horizontal_match(self, row: int, col: int) -> bool:
        color = self.field[row][col]
        if col + 3 < self.cols:
            for i in range(1, 4):
                if self.field[row][col + i] != color:
                    return False
            
            for i in range(4):
                self.field[row][col + i] = f'*{color}*'
            return True
        return False

    def find_vertical_match(self, row: int, col: int) -> bool: 
       color = self.field[row][col]
       if row + 3 < self.rows:
            for i in range(1, 4):
                if self.field[row][col + i] != color:
                    return False
            for i in range(4):
                self.field[row + i][col] = f'*{color}*'
            return True
       return False
    



