import random
import tkinter as tk
from tkinter import ttk
import pyperclip
import os

global data

def MainWindow():
    window = tk.Tk()
    window.geometry('500x500')
    window.title("Shuffler")

    og_tracklist = tk.StringVar()

    header = tk.Label(window, 
                      anchor="center",
                      text="Copy and Paste in the Tracklist",
                      font=("bold", 20)
                      ).place(x=110, y=20)
    
    tk.Button(window, 
                text='Shuffle',
                bg='brown',
                fg='black',
                command=lambda : Shuffle()
                ).place(x=100,y=60)
    
    tk.Button(window, 
                text='Clear Text',
                bg='brown',
                fg='black',
                command=lambda : ClearText()
                ).place(x=300,y=60)
    
    tk.Button(window, 
                text='Copy List',
                bg='brown',
                fg='black',
                command=lambda : CopyList()
                ).place(x=330,y=430)  

    og_tracklist_entry = tk.Text(window)
    og_tracklist_entry.place(width=230,
                             x=10,y=100)
    
    new_tracklist_entry = tk.Text(window)
    new_tracklist_entry.place(width=230,
                             x=260,y=100)

    def Shuffle():
        og_tracklist = og_tracklist_entry.get("1.0","end-1c")
        tracklist = og_tracklist.split("\n")
        random.shuffle(tracklist)
        new_tracklist_entry.delete('1.0',tk.END)
        new_tracklist_string = ''
        for track in tracklist:
            if track == tracklist[-1]:
                new_tracklist_string+= track
            else:
                new_tracklist_string+= track + '\n'
        new_tracklist_entry.insert(tk.END, new_tracklist_string)

    def ClearText():
        og_tracklist_entry.delete('1.0',tk.END)
        new_tracklist_entry.delete('1.0',tk.END)

    def CopyList():
        new_tracklist_entry.tag_add(tk.SEL, "1.0", tk.END)
        global data
        data = new_tracklist_entry.get("1.0", tk.END)
        pyperclip.copy(data)

    window.mainloop()

MainWindow()