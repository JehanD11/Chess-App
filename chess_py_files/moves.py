from chess_py_files.constants import BLOCKED_MOVE, ILLEGAL_MOVE
from chess_py_files.services import create_message


def rooks_moves(board, starting_pos, ending_pos) -> bool:
    if starting_pos[0] == ending_pos[0]:  # Meant to move vertically
        # First check the higher value to determine whether we move the piece up
        # or down the board
        down = starting_pos[1] if starting_pos[1] < ending_pos[1] else ending_pos[1]
        up = starting_pos[1] if starting_pos[1] > ending_pos[1] else ending_pos[1]

        for position in range(down + 1, up):
            # If there's a piece on that place, don't place the rook
            if board.board[starting_pos[0]][position] is not None:
                print(BLOCKED_MOVE)
                create_message(detail=BLOCKED_MOVE, messages=board.messages)
                return False
        return True

    else:  # Now let's check from left to right, or right to left
        # Check if we are to move left or right of the board
        left = starting_pos[0] if starting_pos[0] < ending_pos[0] else ending_pos[0]
        right = starting_pos[1] if starting_pos[1] > ending_pos[1] else ending_pos[1]

        # This check prevents the -1 list indexing possibility
        for position in range(left + 1, right):
            if board.board[position][starting_pos[1]] is not None:
                print(BLOCKED_MOVE)
                create_message(detail=BLOCKED_MOVE, messages=board.messages)
                return False

        return True


def bishops_moves(board, starting_pos, finishing_pos) -> bool:
    #ensures that the path is diagonal
    #(x1-y1) should equal (x2-y2)
    if abs(starting_pos[0] - finishing_pos[0]) != abs(
        starting_pos[1] - finishing_pos[1]
    ):
        print(ILLEGAL_MOVE)
        create_message(detail=ILLEGAL_MOVE, messages=board.messages)
        return False

    x_axis = 1 if finishing_pos[0] - starting_pos[0] > 0 else -1
    y_axis = 1 if finishing_pos[1] - starting_pos[1] > 0 else -1

    x_position = starting_pos[0] + x_axis
    y_position = starting_pos[1] + y_axis

    movement_possible = (
        x_position < finishing_pos[0] if x_axis == 1 else x_position > finishing_pos[0]
    )

    while movement_possible:
        # Check if the intended slot has a piece already
        if board.board[x_position][y_position] is not None:
            print(BLOCKED_MOVE + f" [{x_position}, {y_position}]")
            return False

        # Move piece diagonal
        x_position += x_axis
        y_position += y_axis

    return True
