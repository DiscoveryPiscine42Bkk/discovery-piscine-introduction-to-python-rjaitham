def checkmate(board):
    # Convert board into 2D grid
    rows = board.splitlines()
    n = len(rows)
    
    # Find the position of the King
    king_pos = None
    for i in range(n):
        for j in range(n):
            if rows[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    if not king_pos:
        return  # No King found, exit gracefully
    
    king_x, king_y = king_pos
    
    # Directions for each piece's movement
    directions_rook = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Vertical and horizontal
    directions_bishop = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonals
    directions_queen = directions_rook + directions_bishop  # Queen combines both Rook and Bishop
    directions_pawn = [(-1, -1), (-1, 1)]  # Pawn captures diagonally
    
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n
    
    # Check if any enemy piece can attack the King
    for i in range(n):
        for j in range(n):
            piece = rows[i][j]
            if piece == '.':
                continue  # Skip empty squares

            if piece == 'P':  # Check Pawn
                # Pawns can only attack diagonally, so we check if it can reach the King
                for dx, dy in directions_pawn:
                    if is_valid(i + dx, j + dy) and i + dx == king_x and j + dy == king_y:
                        print("Success")
                        return
            elif piece == 'R':  # Check Rook
                for dx, dy in directions_rook:
                    x, y = i, j
                    while is_valid(x + dx, y + dy):
                        x, y = x + dx, y + dy
                        if x == king_x and y == king_y:
                            print("Success")
                            return
                        if rows[x][y] != '.':
                            break  # Stop if we hit any other piece
            elif piece == 'B':  # Check Bishop
                for dx, dy in directions_bishop:
                    x, y = i, j
                    while is_valid(x + dx, y + dy):
                        x, y = x + dx, y + dy
                        if x == king_x and y == king_y:
                            print("Success")
                            return
                        if rows[x][y] != '.':
                            break  # Stop if we hit any other piece
            elif piece == 'Q':  # Check Queen
                for dx, dy in directions_queen:
                    x, y = i, j
                    while is_valid(x + dx, y + dy):
                        x, y = x + dx, y + dy
                        if x == king_x and y == king_y:
                            print("Success")
                            return
                        if rows[x][y] != '.':
                            break  # Stop if we hit any other piece
    # If we didn't find any check
    print("Fail")
    

def main():
    board = """\
..K.....
........
...R....
....Q...
........
........
........
........\
"""
    checkmate(board)

if __name__ == "__main__":
    main()