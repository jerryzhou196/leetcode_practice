from collections import deque

def findPath(start_y, start_x, maze):
    queue = deque()
    queue.append((start_y, start_x))
    seen = set()
    score = 0
    can_finish = False

    while queue: 
        node = queue.popleft()
        if node in seen or maze[node[0]][node[1]] == 'X': 
            continue
        seen.add(node)
        if maze[node[0]][node[1]] == 'E':
            can_finish = True
        elif maze[node[0]][node[1]] != 'S':
            score += int(maze[node[0]][node[1]])
        for x, y in [[0,1], [1, 0], [-1, 0], [0, -1]]:
            new_y, new_x = node[0] + y, node[1] + x
            if new_y >= 0 and new_y < len(maze) and new_x >= 0 and new_x < len(maze[0]):
                queue.append((new_y, new_x))
    
    return score if can_finish else -1

grid = [
    ['X', 'S', '1', 'X', 'X', 'X'],
    ['X', '1', '2', '1', 'X', 'X'],
    ['X', 'X', '2', '1', '1', '9'],
    ['X', 'X', 'X', 'E', 'X', 'X'],
]
print(findPath(0,1, grid))



# iteration #1: 
# curr_node = (0, 1)
# queue = (0, 2), (1, 1)
# mark (0, 1) as seen
# score: 0

# iteration #2: 
# curr_node = (0, 2)
# queue = (1, 1), (1, 2)
# mark (0, 2) as seen
# score: 1

# iteration #3: 
# curr_node = (1, 1)
# queue = (1, 1), (1, 2), (1, 2)
# mark (1, 1) as seen
# score: 3

# iteration #4: 
# curr_node = (1, 2)
# queue = (1, 2), (1, 2), (1, 3), 
# mark (0, 2) as seen
# score: 5








