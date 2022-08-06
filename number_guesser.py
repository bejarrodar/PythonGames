import random
import tkinter
from tkinter import StringVar, ttk

from Games import loop


def number_game(frame:tkinter.Frame):

    for child in frame.winfo_children():
        child.destroy()

    W = tkinter.W
    E = tkinter.E
    attempt = 0
    
    answer = random.sample(range(10), 6)
    str_ans = ""
    for x in answer:
        str_ans += str(x)
    print(answer)

    def check_ans():
        nonlocal attempt
        guess = str(entry_val.get())
        temp_key = ""
        for x in range(6):
            if str_ans.count(guess[x]) == 0:
                print(f"{guess[x]} not in string")
                temp_key += "W"
                continue
            elif str_ans[x] == guess[x]:
                print(f"{guess[x]} in correct spot in string")
                temp_key += "C"
                continue
            print(f"{guess[x]} wrong spot in string")
            temp_key += "P"

        for y in range(6):
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
            for child in frame.winfo_children():
                child.destroy()
            loop(frame)


    grid = {str(x)+str(y):ttk.Label(frame) for x in range(5) for y in range(6)}
    answer_grid = {str(x)+str(y):StringVar() for x in range(5) for y in range(6)}

    for label in grid:
        grid[label].config(textvariable=answer_grid[label])
        grid[label].grid(column=label[1],row=label[0],padx=5,pady=5,ipadx=20)
        grid[label].config(padding=6,background="gray",font="helvetica 24",foreground="black")

    entry_val = StringVar()
    entry = ttk.Entry(frame)
    entry.config(textvariable=entry_val)
    entry.grid(column=0,columnspan=6,row=8,sticky=(E,W))


    submit = ttk.Button(frame, text="Submit", command=check_ans)
    submit.grid(column=0,columnspan=6,row=9,sticky=(E,W))
    
    



if __name__ == "__main__":
    root = tkinter.Tk()
    number_game(root)
    root.mainloop()
