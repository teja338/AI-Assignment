from collections import deque
from itertools import combinations

times = {
    'A': 5,    # Amogh
    'M': 10,   # Ameya
    'G': 20,   # Grandmother
    'F': 25    # Grandfather
}

def bfs_bridge_and_torch():
    initial = (frozenset(['A', 'M', 'G', 'F']), frozenset(), 0, 'L')
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        (left, right, current_time, torch_side), path = queue.popleft()

        if len(left) == 0 and torch_side == 'R':
            return path + [("All crossed", current_time)]

        state_id = (left, right, torch_side)
        if state_id in visited or current_time > 60:
            continue
        visited.add(state_id)

        if torch_side == 'L':
            
            for p1, p2 in combinations(left, 2):
                new_left = left - {p1, p2}
                new_right = right | {p1, p2}
                new_time = current_time + max(times[p1], times[p2])
                queue.append((
                    (frozenset(new_left), frozenset(new_right), new_time, 'R'),
                    path + [((p1, p2), '->', new_time)]
                ))
        else:
            
            for p in right:
                new_left = left | {p}
                new_right = right - {p}
                new_time = current_time + times[p]
                queue.append((
                    (frozenset(new_left), frozenset(new_right), new_time, 'L'),
                    path + [((p,), '<-', new_time)]
                ))

    return None


solution = bfs_bridge_and_torch()

print("Bridge and Torch Solution:")
if solution:
    for step in solution:
        print(step)
else:
    print(" No solution found.")
