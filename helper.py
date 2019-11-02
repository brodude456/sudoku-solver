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
        ------------------'''


def make_board(str_br):
    cleaned_str_rows = str_br.split("\n")
    board = []
    for row in cleaned_str_rows:
        if "∣" in row:
            cleaned_str_column = row.split("∣")
            list1 = []
            for element in cleaned_str_column:
                for number in element.strip():
                    list1.append(int(number))
            board.append(list1)
    return board
