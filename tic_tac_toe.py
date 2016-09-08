#!/usr/bin/python3

board = [1,2,3,4,5,6,7,8,9]
turn = 'X'
win = False

print("\n")
print("Welcome to TIC TAC TOE GAME")
print("---------------------------\n")
print("Starting with ", turn,"")

def showBoard():
    count = 1
    print('\n-----------')
    for b in board:
        if(count % 3 == 0):
            print('', b)
            print('-----------')
        else:
            print('',b,'|', end="")
        count+=1

def placing():
    print("[",turn, "]", end="")
    pos = int(input(" , which position you want to place : "))
    if(chkPlace(pos) is False):
        print("\n=====================================================")
        print("You cannot place on this position! Please try again.")
        print("=====================================================\n")
    else:
        place(pos)
    return

def place(pos):
    board[pos-1] = turn
    showBoard()
    print('>> ',turn, ' place at ', pos, '\n')

    if(chkWin() is not True):
        setTurn()

    return
def setTurn():
    global turn
    turn = (turn is 'X') and 'O' or 'X'
    return

def chkPlace(pos):
    if(board[pos-1] is 'X' or board[pos-1] is 'O'):
        return False
    else:
        return True

def chkWin():
    pos1 = board[0]

    pos2 = board[1]
    pos3 = board[2]

    pos4 = board[3]

    pos7 = board[6]

    global win
    #Hoz
    if((board[0] == pos1 and board[1] == pos1 and board[2] == pos1) or (board[3] == pos4 and board[4] == pos4 and board[5] == pos4) or (board[6] == pos7 and board[7] == pos7 and board[8] == pos7)):
        win = True
        return True
    #Vert
    if((board[0] == pos1 and board[4] == pos1 and board[7] == pos1) or (board[1] == pos2 and board[4] == pos2 and board[7] == pos2) or (board[2] == pos3 and board[5] == pos3 and board[8] == pos3)):
        win = True
        return True

    #\
    if((board[0] == pos1 and board[4] == pos1 and board[8] == pos1) or (board[2] == pos2 and board[4] == pos2 and board[6] == pos2)):
        win = True
        return True

    return False

def printEnd():
    print("\n==================")
    print("Game ended!\nThe winner is ", turn,"!")
    print("==================\n")

showBoard()
print()
while(win is not True):
    placing()

printEnd()
