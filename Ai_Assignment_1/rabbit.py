from collections import deque

def is_goal(state):
    return state == "EEE_WWW"

def get_neighbors(state):
    neighbors = []
    s = list(state)
    i = state.index('_')

    if i < 6 and s[i + 1] == 'E':
        temp = s[:]
        temp[i], temp[i + 1] = temp[i + 1], temp[i]
        neighbors.append("".join(temp))

    if i < 5 and s[i + 2] == 'E' and s[i + 1] == 'W':
        temp = s[:]
        temp[i], temp[i + 2] = temp[i + 2], temp[i]
        neighbors.append("".join(temp))

    if i > 0 and s[i - 1] == 'W':
        temp = s[:]
        temp[i], temp[i - 1] = temp[i - 1], temp[i]
        neighbors.append("".join(temp))

    if i > 1 and s[i - 2] == 'W' and s[i - 1] == 'E':
        temp = s[:]
        temp[i], temp[i - 2] = temp[i - 2], temp[i]
        neighbors.append("".join(temp))

    return neighbors

def bfs(start):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        state = path[-1]

        if is_goal(state):
            return path
        
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    
    return []

def dfs(start):
    visited = set()
    stack = [[start]]

    while stack:
        path = stack.pop()
        state = path[-1]

        if is_goal(state):
            return path
        
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(path + [neighbor])
    
    return []

start_state = "WWW_EEE"

print("BFS Path:")
bfs_path = bfs(start_state)
if bfs_path:
    for step in bfs_path:
        print(step)
else:
    print("No solution found.")

print("\nDFS Path:")
dfs_path = dfs(start_state)
if dfs_path:
    for step in dfs_path:
        print(step)
else:
    print("No solution found.")
