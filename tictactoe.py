#printing the game board
# take playerinput
#check for win or tie
# switch the player
# check for win or tie again


import random
board = ["_","_","_",
        "_","_","_",
        "_","_","_",]
currentplayer="x"
winner = None
gameRunning =True        

#printing the game board
def printboard(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("_______")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("_______")
    print(board[6]+"|"+board[7]+"|"+board[8])
    print("_______")
printboard(board)

#take player input
def playerInput(board):
    inp=int(input("enter a number 1-9:"))
    if inp>=1 and inp <=9 and board[inp-1 ]=="_":
        board[inp-1]=currentplayer
    else:
        print("oops player is already in the spot")

#check for win or tie
def checkHorizontle(board):
    global winner
    if board[0]==board[1]==board[2] and board[1] !="_":
        winner =board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3] !="_":
        winner =board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6] !="_":
        winner =board[6]
        return True
    
def checkRow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0] !="_":
        winner =board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1] !="_":
        winner =board[1]
        return True
    elif board[2]==board[4]==board[8] and board[2] !="_":
        winner =board[2]
        return True
    
def checkdiag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0] !="_":
        winner =board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2] !="_":
        winner =board[2]
        return True
def checktie(board):
    global gameRunning
    if "_" not in board:
        printboard(board)
        print("it is a tie!")
        gameRunning=False


def checkwin():
    if checkdiag(board) or checkHorizontle(board) or checkRow(board):
        print("the winner is x")
#switch the player
def switchplayer():
    global currentplayer
    if currentplayer=="x":
        currentplayer="0"
    else:
        currentplayer="x"

#computer
def computer(board):
    while currentplayer=="0":
        position=random.randint(0,8)
        if board[position]=="_":
            board[position]="0"
            switchplayer()
    


while gameRunning:
    printboard(board)
    playerInput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)