from copy import deepcopy
from helper import make_board

string_board = '''000 ∣ 065 ∣ 002 ∣ 
        501 ∣ 000 ∣ 830 ∣ 
        002 ∣ 080 ∣ 560 ∣ 
        ------------------
        003 ∣ 750 ∣ 090 ∣ 
        000 ∣ 040 ∣ 000 ∣ 
        070 ∣ 032 ∣ 100 ∣ 
        ------------------
        015 ∣ 020 ∣ 600 ∣ 
        028 ∣ 000 ∣ 401 ∣ 
        400 ∣ 510 ∣ 000 ∣ 
        ------------------'''

board = make_board(string_board)


def make_dict(emptyplaceslist):
    used_numbers = {}

    for item in emptyplaceslist:
        used_numbers[item] = []

    return used_numbers


def find_next_empty(board):
    for rowind, row in enumerate(board):
        for colind, element in enumerate(row):
            if element == 0:
                yield (rowind, colind)

# DID

emptyplaceslist = list(find_next_empty(board))

used_numbers = make_dict(emptyplaceslist)




def solve(board,emptyplaceslist):
    i=0
    while i<len(emptyplaceslist):
        pos = emptyplaceslist[i]
        bruh = 0
        for num in range(1, 10):
            if  num not in used_numbers[pos] and valid(board, num, pos):
               
                board[pos[0]][pos[1]] = num
                bruh = 1
                i+=1
                used_numbers[pos].append(num)
                break
        if bruh == 0:
            i-=1
            used_numbers[pos]=[]
            board[pos[0]][pos[1]] = 0
        
        if i<0: return False

    return True


def valid(board, num, pos):

    if num != 0:
        for colind, element in enumerate(board[pos[0]]):
            if element == num and colind != pos[1]:
                return False
        for rowind, row in enumerate(board):
            if row[pos[1]] == num and rowind != pos[0]:
                return False

        box_row_ind = pos[0]//3
        box_col_ind = pos[1]//3
        for row in range(box_row_ind*3, box_row_ind*3+3):
            for col in range(box_col_ind*3, box_col_ind*3+3):
                if board[row][col] == num and [row, col] != pos:
                    return False
    return True


def print_board(board):
    for rowind, row in enumerate(board):
        for colind, element in enumerate(row):
            print(element, end="")
            if (colind+1) % 3 == 0:
                print(" ∣ ", end="")
        print()
        if (rowind+1) % 3 == 0:
            print("-"*(len(board[0])+9))

# DID

solve(board,emptyplaceslist)
print_board(board)

