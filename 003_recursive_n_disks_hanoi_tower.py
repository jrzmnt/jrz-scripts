"""
Solves the Tower of Hanoi problem recursively.

Parameters:
- n (int): The number of disks to move.
- source (list): The source peg (where the disks start).
- auxiliary (list): The auxiliary peg (used for temporary storage).
- target (list): The target peg (where the disks should end up).

Returns:
- None: The function modifies the pegs in place and prints the progress.

Algorithm:
1. Move n - 1 disks from the source peg to the auxiliary peg.
2. Move the nth disk from the source peg to the target peg.
3. Move the n - 1 disks from the auxiliary peg to the target peg.

Example:
    NUMBER_OF_DISKS = 3
    A = [3, 2, 1]  # Source peg
    B = []         # Auxiliary peg
    C = []         # Target peg
    move(NUMBER_OF_DISKS, A, B, C)
    # Displays the step-by-step movement of disks from A to C.
"""


def move(n, source, auxiliary, target):
    if n <= 0:
        return

    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)

    # move the nth disk from source to target
    target.append(source.pop())

    # display our progress
    print(A, B, C, "\n")

    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1, auxiliary, source, target)


NUMBER_OF_DISKS = 7
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)
