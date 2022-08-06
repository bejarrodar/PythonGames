import tkinter
from tkinter import ttk

import main


def loop(root) -> None: # pylint: disable=W0621
    """The start of the program automatically ran when this file is launched"""


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
    
    main.main(mainframe)
    

if __name__ == "__main__":

    root = tkinter.Tk()
    root.title("Games")
    loop(root)
    root.mainloop()
