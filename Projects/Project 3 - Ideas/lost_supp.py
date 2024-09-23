import tkinter as tk
import pygame as py

def game_lost():
      window = tk.Tk()
      window.title('YOU LOST')
      
      yes = tk.Button(window, text = 'YES', command = lambda:(window.destroy()))
      no = tk.Button(window, text = 'NO', command = lambda:(py.quit(), window.destroy()))

      yes.place(x = 20,y = 50)
      no.place(x = 130, y = 50)

      window.geometry("200x200+10+10")
      window.mainloop()
