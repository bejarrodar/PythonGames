"""Main loop for the program this is what controls the whole thing"""
import tkinter
from tkinter import ttk

from connect_four import connect_main
from number_guesser import number_game
from rock_paper_scissors import rps_launch
from tic_tac_toe import ttt_game


def main(root) -> None: # pylint: disable=W0621
    """Main screen of the program shows buttons to select game"""


    N = tkinter.N
    W = tkinter.W
    E = tkinter.E
    S = tkinter.S

    style = ttk.Style()
    try:
        style.theme_use("vista")
    except tkinter.TclError:
        print("Unable to find theme")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    tic_tac_toe_button = ttk.Button(mainframe, text="Tic Tac Toe", command=lambda : ttt_game(mainframe))
    tic_tac_toe_button.grid(column=0,row=0)

    connect_4_button = ttk.Button(mainframe, text="Connect 4", command=lambda : connect_main(mainframe))
    connect_4_button.grid(column=1,row=0)

    rps_button = ttk.Button(mainframe, text="Rock Paper Scissors", command=lambda : rps_launch(mainframe))
    rps_button.grid(column=0,row=1)

    number_guess_button = ttk.Button(mainframe, text="Number Guesser", command=lambda : number_game(mainframe))
    number_guess_button.grid(column=1,row=1)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)


if __name__ == "__main__":

    root = tkinter.Tk()
    main(root)
    root.mainloop()
