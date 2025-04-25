class Game:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.field = [[' ' * 3 for _ in range(cols)] for _ in range(rows)]
                    
    def create_field(self):
        lines = []
        for row in self.field:
            lines.append('|' + ''.join(cell for cell in row) + '|')
        lines.append(' ' + '-' * (self.cols * 3))
        return '\n'.join(lines)
    
    def faller(self):
        pass #implement all class methods 

    
