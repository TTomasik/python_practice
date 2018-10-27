# BFS
import collections


def bfs(graph, root):
    seen, queue = set([]), collections.deque([root])
    while queue:
        current = queue.popleft()
        if current not in seen:
            seen.add(current)
            for node in graph[current]:
                queue.append(node)

# graph = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [6], 6: [7], 7: [5]}
# print(bfs(graph, 1))


def maze(graph):
    paths, root = [], ()
    for idx_r, row in enumerate(graph):
        for idx_e, element in enumerate(row):
            if element == ' ':
                paths.append((idx_r, idx_e))
            elif element == 'x':
                root = (idx_r, idx_e)
    seen, queue = set([]), collections.deque([root])
    while queue:
        current = queue.popleft()
        row = current[0]
        position = current[1]
        if row in [0, len(graph) - 1] or position in [0, len(graph[0]) - 1]:
            return "The coordinates of nearest exit are: [{}, {}]".format(row, position)
        if current not in seen:
            seen.add(current)
            for node in paths:
                if node[0] == row and node[1] in [position + 1, position - 1]:
                    queue.append(node)
                if node[1] == position and node[0] in [row + 1, row - 1]:
                    queue.append(node)

graph = [
    '########',
    '# #    #',
    '# # ####',
    '#    x #',
    '### ####',
    '#      #',
    '###### #'
]
