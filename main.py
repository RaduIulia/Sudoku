from tkinter import *
from random import randint, shuffle
import time
from tkinter import messagebox

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
  
def distruge(x):
 x.destroy()

def start_game():
 generare_sudoku_rezolvabil()
 game_grid = Tk()
 game_grid.title("Sudoku")
 game_grid.geometry("500x500")
 puzzle = Frame(game_grid, bg='white')
 puzzle.pack()
 hour=StringVar()
 minute=StringVar()
 second=StringVar()
 hour.set("00")
 minute.set("00")
 second.set("00")
 hourEntry= Entry(game_grid, width=3, font=("Arial",18,""),textvariable=hour)
 minuteEntry= Entry(game_grid, width=3, font=("Arial",18,""),textvariable=minute)
 secondEntry= Entry(game_grid, width=3, font=("Arial",18,""),textvariable=second)
 label1p = Label(game_grid, text="Sudoku Time Remaining:", font="arial, 25", borderwidth=3, relief="flat")
 blocks = [] 
 for r in range(3):
    row = []
    for c in range(3): 
        frame = Frame(puzzle, bd=1, highlightbackground='light blue', highlightcolor='light blue', highlightthickness=1)
        frame.grid(row=r, column=c, sticky='nsew')
        row.append(frame)
    blocks.append(row)
 btn_cells = [[None for x in range(9)] for x in range(9)]
 for i in range(9):
    for j in range(9):
        frm_cell = Frame(blocks[i // 3][j // 3])
        frm_cell.grid(row=(i % 3), column=(j % 3), sticky='nsew')
        frm_cell.rowconfigure(0, minsize=50, weight=1)
        frm_cell.columnconfigure(0, minsize=50, weight=1)
        var = StringVar()
        btn_cells[i][j] = Button(frm_cell, relief='ridge', bg='white', textvariable=var)
        btn_cells[i][j].grid(sticky='nsew')
        var.set(grid[i][j])
 label1p.pack()
 hourEntry.pack()
 minuteEntry.pack()
 secondEntry.pack()
 temp = 0*3600 + 0*60 + 5
 while temp >-1:
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        game_grid.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Sudoku Time Countdown", "Time's up, you've lost ")
            distruge(game_grid)
            start()
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1

def start():
 window = Tk()
 window.title("Sudoku")
 window.geometry("500x500")
 label1 = Label(window, text="Sudoku", font="arial, 50",width=10, height=2, borderwidth=3, relief="flat")
 button_start = Button(window, text ="Start", command = lambda: [distruge(window),start_game()], width = 500, font = 'summer, 25', bd = 10)
 label2= Label(window, text = "Select the difficulty below :  ", font = ("Times New Roman", 30), padx = 10, pady = 10)
 list = Listbox(window, selectmode = "single")
 x =["Easy", "Medium", "Hard"]
 for each_item in range(len(x)):
    list.insert(END, x[each_item])
    list.itemconfig(each_item)
 label1.pack()
 button_start.pack()
 label2.pack()
 list.pack(padx = 10, pady = 10, fill = "both")
 window.mainloop()

def sudoku():
 start()

def main():
 sudoku()

if __name__ == '__main__':
    main()