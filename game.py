import shlex

class Game:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.field = self.create_empty_field()
        self.faller = None
    
    def create_empty_field(self):
        return [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
    
    def create_content_field(self, contents: list): #work on this once you figure out empty field
        self.field = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                print(contents[r][c])
                self.field[r][c] = contents[r][c]

    def create_faller(self, command: str):
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
            
        self.faller = { #should i put this in a seperate function
            'row': 1,
            'left_col': left_col,
            'right_col': right_col, 
            'left_color': left,
            'right_color': right,
            'parity': parity,
            'state': 'falling'
        }

    def apply_gravity(self):
        if not self.faller: 
            return
        
        row = self.faller['row']
        left_col = self.faller['left_col']
        right_col = self.faller['right_col']

        if row + 1 < self.rows and self.field[row + 1][left_col] == ' ' and self.field[row + 1][right_col] == ' ':
            self.faller['row'] += 1
            self.faller['state'] == 'falling'
            print('falling')
        elif self.faller['state'] == 'falling':
            self.faller['state'] = 'landed'
            print('landed')
        elif self.faller['state'] == 'landed':
            self.freeze_faller()
            #self.faller['state'] = 'frozen'
            print('frozen')
                    
    def land_faller(self):
        row = self.faller['row']
        left_col = self.faller['left_col']
        right_col = self.faller['right_col']
        self.field[row][left_col] = self.faller['left_color']
        self.field[row][right_col] = self.faller['right_color']

    def freeze_faller(self):
        if not self.faller:
            return

        row = self.faller['row']
        left_col = self.faller['left_col']
        right_col = self.faller['right_col']
        left_color = self.faller['left_color']
        right_color = self.faller['right_color']
        parity = self.faller['parity']

        if parity == 'even':
            self.field[row][left_col] = f"{left_color}-"
            self.field[row][right_col] = f"-{right_color}"
        else:
            self.field[row][left_col] = f"{left_color}"
            self.field[row][right_col] = f"{right_color}"


        self.faller = None



    def check_virus(self):
        for row in self.field:
            for cell in row:
                if cell in ['r', 'y', 'b']:
                    return False
        return True

    def rotate_clockwise(self, command: str):
        pass

