from chess_py_files.constants import (
    BISHOP,
    BLOCKED_MOVE,
    ILLEGAL_MOVE,
    KING,
    KNIGHT,
    PAWN,
    QUEEN,
    ROOK,
)
from chess_py_files.moves import bishops_moves, rooks_moves
from chess_py_files.services import create_message


class ChessPiece:

    def __init__(self, color) -> None:
        self.name = ""
        self.color = color

    def is_valid_move(self, board, starting_position, finishing_position) -> bool:
        return False

    def is_white(self):
        return self.color

    def __str__(self) -> str:
        return self.name


# THE ROOK
class Rook(ChessPiece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.name = ROOK

    # Override the default method
    def is_valid_move(self, board, starting_position, finishing_position) -> bool:
        if (
            starting_position[0] == finishing_position[0]
            or starting_position[1] == finishing_position[1]
        ):
            return rooks_moves(
                board=board,
                starting_pos=starting_position,
                ending_pos=finishing_position,
            )

        # If move doesn't check,
        create_message(detail=ILLEGAL_MOVE, messages=board.messages)
        print(ILLEGAL_MOVE)
        return False


# THE KNIGHT
class Knight(ChessPiece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.name = KNIGHT

    # Call the move validation method
    def is_valid_move(self, board, starting_position, finishing_position) -> bool:
        if (
            abs(starting_position[0] - finishing_position[0]) == 2
            and abs(starting_position[1] - finishing_position[1]) == 1
        ):
            return True

        if (
            abs(starting_position[1] - finishing_position[1]) == 1
            and abs(starting_position[1] - finishing_position[1]) == 2
        ):
            return True
        create_message(detail=ILLEGAL_MOVE, messages=board.messages)
        print(ILLEGAL_MOVE)
        return False


# THE BISHOP
class Bishop(ChessPiece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.name = BISHOP

    def is_valid_move(self, board, starting_position, finishing_position) -> bool:
        return bishops_moves(
            board=board,
            starting_pos=starting_position,
            finishing_pos=finishing_position,
        )


# THE QUEEN
class Queen(ChessPiece):

    def __init__(self, color) -> None:
        super().__init__(color)
        self.name = QUEEN

    def is_valid_move(self, board, starting_position, finishing_position) -> bool:
        # Along the axis like a rook
        if (starting_position[0] == finishing_position[0]) or (
            starting_position[0] == finishing_position[1]
        ):
            return rooks_moves(
                board=board,
                starting_pos=starting_position,
                finishing_position=finishing_position,
            )

        # Diagonally like a bishop
        if abs(starting_position[0] - finishing_position[0]) == abs(
            starting_position[1] - finishing_position[1]
        ):
            return bishops_moves(
                board=board,
                starting_pos=starting_position,
                finishing_pos=finishing_position,
            )


# THE KING
class King(ChessPiece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.name = KING

    def is_valid_move(self, board, starting_position, finishing_position) -> bool:
        # If one step diagonally or along a line. On either axis
        if (abs(starting_position[0] - finishing_position[0]) == 1) or (
            starting_position[0] - finishing_position[0] == 0
        ):
            if (abs(starting_position[1] - finishing_position[1]) == 1) or (
                starting_position[1] - finishing_position[1] == 0
            ):
                return True

        create_message(detail=ILLEGAL_MOVE, messages=board.messages)
        print(ILLEGAL_MOVE)
        return False


# THE PAWN
class Pawn(ChessPiece):

    def __init__(self, color) -> None:
        super().__init__(color)
        self.name = PAWN
        self.first_move = True

    def is_valid_move(self, board, starting_position, finishing_position) -> bool:
        # Prevent from capturing your own pieces
        if self.color:
            # Check diagonally
            if starting_position[0] == (finishing_position[0] + 1) and (
                (starting_position[1] == finishing_position[1] + 1)
                or starting_position[1] == finishing_position[1] - 1
            ):
                if (
                    board.board[finishing_position[0]][finishing_position[1]]
                    is not None
                ):
                    self.first_move = False
                    return True
                create_message(detail=ILLEGAL_MOVE, messages=board.messages)
                print(ILLEGAL_MOVE)
                return False

            # Check forward movements
            if starting_position[1] == finishing_position[1]:
                if (
                    starting_position[0] - finishing_position[0] == 2
                    and self.first_move
                ) or (starting_position[0] - finishing_position[0] == 1):
                    for pos in range(
                        starting_position[0] - 1, finishing_position[0] - 1, -1
                    ):
                        if board.board[pos][starting_position[1]] is not None:
                            create_message(detail=ILLEGAL_MOVE, messages=board.messages)
                            print(BLOCKED_MOVE)
                            return False

                    # GHOST PAWN HERE
                    self.first_move = False
                    return True
                create_message(ILLEGAL_MOVE)
                print(ILLEGAL_MOVE)
                return False
            return False

        else:
            if (starting_position[0] == (finishing_position[0] - 1)) and (
                (starting_position[1] == finishing_position[1] - 1)
                or (starting_position[1] == (finishing_position[1] + 1))
            ):
                if (
                    board.board[finishing_position[0]][finishing_position[1]]
                    is not None
                ):
                    self.first_move = False
                    return True

                print(ILLEGAL_MOVE)
                return False

            if starting_position[1] == finishing_position[1]:
                if (
                    (finishing_position[0] - starting_position[0] == 2)
                    and self.first_move
                ) or (finishing_position[0] - starting_position[0] == 1):
                    for pos in range(
                        starting_position[0] + 1, finishing_position[0] + 1
                    ):
                        if board.board[pos][starting_position[1]] is not None:
                            create_message(detail=ILLEGAL_MOVE, messages=board.messages)
                            print(ILLEGAL_MOVE)
                            return False

                    # GHOST PAWN HERE

                    self.first_move = False
                    return True

                create_message(detail=ILLEGAL_MOVE, messages=board.messages)
                print(ILLEGAL_MOVE)
                return False

            create_message(detail=ILLEGAL_MOVE, messages=board.messages)
            print(ILLEGAL_MOVE)
            return False
