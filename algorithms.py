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
                    _row.append('*')
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
        if row in [0, len(graph) - 1] or position in [0, len(graph[0]) - 1]:
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
    '#################',
    '# #    #   #     ',
    '# # #### # # ####',
    '#    X # # #    #',
    '### #### # # ## #',
    '#        #    # #',
    '#################'
]

print(maze(graph))
