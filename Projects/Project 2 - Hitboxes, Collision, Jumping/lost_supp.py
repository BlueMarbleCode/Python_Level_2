import tkinter as tk
import pygame as py

def game_lost():
      window = tk.Tk()
      window.title('YOU LOST')

      t = tk.Text(window, height = 5, width = 30)
      words = tk.Label(window, text = 'PLAY AGAIN?')
      
      yes = tk.Button(window, text = 'YES', command = lambda:(window.destroy()))
      no = tk.Button(window, text = 'NO', command = lambda:(py.quit(), window.destroy()))

      words.place(x = 20, y = 20)
      yes.place(x = 20,y = 50)
      no.place(x = 65, y = 50)

      window.geometry("100x100+10+10")
      window.mainloop()
