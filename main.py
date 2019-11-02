from copy import deepcopy
from helper import make_board

string_board = '''785 ∣ 439 ∣ 126 ∣
    612 ∣ 875 ∣ 349 ∣
    493 ∣ 621 ∣ 578 ∣
    ------------------
    357 ∣ 948 ∣ 261 ∣
    861 ∣ 752 ∣ 934 ∣
    904 ∣ 060 ∣ 005 ∣
    ------------------
    070 ∣ 300 ∣ 012 ∣
    120 ∣ 007 ∣ 400 ∣
    049 ∣ 206 ∣ 007 ∣
    ------------------
       '''

board = make_board(string_board)


def make_dict(board):

    dict = {}

    for row in range(len(board)):
        for column in range(len(board[0])):
            dict[(row, column)] = []

    return dict


def find_next_empty(board):
    for rowind, row in enumerate(board):
        for colind, element in enumerate(row):
            if element == 0:
                yield [rowind, colind]

# DID


dict = make_dict(board)

emptyplaceslist = list(find_next_empty(board))


def solve(bo):
    while True:
        print_board(bo)
        print("       ")
        pos = emptyplaceslist[0]
        if not pos:
            break
        bruh = 0
        for num in range(1, 10):
            if valid(bo, num, pos) and num not in dict[tuple(pos)]:
                bo[pos[0]][pos[1]] = num
                bruh = 1

        if bruh == 0:
            dict[tuple(pos)] = []

            previus_not_filled_place = (emptyplaceslist[emptyplaceslist.index(
                pos)-1][0], emptyplaceslist[emptyplaceslist.index(pos)-1][1])

            dict[previus_not_filled_place].append(bo[emptyplaceslist[emptyplaceslist.index(
                pos)-1][0]][emptyplaceslist[emptyplaceslist.index(pos)-1][1]])
            bo[previus_not_filled_place[0]][previus_not_filled_place[1]] = 0

    return None


def valid(bo, num, pos):

    if num != 0:
        for colind, col in enumerate(bo[pos[0]]):
            if col == num and colind != pos[1]:
                return False
        for rowind, row in enumerate(bo):
            if row[pos[1]] == num and rowind != pos[0]:
                return False
        for row in range(pos[0]//3*3, pos[0]//3*3+3):
            for col in range(pos[1]//3*3, pos[1]//3*3+3):
                if [row, col] != pos:
                    if bo[row][col] == num:
                        return False
    return True


def print_board(bo):
    for rowind, row in enumerate(bo):
        for colind, column in enumerate(row):
            print(column, end="")
            if (colind+1) % 3 == 0:
                print(" ∣ ", end="")
        print("")
        if (rowind+1) % 3 == 0:
            print("-"*(len(bo[0])+3*3))

# DID


solve(board)
print(board)
