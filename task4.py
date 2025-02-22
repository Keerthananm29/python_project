import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","",""],
              ["","","","","","",""],
              ["","","","","","",""],
              ["","","","","","",""],
              ["","","","","","",""],
              ["","","","","","",""]]

rows = 6
cols = 7

def printGameBoard():
    print("\n A B C D E F G ", end="")
    for x in range(rows):
        print("\n +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if(gameBoard[x][y] == "🔵"):
                print("",gameBoard[x][y], end=" |")
            elif(gameBoard[x][y] == "🔴"):
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end=" |")
        print("\n +----+----+----+----+----+----+----+")

def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

turnCounter = 0
while True:
    printGameBoard()
    if turnCounter % 2 == 0:
        turn = "🔵"
        player = "Player 1"
    else:
        turn = "🔴"
        player = "Player 2"
    
    print(f"\n{player}'s turn. Choose a column (A-G): ")
    choice = input().upper()
    if choice not in possibleLetters:
        print("Invalid choice. Please choose a letter between A and G.")
        continue
    
    column = possibleLetters.index(choice)
    for row in range(rows-1, -1, -1):
        if gameBoard[row][column] == "":
            modifyTurn((row, column), turn)
            turnCounter += 1
            break
    else:
        print("Column is full. Please choose another column.")
        continue
    
    # Check for win
    for row in range(rows):
        for col in range(cols):
            if gameBoard[row][col] != "":
                # Check horizontal
                if col < cols - 3 and gameBoard[row][col] == gameBoard[row][col+1] == gameBoard[row][col+2] == gameBoard[row][col+3]:
                    printGameBoard()
                    print(f"\n{player} wins!")
                    exit()
                # Check vertical
                if row < rows - 3 and gameBoard[row][col] == gameBoard[row+1][col] == gameBoard[row+2][col] == gameBoard[row+3][col]:
                    printGameBoard()
                    print(f"\n{player} wins!")
                    exit()
                # Check positive diagonal
                if row < rows - 3 and col < cols - 3 and gameBoard[row][col] == gameBoard[row+1][col+1] == gameBoard[row+2][col+2] == gameBoard[row+3][col+3]:
                    printGameBoard()
                    print(f"\n{player} wins!")
                    exit()
                # Check negative diagonal
                if row > 2 and col < cols - 3 and gameBoard[row][col] == gameBoard[row-1][col+1] == gameBoard[row-2][col+2] == gameBoard[row-3][col+3]:
                    printGameBoard()
                    print(f"\n{player} wins!")
                    exit()