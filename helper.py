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
