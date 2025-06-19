def checkmate(board):
    # Convert the board string into a list of rows for easier manipulation
    board = board.splitlines()
    
    # Find the position of the King ('K')
    king_pos = None
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    # If no King is found, return an error message
    if not king_pos:
        print("Error: King not found.")
        return
    
    kx, ky = king_pos
    
    # Directions for checking (vertical, horizontal, diagonal)
    directions = [
        (-1, 0), (1, 0),  # Vertical (up, down)
        (0, -1), (0, 1),  # Horizontal (left, right)
        (-1, -1), (1, 1), # Diagonal (top-left, bottom-right)
        (-1, 1), (1, -1)  # Diagonal (top-right, bottom-left)
    ]
    
    # Check if any piece can attack the King
    for dx, dy in directions:
        x, y = kx, ky
        while 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
            x += dx
            y += dy
            piece = board[x][y]
            if piece != '.':  # Found a piece
                if piece == 'P':  # Pawn can attack diagonally
                    if abs(dx) == 1 and abs(dy) == 1:
                        print("Success")
                        return
                elif piece == 'R':  # Rook can attack vertically or horizontally
                    if dx == 0 or dy == 0:
                        print("Success")
                        return
                elif piece == 'B':  # Bishop can attack diagonally
                    if abs(dx) == 1 and abs(dy) == 1:
                        print("Success")
                        return
                elif piece == 'Q':  # Queen can attack in all directions
                    if dx == 0 or dy == 0 or (abs(dx) == 1 and abs(dy) == 1):
                        print("Success")
                        return
                break  # Stop checking further in this direction

    # If no piece can attack the King, print "Fail"
    print("Fail")