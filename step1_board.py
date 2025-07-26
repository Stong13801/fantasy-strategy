# Размер поля
BOARD_SIZE = 5

# Координаты объектов на карте
player_base = (0, 0) # Левый верх - база игрока
enemy_base = (BOARD_SIZE - 1, BOARD_SIZE -1) # Правый нижний - база врага
tower_pos = (BOARD_SIZE//2, BOARD_SIZE//2) # Центр - башня

# Юниты (список словарей)
units = []

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

# Создание юнита
def create_unit():
    unit = {
        'type': 'warriot',
        'owner': 'Player',
        'pos': player_base,
        'symbol': 'PW '
    }
    units.append(unit)
    print("Юнит создан и размещён на базе игрока.")

# Переместить юнита
def move_unit():
    if not units:
        print("Нет доступных юнитов.")
        return

    print("\nДоступные юниты:")
    for i, u in enumerate(units):
        print(f"{i}: {u['symbol']} на {u['pos']}")

    try:
        index = int(input("Выберите юнита по номеру: "))
        dx = int(input("Сдвиг по X (-1, 0, 1): "))
        dy = int(input("Сдвиг по Y (-1, 0, 1): "))

        unit = units[index]
        new_x = unit['pos'][0] + dx
        new_y = unit['pos'][1] + dy

        if 0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE:
            unit['pos'] = (new_x, new_y)
            print(f"Юнит перемещён на {unit['pos']}")
        else:
            print("Ход вне карты!")

    except (ValueError, IndexError):
        print("Некорректный ввод")

# Главный цикл игры
def game_loop():
    while True:
        print("\n=== Ход игрока ===")
        draw_board()
        print("\nВыберите действие:")
        print("1 - Создать юнита")
        print("2 - Переместить юнита")
        print("3 - Выход")

        choice = input("Ваш выбор: ")
        if choice == "1":
            create_unit()
        elif choice == "2":
            move_unit()
        elif choice == "3":
            print("Выход из игры.")
            break
        else:
            print("Неверная команда")

# Запуск игры
game_loop()