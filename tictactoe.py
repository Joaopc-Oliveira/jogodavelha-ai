X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action: cell is already occupied")

    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    return not any(EMPTY in row for row in board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        value, best_action = max_value(board, -float('inf'), float('inf'))
    else:
        value, best_action = min_value(board, -float('inf'), float('inf'))

    return best_action

def max_value(board, alpha, beta):
    """
    Returns the maximum value for the current board state, and the associated action.
    """
    if terminal(board):
        return utility(board), None
    v = -float('inf')
    best_action = None
    for action in actions(board):
        min_result, _ = min_value(result(board, action), alpha, beta)
        if min_result > v:
            v = min_result
            best_action = action
        alpha = max(alpha, v)
        if v >= beta:
            break
    return v, best_action

def min_value(board, alpha, beta):
    """
    Returns the minimum value for the current board state, and the associated action.
    """
    if terminal(board):
        return utility(board), None
    v = float('inf')
    best_action = None
    for action in actions(board):
        max_result, _ = max_value(result(board, action), alpha, beta)
        if max_result < v:
            v = max_result
            best_action = action
        beta = min(beta, v)
        if v <= alpha:
            break
    return v, best_action
