from game import Game


class UI:
    @staticmethod
    def display_field(state):
        for r in range(state.rows):
            print('|', end='')
            for c in range(state.cols):
                faller_piece = get_faller_symbol(r, c, state.faller)
                if faller_piece:
                    print(faller_piece, end='')
                else:
                    cell = state.field[r][c]
                    if cell == ' ':
                        print('   ', end='')
                    elif cell in 'rby':
                        print(f' {cell} ', end='') 
                    else:
                        print(f' {cell} ', end='')  
            print('|')
        print(' ' + '-' * (3 * state.cols))


def get_faller_symbol(row, col, faller):
    if faller is None:
        return None

    r = faller['row']
    l_col = faller['left_col']
    r_col = faller['right_col']
    l = faller['left_color']
    r_color = faller['right_color']
    state = faller['state']
    parity = faller['parity']

    if row == r:
        if parity == 'even':
                if col == l_col:
                    return f"{'[' if state == 'falling' else '|'}{l}--"
                elif col == r_col:
                    return f"{r_color}{']' if state == 'falling' else '|'}"
        else:
            if col == l_col:
                return f"{'[' if state == 'falling' else '|'}{l}-{r}{']' if state == 'falling' else '|'}"
    return None
