import random 

'''
Author: Lucas Burt 
Description: A Python-based terminal game where you play against a computer opponent and try to sink their ships before your own are destroyed. 
Bugs: 0
Sources: Google, W3 Schools, Stack Overflow 
Dates: 4/27/26
Features (Bonus): Dots = Ships 
Log: 1.0 
'''

def display_board(board,user):

    '''
    description - displays board to the user 
    args - board, user 
    returns - n/a
    ''' 

    for row in board:
        for cell in row: 
            print(cell,end=' ')
        print("\n") 

    
   
def get_player_move(Pboard, player):
    '''
    description - Gets player to place 4 ships around the board
    args - Pboard, player
    returns - Pboard
    '''
    # 
    while True: 
        try:
            move_input = input(f"Player, place your ships (row and column. Ex. '1 1' ): ")
            row_str, col_str = move_input.split()
            row = int(row_str) - 1
            col = int(col_str) - 1
            if 0 <= row < 5 and 0 <= col < 5:
                if Pboard[row][col] == 'E': #checks if spot taken on board 
                    Pboard[row][col] = player
                    return Pboard
                else:
                    print("That spot is already taken. Please try again.") 
            else:
                print("Invalid row or column. Values must be between 1 and 5.")
        
        except ValueError:
            print("Invalid input format. Please enter two numbers separated by a space.") 
    #add move limit 

def robot_move(Gboard,robot): 

    '''
    description - 4 ships are randomly placed through a random.choice, then displayed. 
    args - Gboard, robot  
    returns - Gboard 
    ''' 
    #random possible coords 
    rplacements = [
    "1 1", "1 2", "1 3", "1 4", "1 5",
    "2 1", "2 2", "2 3", "2 4", "2 5",
    "3 1", "3 2", "3 3", "3 4", "3 5",
    "4 1", "4 2", "4 3", "4 4", "4 5",
    "5 1", "5 2", "5 3", "5 4", "5 5"
]
    #
    while True: 
        move_input = random.choice(rplacements)
        row_str, col_str = move_input.split()
        row = int(row_str) - 1
        col = int(col_str) - 1
        if Gboard[row][col] == 'E':
            Gboard[row][col] = robot
            return Gboard

def player_attack(Gboard,player,pcounter): #robot board, player attacks  
    '''
    description - player chooses 2 random coordinates on the robot board, attempting to hit and sink their ship
    args - GBoard, pcounter 
    returns - GBoard, pcounter 
    ''' 
    #
    try:
        move_input = input(f"Player, Choose your Attack (row and column. Ex. '1 1' ): ")
        row_str, col_str = move_input.split()
        row = int(row_str) - 1
        col = int(col_str) - 1
        if 0 <= row < 5 and 0 <= col < 5:           #
            if Gboard[row][col] == 'E':             #checks if spot taken on board 
                print("MISS!!")
                Gboard[row][col] = 'M'
            elif Gboard[row][col] == '🚢': 
                print("HIT!!!")
                Gboard[row][col] = 'H'
                pcounter = pcounter - 1 
            else:
                print("PLAYER ALREADY ATTACKED THIS SPOT!!") 
        return Gboard, pcounter

    except ValueError:
        print("Invalid input format. Please enter two numbers separated by a space.") 

def robotattack(Pboard,robot,rcounter): #player board, robot attacks.
    print('ok, now robot goes..')

    '''
    description - robot randomly chooses 2 coordinates on the player board, attempting to hit and sink their ships
    args - Pboard, rcounter 
    returns - Pboard, rcounter
    ''' 

    #
    attackposs = [
    "1 1", "1 2", "1 3", "1 4", "1 5",
    "2 1", "2 2", "2 3", "2 4", "2 5",
    "3 1", "3 2", "3 3", "3 4", "3 5",
    "4 1", "4 2", "4 3", "4 4", "4 5",
    "5 1", "5 2", "5 3", "5 4", "5 5"
]
    #manage robot guess
    move_input = random.choice(attackposs)                  #get random guess from list        
    row_str, col_str = move_input.split()
    row = int(row_str) - 1
    col = int(col_str) - 1
    if Pboard[row][col] == 'E':
        print("MISS!!")
        Pboard[row][col] = 'M'
    elif Pboard[row][col] == '🚢':
        print("HIT!!") 
        Pboard[row][col] = 'H'
        rcounter = rcounter - 1
       
    return Pboard, rcounter
    

def main(): 
    

    
    rcounter = 4                    #
    pcounter = 4                    #

    player = "🚢" 
    robot = "🚢"

    #Player board --> what is shown 
    Pboard =   [['E','E','E','E','E',],
                ['E','E','E','E','E',],
                ['E','E','E','E','E',],
                ['E','E','E','E','E',],
                ['E','E','E','E','E',],]


    #Hidden to player 
    Gboard =   [['E','E','E','E','E'],
                ['E','E','E','E','E'],
                ['E','E','E','E','E'],
                ['E','E','E','E','E'],
                ['E','E','E','E','E']]
    
    print("WELCOME TO BATTLESHIP PRIVATE 🫡, YOUR MISSON IS TO DESTROY THE OPPONENTS BATTLESHIPS BEFORE THEY DESTROY YOURS. GOOD LUCK.")

    print('PLAYER BOARD')
    display_board(Pboard,"player")
    print('OPPONENT BOARD')
    display_board(Gboard,"robot") 

    counter = 0
    while counter < 4:
        get_player_move(Pboard,player)          #put ships on board
        counter +=1

    counter = 0
    while counter < 4:
        robot_move(Gboard,robot)          #put ships on board
        counter +=1
    
    print("PLAYER MOVES")
    display_board(Pboard,player)        #ONLY DISPLAYING THIS 
    print("________________________")   
    print("ROBOT MOVES")            
    display_board(Gboard, robot_move)   #NOT FOR USER!!! FOR ME


    while True:                     #play game
        print(pcounter)
        Gboard, pcounter = player_attack(Gboard,player,pcounter)
        if pcounter == 0:
            print("PLAYER WON! :)")
            break
        print(rcounter)
        Pboard, rcounter = robotattack(Pboard,robot,rcounter)
        if rcounter == 0:
            print("ROBOT WON :(")
            break


           

main()