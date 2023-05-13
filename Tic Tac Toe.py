#defining global veriables
#functions
import random
def init_board():
    global board
    board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]  

def print_board():
    print("*" * 20)
    print("    0    1    2 ")
    print(" 0 ", board[0][0] , " |", board[0][1], " |", board[0][2])
    print("  ", "-" * 15)
    print(" 1 ", board[1][0] , " |", board[1][1], "|", board[1][2])
    print("  ", "-" * 15)
    print(" 2 ", board[2][0] , " |", board[2][1], " |", board[2][2])

def get_input(row, col, turn):
    if board[row][col] == " ":
        if turn == 1:
            board[row][col] = 'x'
        else:
            board[row][col] = "O"
        return True
    else:
        return False

def check_win():
    board_triplets = []
    board_triplets.append(board[0])
    board_triplets.append(board[1])
    board_triplets.append(board[2])
    board_triplets.append([board[0][0], board[1][0], board[2][0]])
    board_triplets.append([board[0][1], board[1][1], board[2][1]])
    board_triplets.append([board[0][2], board[1][2], board[2][2]])
    board_triplets.append([board[0][0], board[1][1], board[2][2]])
    board_triplets.append([board[0][2], board[1][1], board[2][0]])
    for x in board_triplets:
        if x[0] == x[1] == x[2] and x != [" ", " ", " "]:
            global win 
            win = "true"
            print(x[0] , "won")
        else:
            None
            
    


#main loop
turn = random.randint(1,2)
win = "false"
i = 1
init_board()
play = input("Do you want to play Tic Tac Toe?: ")
if play.lower() == "no":
    print("Well, okay then. Goodbye")
elif play.lower() == "yes":
    print_board()
    while win == "false" and i <= 9:
        player_input_row = input("please enter the row you would like to play: ")
        player_input_col = input("please enter the col you would like to play: ")
        print(i)
        if get_input(int(player_input_row), int(player_input_col) , turn) == True:
            i += 1
            if turn == 1:
                turn += 1     
            else:
                turn -= 1
        else:
            print("this space is taken, please pick another one")
        print_board()
        check_win()
    if win == "false":
        print("Its a tiee!!")   
            
else:
    print("Its a yes or no question")
print("done")
    

