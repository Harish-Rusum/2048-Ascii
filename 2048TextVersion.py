import random
import sys
import os
from scripts.gravity import gravCalc
from scripts.collision import collisionCalc
from colorama import Fore, init

init(autoreset=True)

def startPos():
    mat = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    mat[random.choice([0,1,2,3])][random.choice([0,1,2,3])] = random.choice([2,4])
    
    i,j = 0,0
    while mat[i][j] != 0:
        i,j = random.choice([0,1,2,3]),random.choice([0,1,2,3])
    mat[i][j] = random.choice([2,4])
    return mat

def get_color(value):
    if value == 2:
        return Fore.GREEN
    elif value == 4:
        return Fore.YELLOW
    elif value == 8:
        return Fore.BLUE
    elif value == 16:
        return Fore.MAGENTA
    elif value == 32:
        return Fore.CYAN
    elif value == 64:
        return Fore.RED
    elif value == 128:
        return Fore.LIGHTGREEN_EX
    elif value == 256:
        return Fore.LIGHTYELLOW_EX
    elif value == 512:
        return Fore.LIGHTBLUE_EX
    elif value == 1024:
        return Fore.LIGHTMAGENTA_EX
    elif value == 2048:
        return Fore.LIGHTCYAN_EX
    else:
        return Fore.WHITE

def printb():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(len(board)):
        line = board[i]
        for j in range(len(line)):
            color = get_color(line[j])
            value = f"{line[j]}" if line[j] > 0 else "."
            print(f"{color}{value:<4}", end=" ")
        print()

def addNum(mat):
    i,j = 0,0
    while mat[i][j] != 0:
        i,j = random.choice([0,1,2,3]),random.choice([0,1,2,3])
    mat[i][j] = random.choice([2,4])
    return mat

board = startPos()
printb()
print()
while True:
    dir = input("Enter in the direction (WASD) : ").lower()
    if dir == "w":
        board = gravCalc(collisionCalc(gravCalc(board, "u"),"u"),"u")
        board = addNum(board)
        printb()
        print()
    elif dir == "d":
        board = gravCalc(collisionCalc(gravCalc(board, "r"),"r"),"r")
        board = addNum(board)
        printb()
        print()
    elif dir == "a":
        board = gravCalc(collisionCalc(gravCalc(board, "l"),"l"),"l")
        board = addNum(board)
        printb()
        print()
    elif dir == "s":
        board = gravCalc(collisionCalc(gravCalc(board, "d"),"d"),"d")
        board = addNum(board)
        printb()
        print()
    elif dir == "q":
        print()
        print("Game Over!")
        sys.exit()
    else:
        print("Invalid direction! Please enter 'W', 'A', 'S', or 'D'.")
