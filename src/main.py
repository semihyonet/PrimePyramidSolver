import PuzzleReader
import PuzzleLogic

puzzle_arr = PuzzleReader.puzzle_arr

class Solution: #A class for individual solutions. Which stores the path and can calculate the sum
    def __init__(self, sol_path):
        self.sol_path = sol_path

    def get_total(self): # Calculates the total of the individual solution
        total = 0
        for i in self.sol_path:
            total += i
        return total

    def get_path(self):
        return self.sol_path

    def print_path(self,puzzle):#Prints the Selected path like a pyramid
        string = ""
        for row in range(len(puzzle)):
            for i in range(int(len(puzzle) - row)):
                string += "\t"
            for number in puzzle[row]:
                if row < len(self.sol_path):
                    if (number == self.sol_path[row]):
                        string += "*"
                string += str(number)+"\t\t"
            string += "\n"
        print(string)


# puzzle_arr[row][column]
# This class solves the problem
class Puzzle_Solver():
    def __init__(self,puzzle_arr:list):
        self.puzzle = puzzle_arr

        self.row_len = len(puzzle_arr)
        self.solutions = []

    def set_solution(self, sol_path): #This stores all possible solutions inside self.solutions array
        self.solutions.append(Solution(sol_path))

    def get_solutions(self):
        return self.solutions


    def get_biggest_value_path(self):
        biggest = 0
        biggest_object = None
        for i in self.solutions:
            if i.get_total() > biggest:
                biggest = i.get_total()
                biggest_object = i
        return biggest_object

    def solve(self, path:list,row,col):#This is where the algorithm runs

        if (row < (self.row_len - 1)): #Checks if its the last row of the pyramid

            for i in (PuzzleLogic.legalMoves(col)): #This returns possible moves on the next row

                if not (PuzzleLogic.isPrime(self.puzzle[row+1][i])): #*THIS HANDLES THE 3RD REQUIREMENT OF THE QUESTION*

                    new_path = path.copy()  #getting a new array because this algorithm uses a recursive method
                    new_path.append(self.puzzle[row+1][i])

                    self.solve(new_path,row+1, i) #Recursively calls the function again
            #IMPORTANT
            #This set_solution method is only here because the question indicates that its not needed to arrive in to the last row
            #If the line bellow is deleted the algorithm will sellect solutions which arrived in to the last row.
            #self.set_solution(path) #

            return False  # This is not important whether its false or true does not have any consequence

        elif (row == self.row_len -1): #This is true when iteration arrives to the last row
            self.set_solution(path) #Sets the solution and continues to search
            return True # This is not important whether its false or true does not have any consequence


def main():

    level = puzzle_arr
    algorithm = Puzzle_Solver(puzzle_arr)

    algorithm.solve([level[0][0]], 0, 0)
    print("All achievable paths :")
    for i in algorithm.get_solutions():
        print(str(i.get_path()) + "Value: " +str(i.get_total()))

    print("--------------------------------------------------------------------------------------\n\n")

    biggest = algorithm.get_biggest_value_path()
    biggest.print_path(level)

    print("Path with the biggest value total:   "+str(biggest.get_path()),end="\t")
    print("Value total:   "+str(biggest.get_total()))


main()