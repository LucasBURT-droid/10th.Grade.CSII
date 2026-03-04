'''
Author: Lucas Burt 
Description: Classic Tic-Tac-Toe game in 3x3 grid, allowing two players to alternate turns placing 'X' and 'O' until their is three in a row or a draw  
Bugs: None Known 
Sources: Google, W3 Schools, Stack Overflow
Dates: 3/2/26 
Features: 
    - Game board that updates in real time 
    - Player input validation 
    - Win/Draw detection 
    - Game Loop
'''

def display_board(board):
    '''
    description - 
    args - 
    returns- 
    '''
#Print the board in a user-friendly format.
    for row in board:
        for cell in row: 
            print(cell,end=' ')
        print("\n")

def chooseplacement(): 
    '''
    description - 
    args - 
    returns- 
    '''
    mark = input('Would you like to be "X" or "O"? ').lower()
    if mark == 'x':
        p1 = 'x'
        p2 = 'o'
    else:
        p1 = 'o'
        p2 = 'x'
    print(f'Player1, you are {p1}.  That means Player2 is {p2}.  LETS PLAY!')
    return p1,p2

def get_player_move(board, player):
    '''
    description - 
    args - 
    returns- 
    '''
    while True: 
        try:
            move_input = input(f"Player {player}, enter your move (row and column): ")
            row_str, col_str = move_input.split()
            row = int(row_str) - 1
            col = int(col_str) - 1
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == 'E':
                    return row,col
                else:
                    print("That spot is already taken. Please try again.")
            else:
                print("Invalid row or column. Values must be between 1 and 3.")
        
        except ValueError:
            print("Invalid input format. Please enter two numbers separated by a space.")
    
    return p1, p2
def check_winner(board):

    win_row_combos = [
        # Horizontal 3x
        [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
        # Vertical 3x
        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
        # Diagonals 3x
        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
        ]

    for combo in win_row_combos: 
        cell1 = board[combo[0][0]][combo[0][1]]
        cell2 = board[combo[1][0]][combo[1][1]]
        cell3 = board[combo[2][0]][combo[2][1]]

        if cell1 != "E" and cell1 == cell2 == cell3:
            return cell1
    return None

def is_draw(board):

    if check_winner(board) is not None:
        return False

    for row in board:
        for cell in row:
            if cell == 'E':
                return False

    return True

def main():
    board = [['E','E','E'],
          ['E','E','E'],
          ['E','E','E']]

    p1, p2 = chooseplacement()
    current_player = p1

    while True:
        display_board(board)
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player

        #Finds winner 
        winner = check_winner(board)
        if winner: 
            display_board(board)
            print(f"Player {winner.upper()} wins!")
            break
        #If draw
        if is_draw(board):
            display_board(board)
            print("It's a draw!")        
        #Switch Players
        current_player = p1 if current_player == p2 else p2
        
        #Game loop (Printing before game done? need to fix)
        
        '''
        while True: 
            user_input = input("Do you want to play again? (y/n): ").strip().lower()
            if user_input == 'n':
                    print("Ok")
                    return 
            elif user_input == 'y':
                    break 
            else:
                    print("not a valid answer. Please enter 'y' or 'n'.")
        '''
main()


