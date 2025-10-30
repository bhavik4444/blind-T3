
# creating the board
GRID_SIZE = 4

def main():
    
    board = create_board(GRID_SIZE)
    print(board)

def create_board(n: int) -> list:
    board = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        board.append(row)
    return board

if __name__ == "__main__":
    main()