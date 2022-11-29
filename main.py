import tkinter
from tkinter import *


def startgame():
   pass

def initializari_grafice():
 window = Tk()
 window.title("Sudoku")
 window.geometry("500x500")
 label1 = Label(window, text="Sudoku", font="arial, 50",width=10, height=2, borderwidth=3, relief="flat")
 button_start = Button(window, text ="Start", command = startgame, width = 500, font = 'summer, 25', bd = 10)
 label1.pack()
 button_start.place(relx=0.5, rely=0.5, anchor=CENTER)
 window.mainloop()

def sudoku():
 initializari_grafice()
 pass

def main():
 sudoku()

if __name__ == '__main__':
    main()