import random
import tkinter
from tkinter import ttk

from Games import loop


def rps_launch(frame: ttk.Frame):
    """Clears the screen then displays Rock paper scissors"""

    def playRock():
        ties = int(tie_var.get())
        loses = int(lose_var.get())
        wins = int(win_var.get())
        results = ""
        x = random.randint(1, 3)  #  1 is rock 2 is paper 3 is scissors
        match x:
            case 1:
                results = "Tie"
                ties += 1
                tie_var.set(str(ties))
            case 2:
                results = "Lose"
                loses += 1
                lose_var.set(str(loses))
            case 3:
                results = "Win"
                wins += 1
                win_var.set(str(wins))

        ttk.Label(frame, text=results).grid(
            column=2, row=2, sticky=(E, W)
        )

    def playPaper():
        ties = int(tie_var.get())
        loses = int(lose_var.get())
        wins = int(win_var.get())
        results = ""
        x = random.randint(1, 3)
        match x:
            case 1:
                results = "Win"
                wins += 1
                win_var.set(str(wins))
            case 2:
                results = "Tie"
                ties += 1
                tie_var.set(str(ties))
            case 3:
                results = "Lose"
                loses += 1
                lose_var.set(str(loses))

        ttk.Label(frame, text=results).grid(
            column=2, row=2, sticky=(E, W)
        )

    def playScissors():
        ties = int(tie_var.get())
        loses = int(lose_var.get())
        wins = int(win_var.get())
        results = ""
        x = random.randint(1, 3)
        match x:
            case 1:
                results = "Lose"
                loses += 1
                lose_var.set(str(loses))
            case 2:
                results = "Win"
                wins += 1
                win_var.set(str(wins))
            case 3:
                results = "Tie"
                ties += 1
                tie_var.set(str(ties))

        ttk.Label(frame, text=results).grid(
            column=2, row=2, sticky=(E, W)
        )
        
    def leave():
        for child in frame.winfo_children():
            child.destroy()
        loop(frame)

    for child in frame.winfo_children():
        child.destroy()

    W = tkinter.W
    E = tkinter.E
    wins = 0
    loses = 0
    ties = 0
    tie_var = tkinter.StringVar()
    tie_var.set(str(ties))
    win_var = tkinter.StringVar()
    lose_var = tkinter.StringVar()
    win_var.set(str(wins))
    lose_var.set(str(loses))

    ttk.Button(frame, text="Rock", command=playRock).grid(
        column=1, row=1, sticky=(W)
    )
    ttk.Button(frame, text="Paper", command=playPaper).grid(
        column=2, row=1, sticky=(E, W)
    )
    ttk.Button(frame, text="Scissors", command=playScissors).grid(
        column=3, row=1, sticky=(E)
    )

    ttk.Label(frame, text="Wins:").grid(column=1, row=3, sticky=(W))
    winLabel = ttk.Label(frame, textvariable=win_var)
    winLabel.grid(column=2, row=3, sticky=(W))

    ttk.Label(frame, text="Loses:").grid(column=3, row=3, sticky=(W))
    loseLabel = ttk.Label(frame, textvariable=lose_var)
    loseLabel.grid(column=4, row=3, sticky=(W))

    ttk.Label(frame, text="Ties:").grid(column=5, row=3, sticky=(W))
    tieLabel = ttk.Label(frame, textvariable=tie_var)
    tieLabel.grid(column=6, row=3, sticky=(W))
    
    ttk.Button(frame, text="Back", command=leave).grid(column=5,row=1)

    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)
