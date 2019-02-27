# BFS
import collections


# def bfs(graph, root):
#     seen, queue = set([]), collections.deque([root])
#     while queue:
#         current = queue.popleft()
#         if current not in seen:
#             seen.add(current)
#             for node in graph[current]:
#                 queue.append(node)
#
# graph = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [6], 6: [7], 7: [5]}
# print(bfs(graph, 1))


def maze(graph):
    main = {}
    paths, root = [], ()
    for idx_r, row in enumerate(graph):
        for idx_e, element in enumerate(row):
            if element == ' ':
                paths.append((idx_r, idx_e))
            elif element == 'X':
                paths.append((idx_r, idx_e))
                root = (idx_r, idx_e)
    for node in paths:
        if node not in main:
            main[node] = set([])
        for _node in paths:
            if (node[0] == _node[0] and _node[1] in (node[1] - 1, node[1] + 1)) or\
                    (node[1] == _node[1] and _node[0] in (node[0] - 1, node[0] + 1)):
                main[node].add(_node)
    nearest_exit = find_nearest_exit(graph, root, paths)
    if nearest_exit:
        return draw_path_in_maze(main, root, nearest_exit, graph)
    return "There is no exit from this position."


def draw_path_in_maze(graph, root, exit, maze):
    queue = [(root, [root])]
    result = []
    while queue:
        (current, path) = queue.pop(0)
        for node in graph[(current)] - set(path):
            if list(node) == exit:
                result = path + [node]
            else:
                queue.append((node, path + [node]))
    maze_with_path = []
    for idx_r, row in enumerate(maze):
        _row = []
        for idx_e, element in enumerate(row):
            if element == ' ':
                if (idx_r, idx_e) in result:
                    _row.append('.')
                else:
                    _row.append(element)
            else:
                _row.append(element)
        maze_with_path.append(''.join(_row))
    return ''.join([row + '\n' for row in maze_with_path])


def find_nearest_exit(graph, root, paths):
    seen, queue = set([]), collections.deque([root])
    while queue:
        current = queue.popleft()
        row = current[0]
        position = current[1]
        if (row in [0, len(graph) - 1] or position in [0, len(graph[0]) - 1])\
                and row != root[0] and position != root[1]:
            print("The coordinates of nearest exit are: [{}, {}]".format(row, position))
            return [row, position]
        if current not in seen:
            seen.add(current)
            for node in paths:
                if node[0] == row and node[1] in [position + 1, position - 1]:
                    queue.append(node)
                if node[1] == position and node[0] in [row + 1, row - 1]:
                    queue.append(node)


graph = [
    '#X###############',
    '# #    #   #    #',
    '# # #### # # ####',
    '#      # # #    #',
    '### #### # # ## #',
    '#        #    # #',
    '########## ######',
    '#        # ######',
    '###### ###      #',
    '#          ## # #',
    '### ######### ###',
    '#   #      ##   #',
    '### ########### #',
    '#   #           #',
    '# ######## ## ###',
    '#  ###   # ## ###',
    '####   ##  ##   #',
    '## # #### ##### #',
    '#  #      #     #',
    '# ## # #### ### #',
    '#    # ######   #',
    '# #### # #    ###',
    '#  ###   ########',
    '## ##############',
]


def path_finder(area):
    splitted_area = area.splitlines()
    end = height, width = len(splitted_area) - 1, len(splitted_area[0]) - 1
    queue, seen, path = {(0, 0): 0}, set(), []
    while queue:
        x, y = min(queue, key=queue.get)
        total_path_weight = queue.pop((x, y))
        seen.add((x, y))
        if (x, y) == end:
            # path.append(end)
            # return path_drawer(area, width, path)
            return total_path_weight
        for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
            z, w = x + i, y + j
            if (z, w) in seen or not (0 <= z <= height and 0 <= w <= width):
                continue
            single_path_weight = total_path_weight + abs(int(splitted_area[x][y]) - int(splitted_area[z][w]))
            if single_path_weight < queue.get((z, w), float('inf')):
                queue[z, w] = single_path_weight
                # if (x, y) not in path: path.append((x, y))


def path_drawer(area, width, path):
    splitted_area = area.splitlines()
    area_with_path = []
    for idx_row, row in enumerate(splitted_area):
        counter = 0
        for idx_col, col in enumerate(row):
            counter += 1
            if (idx_row, idx_col) in path:
                area_with_path.append('*')
            else:
                area_with_path.append(col)
            if counter == width + 1:
                area_with_path.append('\n')
    return ''.join(area_with_path)


area = '\n'.join([
    '000000000000000000',
    '111111111111111110',
    '000000000000000000',
    '011111111111111111',
    '000000000000000000',
    '111111111111111110',
    '000000000000000000',
    '111111111111111110',
    '000000000000000000',
    '011111111111111111',
    '000000000000000000',
    '111111111111111110',
    '000000000000000000',
    '111111111111111110',
    '000000000000000000',
    '011111111111111111',
    '000000000000000000',
    '111111111111111110',
])
