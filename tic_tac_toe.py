import tkinter
from tkinter import StringVar, ttk

import save_manager
from Games import loop


def ttt_game(frame:tkinter.Frame):

    for child in frame.winfo_children():
        child.destroy()

    board = {str(x)+str(y):ttk.Button(frame) for x in range(3) for y in range(3)}
    values = {str(x)+str(y):StringVar() for x in range(3) for y in range(3)}

    player = True
    save = save_manager.read_results()
    p_1_wins = int(save[3])
    p_2_wins = int(save[4])
    ties = int(save[5])
    
    wins = [["00","01","02"],["10","11","12"],["20","21","22"],
            ["01","11","21"],["00","10","20"],["02","12","22"],
            ["00","11","22"],["20","11","02"]]
    
    def leave():
        for child in frame.winfo_children():
            child.destroy()
        loop(frame)
        
    def board_reset():
        nonlocal player
        for z in ["00","01","02","10","11","12","20","21","22"]:
            values[z].set("")
        player = True
    
    def check_wins():
        nonlocal p_1_wins
        nonlocal p_2_wins
        nonlocal ties
        for x in wins:
            play1_iter = 0
            play2_iter = 0
            for y in x:
                if values[y].get() == "x":
                    play1_iter += 1
                elif values[y].get() == "o":
                    play2_iter += 1
                else:
                    break
            if play1_iter == 3:
                print("player 1 wins")
                p_1_wins += 1
                board_reset()
            elif play2_iter == 3:
                print("player 2 wins")
                p_2_wins += 1
                board_reset()
        remain = 9
        for z in ["00","01","02","10","11","12","20","21","22"]:
            if values[z].get() == "x" or values[z].get() == "o":
                remain -= 1
        if remain == 0:
            ties += 1
            board_reset()
            

    def click(pos:str):
        nonlocal player
        if values[pos].get() != "x" and values[pos].get() != "o":
            if player is True:
                values[pos].set("x")
            else:
                values[pos].set("o")
            player = not player
            check_wins()
            save_manager.write_results({"win":p_1_wins,"lose":p_2_wins,"tie":ties},"ttt")

    for button in board:
        board[button].grid(ipadx=10,ipady=10,column=button[0],row=button[1])

    board["00"].config(textvariable=values["00"], command= lambda : click("00"))
    board["10"].config(textvariable=values["10"], command= lambda : click("10"))
    board["20"].config(textvariable=values["20"], command= lambda : click("20"))
    board["01"].config(textvariable=values["01"], command= lambda : click("01"))
    board["11"].config(textvariable=values["11"], command= lambda : click("11"))
    board["21"].config(textvariable=values["21"], command= lambda : click("21"))
    board["02"].config(textvariable=values["02"], command= lambda : click("02"))
    board["12"].config(textvariable=values["12"], command= lambda : click("12"))
    board["22"].config(textvariable=values["22"], command= lambda : click("22"))

if __name__ == "__main__":
    root = tkinter.Tk()
    ttt_game(root)
    root.mainloop()
