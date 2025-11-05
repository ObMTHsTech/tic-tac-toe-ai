def play(board):
    # Determine who's turn it is
    x_count = board.count('x')
    o_count = board.count('o')
    current = 'x' if x_count == o_count else 'o'

    # Winning combinations
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    # 1. Try to win
    for a, b, c in wins:
        line = [board[a], board[b], board[c]]
        if line.count(current) == 2 and line.count('') == 1:
            return [a, b, c][line.index('')]

    # 2. Try to block opponent's win
    opponent = 'o' if current == 'x' else 'x'
    for a, b, c in wins:
        line = [board[a], board[b], board[c]]
        if line.count(opponent) == 2 and line.count('') == 1:
            return [a, b, c][line.index('')]

    # 3. Take center if available
    if board[4] == '':
        return 4

    # 4. Take any corner if available
    for i in [0, 2, 6, 8]:
        if board[i] == '':
            return i

    # 5. Take any remaining empty spot
    for i in range(9):
        if board[i] == '':
            return i
