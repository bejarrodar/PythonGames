import tkinter
from tkinter import StringVar, ttk

import random_word
import save_manager

#from Games import loop


def wordle(frame:tkinter.Frame):

    for child in frame.winfo_children():
        child.destroy()

    W = tkinter.W
    E = tkinter.E
    attempt = 0
    save = save_manager.read_results()
    wins = int(save[6])
    lose = int(save[7])
    
    def leave():
        for child in frame.winfo_children():
            child.destroy()
        #loop(frame)
    
    def clear_board():
        nonlocal attempt
        nonlocal answer
        answer = random_word.pick_word()
        attempt = 0
        for x in range(5):
            for y in range(5):
                answer_grid[str(x)+str(y)].set("")
                grid[str(x)+str(y)].config(foreground="black")
                entry_val.set("")
                
    
    answer = random_word.pick_word()

    def check_ans(*args):
        nonlocal attempt
        nonlocal wins
        nonlocal lose
        guess = entry_val.get().upper()
        if random_word.check_word(guess):
            temp_key = ""
            for x in range(5):
                if answer.count(guess[x]) == 0:
                    print(f"{guess[x]} not in string")
                    temp_key += "W"
                    continue
                elif answer[x] == guess[x]:
                    print(f"{guess[x]} in correct spot in string")
                    temp_key += "C"
                    continue
                print(f"{guess[x]} wrong spot in string")
                temp_key += "P"

            for y in range(5):
                if temp_key[y] == "C":
                    grid[str(attempt)+str(y)].config(foreground="green")
                elif temp_key[y] == "P":
                    grid[str(attempt)+str(y)].config(foreground="yellow")
                else:
                    grid[str(attempt)+str(y)].config(foreground="red")
                answer_grid[str(attempt)+str(y)].set(guess[y])

            entry_val.set("")
            attempt += 1
            if temp_key == "CCCCCC":
                wins += 1
                clear_board()
            if attempt == 5:
                lose += 1
                clear_board()
            save_manager.write_results({"win":wins,"lose":lose,"tie":0}, "wdl")
        else:
            print(f"{guess} is not a valid 5 letter word")
            
    


    grid = {str(x)+str(y):ttk.Label(frame) for x in range(5) for y in range(5)}
    answer_grid = {str(x)+str(y):StringVar() for x in range(5) for y in range(5)}

    for label in grid:
        grid[label].config(textvariable=answer_grid[label])
        grid[label].grid(column=label[1],row=label[0],padx=5,pady=5,ipadx=20)
        grid[label].config(padding=6,background="gray",font="helvetica 24",foreground="black")

    entry_val = StringVar()
    entry = ttk.Entry(frame)
    entry.config(textvariable=entry_val)
    entry.grid(column=0,columnspan=5,row=8,sticky=(E,W))


    submit = ttk.Button(frame, text="Submit", command=check_ans)
    submit.grid(column=0,columnspan=5,row=9,sticky=(E,W))
    
    entry.bind("<Return>", check_ans)
    
    



if __name__ == "__main__":
    root = tkinter.Tk()
    wordle(root)
    root.mainloop()
