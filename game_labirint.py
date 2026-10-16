import random 
start, end = (0, 0), (14, 14)
size = 15
attemps = 0
gamepole_found = False #
while not gamepole_found:
    attemps += 1
    game_pole = []
    for r in range(size):
        row = []
        for c in range(size):
            if random.random() < 0.30:
                row.append('#') # это у меня стена будет
            else:   
                row.append('.') # проход тип
        game_pole.append(row)
    game_pole[start[0]][start[1]] = "."
    game_pole[end[0]][end[1]] = '.'
    rows = len(game_pole)
    cols = len(game_pole[0])
    queue = [start]
    distances = {start: 0}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while len(queue) > 0:
        row, col = queue.pop(0)

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc
            neighbor = (nr, nc)
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if game_pole[nr][nc] == '#':
                continue
            if neighbor in distances:
                continue
            distances[neighbor] = distances[(row, col)] + 1
            queue.append(neighbor)
        if end in distances:
            gamepole_found = True
empty_cells = []
for r in range(size):
    for c in range(size):
        if game_pole[r][c] == '.' and (r, c) != start and (r, c) != end:
            empty_cells.append((r, c))
num_traps = random.randint(5, 10)
if len(empty_cells) < num_traps:
    num_traps = len(empty_cells)
positions = random.sample(empty_cells, num_traps)
for r, c in positions:
    game_pole[r][c] = 't'



player = start
steps = 0
traps_used = 0
game_over = False
print('Лабиринт создан.')
print('Управление: w(вверх) a(влево) s(вниз) d(вправо)')
print('f(найти путь), i(статистика), q(выход)')
while not game_over:
    for r in range(size):
        row_cells = []
        for c in range(size):
            if (r, c) == player:
                row_cells.append('p')
            elif (r, c) == start:
                row_cells.append('s')
            elif (r, c) == end:
                row_cells.append('e')
            else:
                row_cells.append(game_pole[r][c])
        print(row_cells)
    if player == end:
        print(f'победа! вы нашли выход за {steps} шагов!')
        print(f'попаданий в ловушки {traps_used}')
        break
    command = input('введите действие: ')
    dr, dc = 0, 0
    move = False
    if command == 'w':
        dr, dc = -1, 0
        move = True
    elif command == 's':
        dr, dc = 1, 0
        move = True
    elif command == 'a':
        dr, dc = 0, -1
        move = True
    elif command == 'd':
        dr, dc = 0, 1
        move = True
    elif command == 'f':
        find = [player]
        parent_find = {player: None}
        path_find = False
        while len(find) > 0:
            cur = find.pop(0)
            if cur == end:
                path_find = True
                break 
            f_row, f_col = cur
            for m_dr, m_dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = f_row + m_dr
                nc = f_col + m_dc
                neighbor = (nr, nc)
                if 0 <= nr < size and 0 <= nc < size:
                    if game_pole[nr][nc] != '#' and neighbor not in parent_find:
                        parent_find[neighbor] = cur
                        find.append(neighbor) 
        if not path_find:
            print('пути на выход нет:')
        else:
            path = []
            cur = end 
            while cur is not None:
                path.append(cur)
                cur = parent_find[cur]
            path.reverse()
            print(f'маршрут до выхода: {path}')
            print(f'длина пути: {(len(path) - 1)}')
    elif command == 'i':
        print('статистика:')
        print(f'позиция: {player}')
        print(f'шаги: {steps}')
        print(f'задето ловушек: {traps_used}')
    elif command == 'q':
        game_over = True
    else:
        print('неверный ввод')
    if move:
        new_r = player[0] + dr
        new_c = player[1] + dc
        if not (0 <= new_r < size and 0 <= new_c < size):
            print('выход за границы')
        elif game_pole[new_r][new_c] == '#':
            print('перед вами стена')
        else:
            player = (new_r, new_c)
            steps += 1
            if game_pole[new_r][new_c] == 't':
                traps_used += 1
                print('вы наступили на ловушку')
        
    
