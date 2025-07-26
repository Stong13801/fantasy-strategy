# Размер поля
BOARD_SIZE = 5

# Координаты объектов на карте
player_base = (0, 0) # Левый верх - база игрока
enemy_base = (BOARD_SIZE - 1, BOARD_SIZE -1) # Правый нижний - база врага
tower_pos = (BOARD_SIZE//2, BOARD_SIZE//2) # Центр - башня

# Юниты (список словарей)
units = [
    {
        'type': 'warrior',
        'owner': 'Player',
        'pos': (0,1),
        'symbol': 'PW '  #Player Warrior
    }
]

# Отрисовка поля
def draw_board():
    for y in range(BOARD_SIZE):
        row = ''
        for x in range(BOARD_SIZE):
            pos = (x, y)
            # Проверка: юнит ли здесь
            unit_here = next((u for u in units if u['pos'] == pos), None)
            if unit_here:
                row += f"[{unit_here['symbol']}]"
            elif pos == player_base:
                row += '[ P ]'  # Player base
            elif pos == enemy_base:
                row += '[ E ]'  # Enemy base
            elif pos == tower_pos:
                row += '[ T ]'  # Tower
            else:
                row += '[ . ]'  # Пустая клетка
        print(row)

# Переместить юнита
def move_unit(unit_index, dx, dy):
    unit = units[unit_index]
    x, y = unit['pos']
    new_x = x + dx
    new_y = y + dy

    # Проверка: в пределах ли поля
    if 0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE:
        unit['pos'] = (new_x, new_y)
        print(f"Юнит перемещён на {unit['pos']}")
    else:
        print(f"Ход невозможен - вне карты!")

# Основной код
draw_board()

# Пример перемещения
print("\nДвигаем юнита вниз...")
move_unit(0, 0, 1)

print("\nНовое поле:")
draw_board()