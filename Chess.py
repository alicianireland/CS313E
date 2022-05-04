#  File: Chess.py

#  Description: Find the number of solutions to N-Queens problem.

#  Student Name: Alicia Ireland

#  Student UT EID: ani324

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/22/2020

#  Date Last Modified:10/22/2020
import sys

class Queens (object):
    def __init__ (self, n):
        self.count = 0
        self.board = []
        self.n = n
        for i in range (self.n):
          row = []
          for j in range (self.n):
            row.append ('*')
          self.board.append (row)
# check if a position on the board is valid
    def is_valid (self, row, col):
        for i in range (self.n):
          if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
            return False
        for i in range (self.n):
          for j in range (self.n):
            row_diff = abs (row - i)
            col_diff = abs (col - j)
            if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
              return False
        return True


    # do the recursive backtracking
    def recursive_solve (self, col):
        if (col == self.n):
            self.count += 1
            return
        else:
          for i in range (self.n):
            if (self.is_valid (i, col)):
              self.board[i][col] = 'Q'
              self.recursive_solve(col + 1)
              self.board[i][col] = '*' 
          return self.count 
def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int (line)

    # create a chess board

    game = Queens (n)

    print(game.recursive_solve(0))
    
if __name__ == "__main__":
    main()
