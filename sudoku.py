from functions import *
import time

sudoku = list(range(9))

for i in range(9):
    lines = open('SudokuPuzzles.txt').read().split('\n')
    inp = lines[i]
    sudoku[i] = list(map(int, list(inp)))
file = open("SudokuPuzzles.txt", "w+")
print("\nCalculating...\n")

predefined = [[False for i in range(9)] for j in range(9)]

for x in range(9):
    for y in range(9):
        if sudoku[y][x] != 0:
            predefined[y][x] = True

print_matrix(sudoku, predefined)

try_nr = [[1 for k in range(9)] for l in range(9)]
current_x = 0
current_y = 0

while predefined[current_y][current_x]:
    current_x, current_y = increase_x(current_x, current_y)
    if current_y > 8:
        print("sudoku seems to be solved already...")
        print_matrix(sudoku, predefined)
        #exit()
time1=time.time()
while True:
    try:
        sudoku[current_y][current_x] = try_nr[current_y][current_x]

        valid = True
        for i in range(9):
            valid = valid and valid_row(sudoku, i) and valid_col(sudoku, i) and valid_square(sudoku, i)

        if valid:
            current_x, current_y = increase_x(current_x, current_y)
            if current_y > 8:
                print("finished.\n")
                
                print_matrix(sudoku, predefined)
                #exit()
            while predefined[current_y][current_x]:
                current_x, current_y = increase_x(current_x, current_y)
                if current_y > 8:
                    print("finished.\n")
                    print_matrix(sudoku, predefined)
                    #exit()
        else:
            while True:
                if try_nr[current_y][current_x] == 9:
                    try_nr[current_y][current_x] = 1
                    sudoku[current_y][current_x] = 0
                    current_x, current_y = decrease_x(current_x, current_y)
                    if current_y < 0:
                        print("not solvable\n")
                        print_matrix(sudoku, predefined)
                        #exit()
                    while predefined[current_y][current_x]:
                        current_x, current_y = decrease_x(current_x, current_y)
                        if current_y < 0:
                            print("not solvable\n")
                            print_matrix(sudoku, predefined)
                            #exit()
                else:
                    try_nr[current_y][current_x] += 1
                    break
    except:
        file.write(print_matrix_2(sudoku, predefined))
        file.close()
        break
time2=time.time()

print("total time taken : {}".format(round(time2-time1,3)))