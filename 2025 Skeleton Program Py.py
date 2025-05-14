# Skeleton Program for Oxford AQA International GCSE Computer Science Paper 1
# Developed using Python 3.12
# To be pre-released to centres
# Also available in C# and Visual Basic

import random

EMPTY = " "
OBSTACLE = "#"
GOAL = "@"
UP = "^"
RIGHT = ">"
DOWN = "v"
LEFT = "<"
WIDTH = 22
HEIGHT = 11
GOAL_ROW = 9
GOAL_COLUMN = 20
TURN_RIGHT = 90
TURN_LEFT = -90

board = []

pointerRow = 1
pointerColumn = 1
direction = RIGHT
errorCode = 0

def CreateBoard(randomChance):
    global board
    board = []
    for row in range(HEIGHT):
        board.append([])
        for column in range(WIDTH):
            if column == 0 or column == WIDTH - 1 or row == 0 or row == HEIGHT - 1:
                board[row].append(OBSTACLE)
            else:
                if randomChance > random.randint(0, 99):
                    board[row].append(OBSTACLE)
                else:
                    board[row].append(EMPTY)
    board[GOAL_ROW][GOAL_COLUMN] = GOAL

def CreateExampleBoard():
    CreateBoard(0)
    board[1][4] = OBSTACLE
    board[1][6] = OBSTACLE
    board[2][13] = OBSTACLE
    board[2][15] = OBSTACLE
    board[2][17] = OBSTACLE
    board[3][4] = OBSTACLE
    board[3][17] = OBSTACLE
    board[3][20] = OBSTACLE
    board[4][7] = OBSTACLE
    board[5][11] = OBSTACLE
    board[5][12] = OBSTACLE
    board[5][13] = OBSTACLE
    board[6][15] = OBSTACLE
    board[7][3] = OBSTACLE
    board[7][19] = OBSTACLE
    board[8][1] = OBSTACLE
    board[8][17] = OBSTACLE
    board[9][7] = OBSTACLE
    board[9][9] = OBSTACLE

def DrawBoard():
    for row in range(HEIGHT):
        for column in range(WIDTH):
            if row == pointerRow and column == pointerColumn:
                print(direction, end=" ")
            else:
                print(board[row][column], end=" ")
        print()

def CheckForward():
    if direction == UP:
        if board[pointerRow - 1][pointerColumn] == OBSTACLE:
            return False
        else:
            return True
    elif direction == RIGHT:
        if board[pointerRow][pointerColumn + 1] == OBSTACLE:
            return False
        else:
            return True
    elif direction == DOWN:
        if board[pointerRow + 1][pointerColumn] == OBSTACLE:
            return False
        else:
            return True
    elif direction == LEFT:
        if board[pointerRow][pointerColumn - 1] == OBSTACLE:
            return False
        else:
            return True
    else:
        return False

def MoveForward():
    global pointerRow
    global pointerColumn
    global errorCode
    if direction == UP:
        pointerRow = pointerRow - 1
    elif direction == RIGHT:
        pointerColumn = pointerColumn + 1
    elif direction == DOWN:
        pointerRow = pointerRow + 1
    elif direction == LEFT:
        pointerColumn = pointerColumn - 1

def Turn(rotation):
    global errorCode
    directions = [UP, RIGHT, DOWN, LEFT]
    directionIndex = directions.index(direction)
    if rotation == TURN_RIGHT:
        newDirection = directions[(directionIndex + 1) % 4]
        return newDirection
    elif rotation == TURN_LEFT:
        newDirection = directions[(directionIndex + 3) % 4]
        return newDirection
    else:
        errorCode = 1
        return direction

def ProcessForward(count):
    global pointerRow
    global pointerColumn
    global errorCode
    oldRow = pointerRow
    oldColumn = pointerColumn
    for x in range(count):
        if CheckForward() == True:
            MoveForward()
        else:
            pointerRow = oldRow
            pointerColumn = oldColumn
            errorCode = 1
            break
    
def SpecialMove():
    global pointerRow
    global pointerColumn

def ProcessInput(command):
    global direction
    global errorCode
    errorCode = 0
    parts = command.split()
    if parts[0] == "FD":
        if len(parts) == 1:
            ProcessForward(1)
        else:
            ProcessForward(int(parts[1]))
    elif parts[0] == "RT":
        direction = Turn(TURN_RIGHT)
    elif parts[0] == "LT":
        direction = Turn(TURN_LEFT)
    elif parts[0] == "SPC":
        SpecialMove()
    elif parts[0] != "GO":
        errorCode = 1

def DisplayMenu():
    print("1: Play using a blank board")
    print("2. Play using the example board")
    print("3: Play using a random board")
    print("9: Exit the program")

def Main():
    global pointerRow
    global pointerColumn
    global direction
    global errorCode
    playAgain = True
    while playAgain == True:
        pointerRow = 1
        pointerColumn = 1
        direction = RIGHT
        errorCode = 0
        gameOver = False
        DisplayMenu()
        choice = input("Enter selection: ")
        if choice == "1":
            CreateBoard(0)
        elif choice == "2":
            CreateExampleBoard()
        elif choice == "3":
            CreateBoard(10)
        else:
            gameOver = True
        nextCommand = 1
        totalCommands = 0
        while gameOver == False:
            DrawBoard()
            command = ""
            commands = []
            while command != "GO":
                command = input(f"{nextCommand}: ").upper()
                nextCommand = nextCommand + 1
                totalCommands = totalCommands + 1
                commands.append(command)
            nextCommand = 1
            for x in range(len(commands)):
                ProcessInput(commands[x])
                if errorCode == 1:
                    print(f"Could not execute line {x + 1} ('{commands[x]}')")
            if pointerRow == GOAL_ROW and pointerColumn == GOAL_COLUMN:
                print()
                print(f"Complete in {totalCommands} commands")
                DrawBoard()
                gameOver = True
        repeat = input("Exit the program? (Y/N): ").upper()
        if repeat == "Y":
            playAgain = False
            input()

if __name__ == "__main__":
    Main()
