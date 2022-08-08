import tkinter
from tkinter import PhotoImage, ttk

import save_manager
from Games import loop


def connect_main(frame: tkinter.Frame):
    """Runs the connect four game"""
    for child in frame.winfo_children():
        child.destroy()

    a_frame = ttk.Frame(frame)
    a_frame.grid(column=0,row=0)

    b_frame = ttk.Frame(frame)
    b_frame.grid(column=1,row=0)

    c_frame = ttk.Frame(frame)
    c_frame.grid(column=2,row=0)

    d_frame = ttk.Frame(frame)
    d_frame.grid(column=3,row=0)

    e_frame = ttk.Frame(frame)
    e_frame.grid(column=4,row=0)

    clear_img = PhotoImage(file="connect_1.gif")
    player_1_img = PhotoImage(file="connect_2.gif")
    player_2_img = PhotoImage(file="connect_3.gif")
    
    def leave():
        for child in frame.winfo_children():
            child.destroy()
        loop(frame)
    
    wins = [["a1","a2","a3","a4"],["b1","b2","b3","b4"],["c1","c2","c3","c4"],
            ["d1","d2","d3","d4"],["e1","e2","e3","e4"],["a1","b2","c3","d4"],
            ["b1","c2","d3","e4"],["a4","b3","c2","d1"],["b4","c3","d2","e1"],
            ["a4","b4","c4","d4"],["a3","b3","c3","d3"],["a2","b2","c2","d2"],
            ["a1","b1","c1","d1"],["e4","b4","c4","d4"],["e3","b3","c3","d3"],
            ["e2","b2","c2","d2"],["e1","b1","c1","d1"]]

    grid = {"a1":0, "b1":0, "c1":0, "d1":0, "e1":0,
            "a2":0, "b2":0, "c2":0, "d2":0, "e2":0,
            "a3":0, "b3":0, "c3":0, "d3":0, "e3":0,
            "a4":0, "b4":0, "c4":0, "d4":0, "e4":0,
            "current_player":1}
    
    save = save_manager.read_results()
    win = int(save[9])
    lose = int(save[10])
    tie = int(save[11])
    
    def clear_board():
        for x in grid2:
            grid2[x].config(image = clear_img)
            grid[x] = 0
            grid2[x].pack()
            grid["current_player"] = 1

    def check_win():
        nonlocal win
        nonlocal lose
        nonlocal tie
        for x in wins:
            play1_iter = 0
            play2_iter = 0
            for y in x:
                if grid[y] == 1:
                    play1_iter += 1
                elif grid[y] == 2:
                    play2_iter += 1
            if play1_iter == 4:
                print("player 1 wins")
                win += 1
                clear_board()
            elif play2_iter == 4:
                print("player 2 wins")
                lose += 1
                clear_board()
        count = 0
        for z in grid2:
            if grid[z] != 0:
                count += 1
        if count == 20:
            print("Tie")
            tie += 1
            clear_board()
        save_manager.write_results({"win":win,"lose":lose,"tie":tie},"connect")

    def make_move(column:str):
        for i in range(4,0,-1):
            grid_id = column + str(i)
            if grid[grid_id] == 0:
                if grid["current_player"] == 1:
                    grid[grid_id] = 1
                    grid2[grid_id].config(image = player_1_img)
                    grid2[grid_id].pack()
                    grid["current_player"] = 2
                    check_win()
                    break
                else:
                    grid[grid_id] = 2
                    grid2[grid_id].config(image = player_2_img)
                    grid2[grid_id].pack()
                    grid["current_player"] = 1
                    check_win()
                    break



    #==============Create images in each square================

    a1 = ttk.Label(a_frame, image=clear_img)
    a2 = ttk.Label(a_frame, image=clear_img)
    a3 = ttk.Label(a_frame, image=clear_img)
    a4 = ttk.Label(a_frame, image=clear_img)

    b1 = ttk.Label(b_frame, image=clear_img)
    b2 = ttk.Label(b_frame, image=clear_img)
    b3 = ttk.Label(b_frame, image=clear_img)
    b4 = ttk.Label(b_frame, image=clear_img)

    c1 = ttk.Label(c_frame, image=clear_img)
    c2 = ttk.Label(c_frame, image=clear_img)
    c3 = ttk.Label(c_frame, image=clear_img)
    c4 = ttk.Label(c_frame, image=clear_img)

    d1 = ttk.Label(d_frame, image=clear_img)
    d2 = ttk.Label(d_frame, image=clear_img)
    d3 = ttk.Label(d_frame, image=clear_img)
    d4 = ttk.Label(d_frame, image=clear_img)

    e1 = ttk.Label(e_frame, image=clear_img)
    e2 = ttk.Label(e_frame, image=clear_img)
    e3 = ttk.Label(e_frame, image=clear_img)
    e4 = ttk.Label(e_frame, image=clear_img)


    a1.image = clear_img
    a2.image = clear_img
    a3.image = clear_img
    a4.image = clear_img

    b1.image = clear_img
    b2.image = clear_img
    b3.image = clear_img
    b4.image = clear_img

    c1.image = clear_img
    c2.image = clear_img
    c3.image = clear_img
    c4.image = clear_img

    d1.image = clear_img
    d2.image = clear_img
    d3.image = clear_img
    d4.image = clear_img

    e1.image = clear_img
    e2.image = clear_img
    e3.image = clear_img
    e4.image = clear_img


    a1.pack()
    a2.pack()
    a3.pack()
    a4.pack()

    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()

    c1.pack()
    c2.pack()
    c3.pack()
    c4.pack()

    d1.pack()
    d2.pack()
    d3.pack()
    d4.pack()

    e1.pack()
    e2.pack()
    e3.pack()
    e4.pack()


    a_button = ttk.Button(frame, text="Drop here", command=lambda : make_move("a"))
    b_button = ttk.Button(frame, text="Drop here", command=lambda : make_move("b"))
    c_button = ttk.Button(frame, text="Drop here", command=lambda : make_move("c"))
    d_button = ttk.Button(frame, text="Drop here", command=lambda : make_move("d"))
    e_button = ttk.Button(frame, text="Drop here", command=lambda : make_move("e"))

    a_button.grid(column=0,row=4)
    b_button.grid(column=1,row=4)
    c_button.grid(column=2,row=4)
    d_button.grid(column=3,row=4)
    e_button.grid(column=4,row=4)
    
    grid2 = {"a1":a1, "b1":b1, "c1":c1, "d1":d1, "e1":e1,
            "a2":a2, "b2":b2, "c2":c2, "d2":d2, "e2":e2,
            "a3":a3, "b3":b3, "c3":c3, "d3":d3, "e3":e3,
            "a4":a4, "b4":b4, "c4":c4, "d4":d4, "e4":e4,}
