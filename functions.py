

def list_unique(l):
    nums = []
    for num in l:
        if num != 0:
            if num in nums:
                return False
            else:
                nums.append(num)
    return True


def valid_row(sudoku, row_idx):
    row = sudoku[row_idx]
    return list_unique(row)


def valid_col(sudoku, col_idx):
    col = []
    for i in range(9):
        col.append(sudoku[i][col_idx])
    return list_unique(col)


def valid_square(sudoku, square_nr):
    square = []

    square_x, square_y = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)][square_nr]

    for y in range(square_y * 3, square_y * 3 + 3):
        for x in range(square_x * 3, square_x * 3 + 3):
            square.append(sudoku[y][x])
    return list_unique(square)

def print_matrix(sudoku, predefined):
    print("=====================================")
    for x, row in enumerate(sudoku):
        for y, val in enumerate(row):
            if val==0:
                val=" "
            if y % 3:
                print("| {} ".format(val),end='')
            else:
                print("‖ {} ".format(val),end='')
            print(end='')
        print('‖', end='\n')
        if (x + 1) % 3:
            print("-------------------------------------")
        else:
            print("=====================================")

def print_matrix_2(sudoku, predefined):
    answer_string=""
    for x, row in enumerate(sudoku):
        for y, val in enumerate(row):
            answer_string+=str(val)
        answer_string+="\n"
    return answer_string
def increase_x(x, y):
    x += 1
    if x > 8:
        x = 0
        y += 1
    return x, y


def decrease_x(x, y):
    x -= 1
    if x < 0:
        x = 8
        y -= 1
    return x, y
