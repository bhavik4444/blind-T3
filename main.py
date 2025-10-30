
# creating the board
GRID_SIZE = 4

def main():
    
    board = create_board(GRID_SIZE)
    

def create_board(n: int) -> list:
    board = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        board.append(row)
    return board

def update_board(column: int, row: int, board: list, player_code: int) -> list:
    """ Gives back an updated board replacing x, y with player_code if cell empty 
    else return back None"""
    if board[row-1][column-1] == 0:
        board[row-1][column-1] = player_code
        return board
    else:
        return None
    
    
if __name__ == "__main__":
    main()