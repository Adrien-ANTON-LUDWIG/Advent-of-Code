import sys

# Length of the snake's body, the snake's head is included
BODY_LENGTH = 10

# Directions as letter to tuple
direction_to_tuple = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}

# Get the norm of a vector
def norm(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


# Round a float to the closest integer but the pivot is 0.4 (number can be negative)
def my_round(number):
    # If number is negative round the absolute value and return the negative value
    if number < 0:
        return -my_round(-number)

    if number - int(number) < 0.4:
        return int(number)
    else:
        return int(number) + 1


# Update the position of a body part. The frist part is called head and the following part is called tail.
# Check if the head is too far from the tail and move the tail if needed
def update_body_part_position(head_position, tail_position):
    # Get the direction from the tail to the head
    direction = (
        head_position[0] - tail_position[0],
        head_position[1] - tail_position[1],
    )

    # Get the distance from the tail to the head by getting the norm of the direction
    distance = norm(direction)

    if distance >= 2:
        # Normalize the direction
        direction = (direction[0] / distance, direction[1] / distance)

        # Round the direction with a custom rounding function to get diagonal directions
        direction = (my_round(direction[0]), my_round(direction[1]))

        # Move the tail
        tail_position = (
            tail_position[0] + direction[0],
            tail_position[1] + direction[1],
        )

    return tail_position


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    body_parts_positions = [(0, 0)] * BODY_LENGTH

    # Part 1: Tail is in fact the neck of the snake
    neck_visited_positions = set()

    # Part 2: Tail is at the end of the body
    tail_visited_positions = set()

    for line in input:
        # Get the direction and the number of steps
        direction, nb_of_steps = line.split()

        # Get the direction as a tuple
        direction = direction_to_tuple[direction]

        # Cast the number of steps to an integer
        nb_of_steps = int(nb_of_steps)

        # Move the head
        for step in range(nb_of_steps):

            # Move the head
            body_parts_positions[0] = (
                body_parts_positions[0][0] + direction[0],
                body_parts_positions[0][1] + direction[1],
            )

            # Move the rest of the body
            for i in range(1, BODY_LENGTH):
                body_parts_positions[i] = update_body_part_position(body_parts_positions[i - 1], body_parts_positions[i])

            neck_visited_positions.add(body_parts_positions[1])
            tail_visited_positions.add(body_parts_positions[-1])

    print(len(neck_visited_positions))
    print(len(tail_visited_positions))
