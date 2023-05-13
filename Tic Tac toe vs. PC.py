#defining global veriables
#functions
from math import trunc
import random
import time
def init_board():
    global board
    board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]] 
    global positions
    positions = [
                [ [0,0],[0,1],[0,2]] , 
                [ [1,0],[1,1],[1,2]] , 
                [ [2,0],[2,1],[2,2]] ,
                [ [0,0],[1,0],[2,0]] ,
                [ [0,1],[1,1],[2,1]] ,
                [ [0,2],[1,2],[2,2]] ,
                [ [0,0],[1,1],[2,2]] ,
                [ [0,2],[1,1],[2,0]] 
                ] 
 
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
    global board_triplets
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

# put only where its empty
# if there is a triplets with 2 O's, place the computers piece in the empty space
# if there are 2 x's, put O in the empty space 
# if cant win, and cant block, find a triplet with one O
# if cant win, vant block, and cant find one O, find a random place to put the O. 
def next_move():
    i = 0
    succ = False
    print("the copmuter is thinking....")
    time.sleep(2)
    while i <= 7 and succ == False:
        trip1 = board[positions[i][0][0]][positions[i][0][1]]
        trip2 = board[positions[i][1][0]][positions[i][1][1]]
        trip3 = board[positions[i][2][0]][positions[i][2][1]]

        if (trip1 ==" "and trip2 ==  "o" and trip3 == "o"):
            board[positions[i][0][0]][positions[i][0][1]] = "o"
            succ = True
            print("hey1")
        elif (trip1 =="o"and trip2 ==  " " and trip3 == "o") :
            board[positions[i][1][0]][positions[i][1][1]] = "o"
            succ = True
            print("hey2")
        elif (trip1 =="o" and trip2 ==  "o" and trip3 == " ") :
            succ = True
            print("hey3")
            board[positions[i][2][0]][positions[i][2][1]] = "o"
        i += 1
    
    i = 0
    while i <= 7 and succ == False:
        trip1 = board[positions[i][0][0]][positions[i][0][1]]
        trip2 = board[positions[i][1][0]][positions[i][1][1]]
        trip3 = board[positions[i][2][0]][positions[i][2][1]]
        print(i,trip1,trip2,trip3)

        if (trip1 ==" "and trip2 ==  "x" and trip3 == "x"):
            board[positions[i][0][0]][positions[i][0][1]] = "o"
            succ = True
        elif (trip1 =="x"and trip2 ==  " " and trip3 == "x"):
             board[positions[i][1][0]][positions[i][1][1]] = "o"
             succ = True
        elif (trip1 =="x" and trip2 ==  "x" and trip3 == " "):
            succ = True
            board[positions[i][2][0]][positions[i][2][1]] = "o"
        i += 1
    while succ == False:
        row_random = random.randint(0,2)
        col_random = random.randint(0,2)
        if board[row_random][col_random] == " ":
            board[row_random][col_random] = "o"
            succ = True

    

        
       
    


#main loop

L = 0
turn = random.randint(1,2)
win = "false"
init_board()
play = input("do you wanna play tic tac toe?\n ")
if play.lower() == "no":
    print("Well, okay then. Goodbye")
elif play.lower() == "yes":
    print("choosing the starting player")
    time.sleep(2)
    if turn == 1:
        print("you are starting, you play as X")
    else:
        print("the computer is starting, you play as X")
    print_board()
    while win == "false" and L <= 9:
        if turn == 1:
            player_input_row = input("please enter the row you would like to play: ")
            player_input_col = input("please enter the col you would like to play: ")
            print(L)
            if get_input(int(player_input_row), int(player_input_col) , turn) == True:
                L += 1
                turn = 2
            else:
                print("this space is taken, please pick another one")
        else:
            next_move()
            turn = 1






        print_board()
        check_win()
    if win == "false":
        print("Its a tiee!!")   
            
else:
    print("Its a yes or no question")
print("done")
    

