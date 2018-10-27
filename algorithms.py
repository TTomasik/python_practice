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
        if current[0] in [0, len(graph[0])] or current[1] in [0, len(graph)]:
            return "The coordinates of nearest exit are: [{}, {}]".format(current[0], current[1])
        if current not in seen:
            seen.add(current)
            for node in paths:
                if node[0] == current[0] and node[1] in [current[1] + 1, current[1] - 1]:
                    queue.append(node)
                if node[1] == current[1] and node[0] in [current[0] + 1, current[0] - 1]:
                    queue.append(node)

graph = [
    '########',
    '# #    #',
    '# # ####',
    '#    x #',
    '### ####',
    '       #',
    '########'
]
