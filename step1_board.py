# Размер поля
BOARD_SIZE = 5

# Координаты объектов на карте
player_base = (0, 0) # Левый верх - база игрока
enemy_base = (BOARD_SIZE - 1, BOARD_SIZE -1) # Правый нижний - база врага
tower_pos = (BOARD_SIZE//2, BOARD_SIZE//2) # Центр - башня

# Функция отрисовки поля
def draw_board():
    for y in range(BOARD_SIZE):
        row = ''
        for x in range(BOARD_SIZE):
            pos = (x, y)
            if pos == player_base:
                row += '[ P ]'  # Player base
            elif pos == enemy_base:
                row += '[ E ]'  # Enemy base
            elif pos == tower_pos:
                row += '[ T ]'  # Tower
            else:
                row += '[ . ]'  # Пустая клетка
        print(row)

# Запуск
draw_board()