BOARD_SIZE = 5

def draw_board():
    for y in range(BOARD_SIZE):
        row = ''
        for x in range(BOARD_SIZE):
            row += '[ . ]'
        print(row)

draw_board()