# 8-Puzzle using Depth First Search (DFS)

def display(state):
    print("-------------")
    for i in range(0, 9, 3):
        print("|", state[i], "|", state[i + 1], "|", state[i + 2], "|")
    print("-------------")


def get_neighbors(state):
    neighbors = []

    # Find blank tile (0)
    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    # Possible movements: Up, Down, Left, Right
    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Check whether the move is valid
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            # Create new state
            new_state = list(state)

            # Swap blank with adjacent tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


def dfs(initial, goal):

    # Stack contains (state, path)
    stack = [(initial, [initial])]

    # To avoid repeated states
    visited = set()

    while stack:

        # Remove top element
        current, path = stack.pop()

        # Check goal
        if current == goal:
            return path

        # Skip if already visited
        if current in visited:
            continue

        visited.add(current)

        # Generate next states
        neighbors = get_neighbors(current)

        for neighbor in neighbors:

            if neighbor not in visited:
                stack.append(
                    (neighbor, path + [neighbor])
                )

    return None


# -----------------------------
# Main Program
# -----------------------------

initial = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

print("INITIAL STATE:")
display(initial)

print("GOAL STATE:")
display(goal)

solution = dfs(initial, goal)

if solution:

    print("\nDFS SOLUTION FOUND")
    print("Number of moves:", len(solution) - 1)

    print("\nSolution Path:")

    for step, state in enumerate(solution):

        print("\nStep", step)
        display(state)

else:
    print("No solution found.")
