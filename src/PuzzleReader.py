import Macros
import os

file_dir = Macros.file_dir

puzzle_file = open(os.path.dirname(os.path.abspath(__file__)) +"/" +file_dir)

puzzle = puzzle_file.read()
puzzle = puzzle.split("\n")

puzzle_arr = []
line_index = 0


for puzzle_row in puzzle:
    if puzzle_row == "\n" or puzzle_row == "":
        pass
    else:
        space = True
        puzzle_arr.append([])
        if len(puzzle_row) == 0:
            pass
        else:

            for i in range(len(puzzle_row)):
                if (puzzle_row[i] == " ") or (puzzle_row[i] == "\t"):
                    space = True
                    pass
                elif  (space):
                    space= False
                    puzzle_element = puzzle_row[i]
                    number_index = i
                    while True:
                        if (number_index + 1 == len(puzzle_row)) or (puzzle_row[number_index+1] == " ") or (puzzle_row[number_index+1] == "\t"):
                            puzzle_arr[line_index].append(int(puzzle_element))
                            False
                            break
                        else:
                            number_index += 1
                            puzzle_element += puzzle_row[number_index]

            line_index += 1
