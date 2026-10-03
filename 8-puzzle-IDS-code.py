
def display(state):
    print("-------------")
    for i in range(0, 9, 3):
        print("|", state[i], "|", state[i + 1], "|", state[i + 2], "|")
    print("-------------")


def get_neighbors(state):

    neighbors = []

    # Find blank tile
    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    # Possible movements
    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Check valid position
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank and adjacent tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


# ----------------------------------
# Depth Limited Search
# ----------------------------------

def depth_limited_search(state, goal, limit, path, visited):

    # Check goal
    if state == goal:
        return path

    # Depth limit reached
    if limit == 0:
        return None

    visited.add(state)

    # Expand current state
    for neighbor in get_neighbors(state):

        if neighbor not in visited:

            result = depth_limited_search(
                neighbor,
                goal,
                limit - 1,
                path + [neighbor],
                visited
            )

            if result is not None:
                return result

    # Remove state during backtracking
    visited.remove(state)

    return None


# ----------------------------------
# Iterative Deepening Search
# ----------------------------------

def ids(initial, goal):

    depth = 0

    while True:

        print("Searching at depth:", depth)

        visited = set()

        result = depth_limited_search(
            initial,
            goal,
            depth,
            [initial],
            visited
        )

        # Goal found
        if result is not None:
            return result, depth

        # Increase depth limit
        depth += 1


# ----------------------------------
# Main Program
# ----------------------------------

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

solution, depth = ids(initial, goal)

print("\nIDS SOLUTION FOUND")
print("Depth:", depth)
print("Number of moves:", len(solution) - 1)

print("\nSolution Path:")

for step, state in enumerate(solution):

    print("\nStep", step)
    display(state)
