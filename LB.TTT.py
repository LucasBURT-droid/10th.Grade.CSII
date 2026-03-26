'''
Author: Lucas Burt 
Description: Tic-Tac-Toe game in 3x3 grid in excel, allowing two players to alternate turns placing 'X' and 'O' until their is three in a row, or a draw --> where the board is filled entirley.    
Bugs:
Sources: Google, W3 Schools, Stack Overflow 
Dates: 3/2/26 
Features: 
    - Game board with updates in real time 
    - Player input validation 
    - Win/Draw detection 
    - User can play again
'''

def display_board(board):
    '''
    description - Print the current board state in a readable format
    args - board: 3x3 grid reserve in excel, "E" marks empty spaces  
    returns- board 
    '''
#Print the board in a user-friendly format.
    for row in board:
        for cell in row: 
            print(cell,end=' ')
        print("\n")

def choose_placement(): 
    '''
    description - Prompt the player to pick "X" or "O", then validates input. 
    args - void 
    returns- p1 and p2 
    '''
    
    p1 = "" #declaration of p1 
    p2 = "" #declaration of p2
    
    while True:
            mark = input('Would you like to be "X" or "O"? ').lower() #User choice 
            if mark == 'x':
                p1 = 'x'
                p2 = 'o'
                print(f'Player1, you are {p1}.  That means Player2 is {p2}.  LETS PLAY!')
                break #Ends loop
            elif mark == 'o': 
                p1 = 'o' 
                p2 = 'x'
                print(f'Player1, you are {p1}.  That means Player2 is {p2}.  LETS PLAY!')
                break #Ends loop
            else:
                print("Invalid input. Please choose between X or O") #reloops function 
                
            

    return p1,p2

def get_player_move(board, player):
    '''
    description - gets players move, updates the 3x3 board with move for player, checks to make sure placement is valid
    args - board: 3x3 grid reserve in excel, player: split between "p1" and "p2" determines between "X" and "O" rotates player each move 
    returns - row,col
    '''
    while True: 
        try:
            move_input = input(f"Player {player}, enter your move (row and column. Ex. '1 1' ): ")
            row_str, col_str = move_input.split()
            row = int(row_str) - 1
            col = int(col_str) - 1
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == 'E': #checks if spot taken on board 
                    return row,col
                else:
                    print("That spot is already taken. Please try again.") 
            else:
                print("Invalid row or column. Values must be between 1 and 3.")
        
        except ValueError:
            print("Invalid input format. Please enter two numbers separated by a space.")
    
    return p1, p2
def check_winner(board):
    '''
    description - Gets win combos from the tuple, either 3x Horizontally, 3x Vertically, 3x Diagonally  
    args - board: 3x3 grid reserve in excell 
    returns- None (returns winner in main)
    '''

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
    '''
    description - after no detected win combos, this code determines if there is a draw
    args - 3x3 grid reserve in excell 
    returns- True 
    '''

    #if no player wins after board is full --> "draw" is declared
    if check_winner(board) is not None:
        return False
    for row in board:
        for cell in row:
            if cell == 'E':
                return False

    return True

def clear_board(board): 

    '''
    description - clears/resets board (if user chooses to post game) by filling it out with "E" --> signifying an empty space
    args - 3x3 grid reserve in excel 
    returns- cleared board 
    '''

    for row in range(0,3):  
        for col in range(0,3):
            board[row][col] = 'E'

def main():
    '''
    description - Main module 
    args - 
    returns- board, p1/p2, winconds
    '''
    board = [['E','E','E'],
          ['E','E','E'],
          ['E','E','E']]

    p1, p2 = choose_placement()
    current_player = p1

    game = True

    while game == True:
        
        while True:
            display_board(board) #displays board to user, uses pm function to get player's move, and displays on board  
            row, col = get_player_move(board, current_player)
            board[row][col] = current_player

            #winner 
            winner = check_winner(board)
            if winner: 
                display_board(board)
                print(f"Player {winner.upper()} wins!")
                break
            #draw
            if is_draw(board):
                display_board(board)
                print("It's a draw :(")
                break        
            #players
            current_player = p1 if current_player == p2 else p2


        #play again bonus 
        play_again = input("Would you like to play again?: y/n ").lower()
        if play_again == "y": 
            clear_board(board) #using cb function 
        elif play_again == "n": 
            print("Goodbye, thanks for playing!")
            game = False
            break 
        else: 
            print("Invlaid response, please choose between y and n")

    
                
main()


