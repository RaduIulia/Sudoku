from tkinter import *
from random import randint, shuffle
import gui

def check_grid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col] == 0:
          return False
  return True 

def solve_grid(grid):
  global counter
  for i in range(0,81):
    row = i // 9
    col = i % 9
    if grid[row][col] == 0:
      for value in range (1,10):
        if not(value in grid[row]):
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            square = []
            if row < 3:
              if col < 3:
                square = [grid[i][0:3] for i in range(0,3)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(0,3)]
              else:  
                square = [grid[i][6:9] for i in range(0,3)]
            elif row < 6:
              if col < 3:
                square = [grid[i][0:3] for i in range(3,6)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(3,6)]
              else:  
                square = [grid[i][6:9] for i in range(3,6)]
            else:
              if col < 3:
                square = [grid[i][0:3] for i in range(6,9)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(6,9)]
              else:  
                square = [grid[i][6:9] for i in range(6,9)]
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col] = value
              if check_grid(grid):
                counter += 1
                break
              else:
                if solve_grid(grid):
                  return True
      break
  grid[row][col] = 0  

def fill_grid(grid):
  global counter
  for i in range(0,81):
    row = i // 9
    col = i % 9
    if grid[row][col] == 0:
      shuffle(lista_numere)      
      for value in lista_numere:
        if not(value in grid[row]):
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            square=[]
            if row < 3:
              if col < 3:
                square = [grid[i][0:3] for i in range(0,3)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(0,3)]
              else:  
                square = [grid[i][6:9] for i in range(0,3)]
            elif row < 6:
              if col < 3:
                square = [grid[i][0:3] for i in range(3,6)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(3,6)]
              else:  
                square = [grid[i][6:9] for i in range(3,6)]
            else:
              if col < 3:
                square = [grid[i][0:3] for i in range(6,9)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(6,9)]
              else:  
                square = [grid[i][6:9] for i in range(6,9)]
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col] = value
              if check_grid(grid):
                return True
              else:
                if fill_grid(grid):
                  return True
      break
  grid[row][col] = 0      

def set_copy_grid(g):
 global copy_grid
 copy_grid = g

def get_copy_grid():
  return copy_grid

def generare_sudoku_rezolvabil():
 global lista_numere, counter, grid
 lista_numere = [1,2,3,4,5,6,7,8,9]
 grid = []
 for i in range(9):
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
 fill_grid(grid)
 counter = 1
 print(grid)
 while gui.attempts>0:
  row = randint(0,8)
  col = randint(0,8)
  while grid[row][col]==0:
    row = randint(0,8)
    col = randint(0,8) 
  backup = grid[row][col]
  grid[row][col] = 0
  copyGrid = []
  for r in range(0,9):
     copyGrid.append([])
     for c in range(0,9):
        copyGrid[r].append(grid[r][c])
  counter = 0      
  solve_grid(copyGrid)   
  if counter != 1:
    grid[row][col] = backup
    gui.attempts -= 1
 set_copy_grid(grid)

def emptyCell():
 for row in range(9):
  for column in range(9):
    if grid[row][column] == 0:
      return (row,column)
 return None

def isValidSudoku(board):
  N = 9
  ok_gol = 0
  ok_interval = 0
  global message
  message = ""
  for i in range(0, N):
    for j in range(0, N):
      if ((board[i][j] <= 0) or
          (board[i][j] > 9)):
        if board[i][j] == 0:
          ok_gol = 1
        else:
          ok_interval = 1
  if ok_gol == 1:
   message = message + "Empty Cells! "
  if ok_interval == 1:
   message = message + "Values out of 1-9 interval!"
  set_message(message)
  if ok_interval or ok_gol:
    return False
  unique = [False] * (N + 1)
  for i in range(0, N):
    for m in range(0, N + 1):
      unique[m] = False
    for j in range(0, N):
      Z = board[i][j]
      if (unique[Z] == True):
        message = "Duplicates on row "+str(i)
        set_message(message)
        return False
      unique[Z] = True
  for i in range(0, N):
    for m in range(0, N + 1):
      unique[m] = False
    for j in range(0, N):
      Z = board[j][i]
      if (unique[Z] == True):
        message = "Duplicates on column "+str(j)
        set_message(message)
        return False
      unique[Z] = True
  for i in range(0, N - 2, 3):
    for j in range(0, N - 2, 3):
      for m in range(0, N + 1):
        unique[m] = False
      for k in range(0, 3):
        for l in range(0, 3):
          X = i + k
          Y = j + l
          Z = board[X][Y]
          if (unique[Z] == True):
            message = "Duplicates in block"
            set_message(message)
            return False
          unique[Z] = True
  message = "You've solved Sudoku, congratulations!"
  set_message(message)
  return True

def set_message(x):
 global mesaj_sudoku
 mesaj_sudoku = x

def get_message():
 global mesaj_sudoku
 return mesaj_sudoku

def main():
 gui.start_menu()

if __name__ == '__main__':
    main()