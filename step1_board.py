# Размер поля
BOARD_SIZE = 5

# Базы и башня
player_base = (0, 0) # Левый верх - база игрока
enemy_base = (BOARD_SIZE - 1, BOARD_SIZE -1) # Правый нижний - база врага
tower_pos = (BOARD_SIZE//2, BOARD_SIZE//2) # Центр - башня

# Список юнитов
units = []

# Функция отрисовки поля
def draw_board():
    for y in range(BOARD_SIZE):
        row = ''
        for x in range(BOARD_SIZE):
            pos = (x, y)
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
def create_unit(owner):
    unit = {
        'type': 'warrior',
        'owner': owner,
        'hp': 3,
        'damage': 1,
        'pos': player_base if owner == 'Player' else enemy_base,
        'symbol': 'PW ' if owner == 'Player' else 'EW '
    }
    units.append(unit)
    print(f"{owner} создал воина")

# Перемещение юнита
def move_unit(owner):
    own_units = [u for u in units if u['owner'] == owner]
    if not own_units:
        print("Нет доступных юнитов.")
        return

    print("\nДоступные юниты:")
    for i, u in enumerate(own_units):
        print(f"{i}: {u['symbol']} HP: {u['hp']} на {u['pos']}")

    try:
        index = int(input("Выберите юнита по номеру: "))
        dx = int(input("Сдвиг по X (-1, 0, 1): "))
        dy = int(input("Сдвиг по Y (-1, 0, 1): "))

        unit = own_units[index]
        new_x = unit['pos'][0] + dx
        new_y = unit['pos'][1] + dy

        if 0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE:
            unit['pos'] = (new_x, new_y)
            print(f"Юнит перемещён на {unit['pos']}")
        else:
            print("Ход вне карты!")

    except (ValueError, IndexError):
        print("Некорректный ввод")

# Битва
def resolve_combat():
    global units
    positions = {}
    for u in units:
        pos = u['pos']
        if pos not in positions:
            positions[pos] = []
        positions[pos].append(u)

    new_units = []
    for pos,group in positions.items():
        owners = set(u['owner'] for u in group)
        if len(owners) == 1:
            print(f"⚔️ Битва на {pos}!")
            for attacker in group:
                for target in group:
                    if attacker['owner'] != target['owner']:
                        target['hp'] -= attacker['damage']
        survivors = [u for u in group if u['hp'] > 0]
        new_units.extend(survivors)

    units[:] = new_units

# Простой ход врага (бота)
def enemy_turn():
    print("\n=== Ход врага ===")
    create_unit('Enemy')
    # Двигаем всех врагов на -1 по X и Y (к игроку)
    for u in units:
        if u['owner'] == 'Enemy':
            x, y = u['pos']
            new_x = max(0, x-1)
            new_y = max(0, y-1)
            u['pos'] = (new_x, new_y)

tower_control = None
tower_progress = 0

def check_tower():
    global tower_control, tower_progress

    occupiers = [u for u in units if u['pos'] == tower_pos]
    if len(occupiers) == 1:
        owner = occupiers[0]['owner']
        if tower_control == owner:
            tower_progress += 1
        else:
            tower_control = owner
            tower_progress = 1
        print(f"🏰 {owner} удерживает башню ({tower_progress}/3)")
    else:
        tower_control = None
        tower_progress = 0

    if tower_progress >= 3:
        print(f"\n🏆 {tower_control} ПОБЕЖДАЕТ, ЗАХВАТИВ БАШНЮ!")
        return True
    return False

def end_game():
    print("\n🎮 Игра окончена.")
    exit()

# Главный цикл игры
def game_loop():
    turn = 1
    while True:
        print(f"\n=== ХОД {turn} ===")
        draw_board()
        print("\nВыберите действие:")
        print("1 - Создать юнита")
        print("2 - Переместить юнита")
        print("3 - Выйти из игры")

        choice = input("Ваш выбор: ")
        if choice == "1":
            create_unit('Player')
        elif choice == "2":
            move_unit('Player')
        elif choice == "3":
            print("Выход из игры.")
            break
        else:
            print("Неверная команда")

        resolve_combat()
        if check_tower():
            end_game()


        enemy_turn()
        resolve_combat()
        if check_tower():
            end_game()

        turn += 1

# Старт
game_loop()