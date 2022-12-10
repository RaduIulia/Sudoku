from tkinter import *
from random import randint, shuffle
from tkinter import messagebox
import re 

def check_grid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False
  return True 

def solve_grid(grid):
  global counter
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      for value in range (1,10):
        if not(value in grid[row]):
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
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
        if not(value in grid[row]):
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
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
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if check_grid(grid):
                return True
              else:
                if fill_grid(grid):
                  return True
      break
  grid[row][col]=0      

def set_copy_grid(g):
 global copy_grid
 copy_grid = g

def get_copy_grid():
  return copy_grid

def generare_sudoku_rezolvabil():
 global lista_numere, counter,grid,attempts
 lista_numere=[1,2,3,4,5,6,7,8,9]
 grid = []
 for i in range(9):
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
 fill_grid(grid)
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
 set_copy_grid(grid)

def set_temp(minute,second):
  global temp
  temp = int(minute.get())*60 + int(second.get())

def get_temp():
  global temp
  return temp
  
def setare_valori_timer(minute,second):
 if get_variabila_dificultate() == 1:
  minute.set("20")
  second.set("00")
 if get_variabila_dificultate() == 2:
  minute.set("10")
  second.set("00")
 if get_variabila_dificultate() == 3:
  minute.set("00")
  second.set("15")
 set_temp(minute,second)

def clear():
 global grid
 grid = get_copy_grid()
 for row in range(9):
  for col in range(9):
    if grid[row][col] == 0:
     board[row][col].delete(0, END)
     cell = cells[(row, col)]
     cell.delete(0, END)

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
        return False
      unique[Z] = True
  for i in range(0, N):
    for m in range(0, N + 1):
      unique[m] = False
    for j in range(0, N):
      Z = board[j][i]
      if (unique[Z] == True):
        message = "Duplicates on column "+str(j)
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
            return False
          unique[Z] = True
  message = "You've solved Sudoku, congratulations!"
  return True

def check_sudoku():
 global grid
 for row in range(9):
  for col in range(9):
    if grid[row][col] == 0:
     val = cells[(row, col)].get()
     if val == "":
      grid[row][col] = 0
     else:
      grid[row][col] = (int(val))
 if isValidSudoku(grid) == True :
  messagebox.askyesno("Valid Sudoku", message )
  sudoku_game()
 else:
  messagebox.showwarning("Warning Invalid Sudoku", message) 
  grid = get_copy_grid() 
  
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
  return True
 else:
    messagebox.showerror("Incorrect Input", "Enter numbers ONLY!")
    return False

def desenat_sudoku(game_grid):
 global puzzle
 puzzle = Frame(game_grid, bg='white')
 puzzle.pack()
 global board
 board  = []
 for i in range(1,10):
  board += [[0,0,0,0,0,0,0,0,0]]
 global cells
 cells = {}
 global row,col
 for row in range(9):
  for col in range(9):
   if (row < 3 or row > 5) and (col < 3 or col > 5):
       color = 'white' 
   elif (row >= 3 and row < 6) and (col >=3 and col < 6):
      color = 'white'
   else:
      color = 'red'
   if grid[row][col] == 0:
    board[row][col] = Entry(puzzle, width = 2, font = ('Arial', 20), bg = color, cursor = 'arrow', borderwidth = 2,
                      highlightcolor = 'yellow',highlightthickness = 1, highlightbackground = 'black') 
    reg = puzzle.register(callback)
    board[row][col].config(validate ='key', validatecommand =(reg, '%S'))
    cells[(row, col)] = board[row][col]
   else:
    board[row][col] = Label(puzzle, width = 2, font = ('Arial', 20), bg = color, cursor = 'arrow', borderwidth = 2,
                      highlightcolor = 'yellow', highlightthickness = 1, highlightbackground = 'black',text=str(grid[row][col])) 
   board[row][col].grid(row = row, column = col)

def start_countdown():
 global temp
 if temp >= 0:
  time_left.config(text = "Game Ends in : " + str(temp) + "s")
  temp -= 1
  time_left.after(1000,start_countdown)
  if (temp == -1):
   messagebox.showerror("Time's up", "You didn't finish the Sudoku in time!")
   time_left.config(text="Game Over!!!")
   game_grid.destroy()
   start_menu()

def start_game():
  window.destroy()
  generare_sudoku_rezolvabil()
  global game_grid
  game_grid = Tk()
  game_grid.title("Sudoku")
  game_grid.geometry("550x550")
  label_game=Label(game_grid, text="Sudoku Game", font=('Aerial 18'))
  label_game.pack()
  minute=StringVar()
  second=StringVar()
  setare_valori_timer(minute,second)
  desenat_sudoku(game_grid)
  add_butoane(game_grid)
  global time_left
  time_left = Label(game_grid, text = "Game Ends in : -", font=('Aerial 18'), fg = "red")
  time_left.pack()
  if temp == get_temp():
   start_countdown()

def setare_variabila_dificultate(x):
 global dificultate
 dificultate = x

def get_variabila_dificultate():
 return dificultate

def add_label():
   global label,attempts
   label=Label(window, text="Default Difficulty: Easy", font=('Aerial 18'))
   setare_variabila_dificultate(1)
   label.pack()
   attempts = 3

def update_label1():
   global label,attempts
   label["text"]="Difficulty Chosen: Easy"
   setare_variabila_dificultate(1)
   attempts = 3

def update_label2():
   global label,attempts
   label["text"]="Difficulty Chosen: Medium"
   setare_variabila_dificultate(2)
   attempts = 4

def update_label3():
   global label,attempts
   label["text"]="Difficulty Chosen: Hard"
   setare_variabila_dificultate(3)
   attempts = 5

def start_menu():
 global window
 window = Tk()
 window.title("Sudoku")
 window.geometry("550x550")
 label1 = Label(window, text="Sudoku", font="arial, 65",width=10, height=2, borderwidth=3, relief="flat")
 button_start = Button(window, text ="Start", command =start_game, width = 500, font = 'summer, 40', bd = 10)
 label2= Label(window, text = "Select the difficulty below :  ", font = ("Times New Roman", 35), padx = 10, pady = 10)
 R1 = Radiobutton(window, text="Easy",background="white", activebackground="red",indicatoron = 0,font=40,command=update_label1)
 R2 = Radiobutton(window, text="Medium",background="white", activebackground="red",indicatoron = 0,font=40,command=update_label2)
 R3 = Radiobutton(window, text="Hard",background="white", activebackground="red",indicatoron = 0,font=40,command=update_label3)
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