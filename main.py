from tkinter import *
from random import randint, shuffle
import time
from tkinter import messagebox
from functools import partial
import re 

def check_grid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False
  return True 

def solve_grid(grid):
  global counter
  #Find next empty cell
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      for value in range (1,10):
        #Check that this value has not already be used on this row
        if not(value in grid[row]):
          #Check that this value has not already be used on this column
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            #Identify which of the 9 squares we are working on
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
            #Check that this value has not already be used on this 3x3 square
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if check_grid(grid):
                counter+=1
                break
              else:
                if solve_grid(grid):
                  return True
      break
  grid[row][col]=0  

def fill_grid(grid):
  global counter
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      shuffle(lista_numere)      
      for value in lista_numere:
        #Check that this value has not already be used on this row
        if not(value in grid[row]):
          #Check that this value has not already be used on this column
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            #Identify which of the 9 squares we are working on
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
            #Check that this value has not already be used on this 3x3 square
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if check_grid(grid):
                return True
              else:
                if fill_grid(grid):
                  return True
      break
  grid[row][col]=0           

def generare_sudoku_rezolvabil():
 global lista_numere, counter,grid
 lista_numere=[1,2,3,4,5,6,7,8,9]
 grid = []
 for i in range(9):
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
 fill_grid(grid)
 print(grid)
 attempts = 5 
 counter=1
 while attempts>0:
  row = randint(0,8)
  col = randint(0,8)
  while grid[row][col]==0:
    row = randint(0,8)
    col = randint(0,8) 
  backup = grid[row][col]
  grid[row][col]=0
  copyGrid = []
  for r in range(0,9):
     copyGrid.append([])
     for c in range(0,9):
        copyGrid[r].append(grid[r][c])
  counter=0      
  solve_grid(copyGrid)   
  if counter!=1:
    grid[row][col]=backup
    attempts -= 1
 print(grid)

def set_temp(minute,second):
  global temp
  temp = int(minute.get())*60 + int(second.get())
  
def setare_valori_timer(minute,second):
 if get_variabila_dificultate() == 1:
  minute.set("20")
  second.set("00")
 if get_variabila_dificultate() == 2:
  minute.set("10")
  second.set("00")
 if get_variabila_dificultate() == 3:
  minute.set("00")
  second.set("05")
 set_temp(minute,second)

def grid_checker():
 for row in range(9):
  for col in range(9):
    if board[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
        board[row][col].set('')

def clear():
 for row in range(9):
  for col in range(9):
    if copy_grid[row][col] == 0:
     board[row][col].delete(0, END)
 grid = copy_grid

def add_label_timer(game_grid):
 timer = Frame(game_grid, bg='white')
 timer.pack()
 timeLabel= Label(timer, font=("Arial",15,""),text="Sudoku Time Remaining: ")
 timeLabel.pack(side=LEFT)
 mins_box = Label( timer,font=("Arial",15,""),textvariable=minute)
 mins_box.pack(side=LEFT)
 timeLabel= Label(timer, font=("Arial",15,""),text=":")
 timeLabel.pack(side=LEFT)
 sec_box = Label(timer, font=("Arial",15,""),textvariable=second)
 sec_box.pack(side=LEFT)

def emptyCell():
 for row in range(9):
  for column in range(9):
    if grid[row][column] == 0:
      return (row,column)
 return None

def isValidSudoku(board):
  N = 9
  global message
  message = ""
   
  # Check if all elements of board[][]
  # stores value in the range[1, 9]
  for i in range(0, N):
    for j in range(0, N):
       
      # Check if board[i][j]
      # lies in the range
      if ((board[i][j] <= 0) or
          (board[i][j] > 9)):
        if board[i][j] == 0:
          message = "Empty Cells"
          return False
        else:
          message = "Values out of 1-9 interval"
          return False
 
  # Stores unique value
  # from 1 to N
  unique = [False] * (N + 1)
 
  # Traverse each row of
  # the given array
  for i in range(0, N):
     
    # Initialize unique[]
    # array to false
    for m in range(0, N + 1):
      unique[m] = False
 
    # Traverse each column
    # of current row
    for j in range(0, N):
       
      # Stores the value
      # of board[i][j]
      Z = board[i][j]
 
      # Check if current row
      # stores duplicate value
      if (unique[Z] == True):
        message = "Duplicates on row "+str(i)
        return False
       
      unique[Z] = True
 
  # Traverse each column of
  # the given array
  for i in range(0, N):
     
    # Initialize unique[]
    # array to false
    for m in range(0, N + 1):
      unique[m] = False
 
    # Traverse each row
    # of current column
    for j in range(0, N):
       
      # Stores the value
      # of board[j][i]
      Z = board[j][i]
 
      # Check if current column
      # stores duplicate value
      if (unique[Z] == True):
        message = "Duplicates on column "+str(j)
        return False
       
      unique[Z] = True
 
  # Traverse each block of
  # size 3 * 3 in board[][] array
  for i in range(0, N - 2, 3):
     
    # j stores first column of
    # each 3 * 3 block
    for j in range(0, N - 2, 3):
       
      # Initialize unique[]
      # array to false
      for m in range(0, N + 1):
        unique[m] = False
 
      # Traverse current block
      for k in range(0, 3):
        for l in range(0, 3):
           
          # Stores row number
          # of current block
          X = i + k
 
          # Stores column number
          # of current block
          Y = j + l
 
          # Stores the value
          # of board[X][Y]
          Z = board[X][Y]
 
          # Check if current block
          # stores duplicate value
          if (unique[Z] == True):
            message = "Duplicates in block"
            return False
           
          unique[Z] = True
           
  # If all conditions satisfied
  message = "You've solved Sudoku, congratulations!"
  return True

def check_sudoku():
 print(grid)
 print(isValidSudoku(grid))
 print(message)
 if isValidSudoku(grid) == True :
  messagebox.showinfo("Valid Sudoku", message)
 else:
  messagebox.showinfo("Invalid Sudoku", message)

 
def add_butoane(game_grid):
 butoane = Frame(game_grid, bg='white')
 butoane.pack()
 button_clear = Button(butoane, text ="Clear",  width = 50, font = 'summer, 20',command=clear, bd = 5)
 button_clear.pack()
 button_check = Button(butoane, text ="Check",  width = 50, font = 'summer, 20',command=check_sudoku, bd = 5)
 button_check.pack()

def callback(input):
 regex = '[1-9]'
 if re.search(regex,input):
    print(input)
    grid[row][col]=int(input)
    return True
 else:
    print(input)
    messagebox.showinfo("Incorrect Input", "Enter numbers ONLY!")
    return False


def desenat_sudoku(game_grid):
 global puzzle
 puzzle = Frame(game_grid, bg='white')
 puzzle.pack()
 global board
 board  = []
 for i in range(1,10):
           board += [[0,0,0,0,0,0,0,0,0]]
 global row,col
 for row in range(9):
  for col in range(9):
   if (row < 3 or row > 5) and (col < 3 or col > 5):
       color = 'white' 
   elif (row >= 3 and row < 6) and (col >=3 and col < 6):
      color = 'white'
   else:
      color = 'grey'
   if grid[row][col] == 0:
    board[row][col] = Entry(puzzle, width = 2, font = ('Arial', 20), bg = color, cursor = 'arrow', borderwidth = 2,
                      highlightcolor = 'yellow', highlightthickness = 0, highlightbackground = 'black') 
    reg = puzzle.register(callback)
    board[row][col].config(validate ='key', validatecommand =(reg, '%S'))
   else:
    board[row][col] = Label(puzzle, width = 2, font = ('Arial', 20), bg = color, cursor = 'arrow', borderwidth = 2,
                      highlightcolor = 'yellow', highlightthickness = 0, highlightbackground = 'black',text=copy_grid[row][col]) 
   board[row][col].grid(row = row, column = col)

def functie_timer(game_grid):
 global temp
 if temp >-1:
  mins,secs = divmod(temp,60)
  minute.set("{0:2d}".format(mins))
  second.set("{0:2d}".format(secs))
  game_grid.update()
  time.sleep(1)
  if (temp == 0):
    messagebox.showinfo("Sudoku Time Countdown", "Time's up, you've lost!")
  temp -= 1

def start_game(game_grid):
 generare_sudoku_rezolvabil()
 global copy_grid
 copy_grid = grid
 game_grid.destroy()
 game_grid = Tk()
 game_grid.title("Sudoku")
 game_grid.geometry("500x500")
 global minute,second
 minute=StringVar()
 second=StringVar()
 setare_valori_timer(minute,second)
 add_label_timer(game_grid)
 desenat_sudoku(game_grid)
 add_butoane(game_grid)
 game_grid.mainloop()

def setare_variabila_dificultate(x):
 global dificultate
 dificultate = x

def get_variabila_dificultate():
 return dificultate

def add_label():
   global label
   label=Label(window, text="Default Difficulty: Easy", font=('Aerial 18'))
   setare_variabila_dificultate(1)
   label.pack()

def update_label1():
   global label
   label["text"]="Difficulty Chosen: Easy"
   setare_variabila_dificultate(1)

def update_label2():
   global label
   label["text"]="Difficulty Chosen: Medium"
   setare_variabila_dificultate(2)

def update_label3():
   global label
   label["text"]="Difficulty Chosen: Hard"
   setare_variabila_dificultate(3)

def start_menu():
 global window
 window = Tk()
 window.title("Sudoku")
 game = partial(start_game, window)
 window.geometry("500x500")
 label1 = Label(window, text="Sudoku", font="arial, 50",width=10, height=2, borderwidth=3, relief="flat")
 button_start = Button(window, text ="Start", command = game, width = 500, font = 'summer, 25', bd = 10)
 label2= Label(window, text = "Select the difficulty below :  ", font = ("Times New Roman", 30), padx = 10, pady = 10)
 R1 = Radiobutton(window, text="Easy",background="white", activebackground="red",indicatoron = 0,font=30,command=update_label1)
 R2 = Radiobutton(window, text="Medium",background="white", activebackground="red",indicatoron = 0,font=30,command=update_label2)
 R3 = Radiobutton(window, text="Hard",background="white", activebackground="red",indicatoron = 0,font=30,command=update_label3)
 label1.pack()
 button_start.pack()
 label2.pack()
 R1.pack()
 R2.pack()
 R3.pack()
 add_label()
 window.mainloop()

def sudoku_game():
 start_menu()

def main():
 sudoku_game()

if __name__ == '__main__':
    main()