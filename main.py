from tkinter import *

def check_grid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False
  return True 

def generare_sudoku_rezolvabil():
 lista_numere=[1,2,3,4,5,6,7,8,9]
 grid = []
 grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
 grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
 grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
 grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
 grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
 grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
 grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
 grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
 grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

def start_game():
 generare_sudoku_rezolvabil()
 pass

def start():
 window = Tk()
 window.title("Sudoku")
 window.geometry("500x500")
 label1 = Label(window, text="Sudoku", font="arial, 50",width=10, height=2, borderwidth=3, relief="flat")
 button_start = Button(window, text ="Start", command = start_game, width = 500, font = 'summer, 25', bd = 10)
 label1.pack()
 button_start.place(relx=0.5, rely=0.5, anchor=CENTER)
 window.mainloop()

def sudoku():
 start()

def main():
 sudoku()

if __name__ == '__main__':
    main()