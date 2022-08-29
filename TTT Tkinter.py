from tkinter import *

main = Tk()

v = 0
game = [0, 0, 0, 0, 0, 0, 0, 0, 0]
winningBoard = []


def allButtons():
    Button(text="   ", padx=45, pady=45, font=25, command=lambda: XClicked(1, 0, 0)).grid(row=1, column=0)
    Button(text="   ", padx=45, pady=45, font=25, command=lambda: XClicked(1, 1, 1)).grid(row=1, column=1)
    Button(text="   ", padx=45, pady=45, font=25, command=lambda: XClicked(1, 2, 2)).grid(row=1, column=2)
    Button(text="   ", padx=45, pady=45, font=25, command=lambda: XClicked(2, 0, 3)).grid(row=2, column=0)
    Button(text="   ", padx=45, pady=45, font=25, command=lambda: XClicked(2, 1, 4)).grid(row=2, column=1)
    Button(text="   ", padx=45, pady=45, font=25, command=lambda: XClicked(2, 2, 5)).grid(row=2, column=2)
    Button(text="   ", padx=45, pady=45, font=25, command=lambda: XClicked(3, 0, 6)).grid(row=3, column=0)
    Button(text="   ", padx=45, pady=45, font=25, command=lambda: XClicked(3, 1, 7)).grid(row=3, column=1)
    Button(text="   ", padx=45, pady=45, font=25, command=lambda: XClicked(3, 2, 8)).grid(row=3, column=2)


def winner():
    global winningBoard
    main.destroy()
    root = Tk()
    root.title("Winner!")
    root.geometry("500x500")

    root.rowconfigure(1, weight=3)
    root.rowconfigure(2, weight=3)
    root.rowconfigure(3, weight=3)

    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=3)
    root.columnconfigure(2, weight=3)

    Label(text="Winner!", fg="Purple", padx=25, pady=25, font=25).grid(row=0, column=1)

    for x in range(len(winningBoard)):
        Button(text=f"{winningBoard[x][2]}", padx=45, pady=45, font=25).grid(row=winningBoard[x][0], column=winningBoard[x][1])
    root.mainloop()


def checkWinner():
    global game
    for x in range(1, 3):
        if x == 1:
            b = "X"
        else:
            b = "O"
        var1 = 0
        for l in range(3):
            if game[l] == b:
                var1 += 1
        if var1 == 3:
            winner()
        var2 = 0
        for k in range(3, 6):
            if game[k] == b:
                var2 += 1
        if var2 == 3:
            winner()
        var3 = 0
        for j in range(6, 9):
            if game[j] == b:
                var3 += 1
        if var3 == 3:
            winner()
        var4 = 0
        for j in range(0, 9, 3):
            if game[j] == b:
                var4 += 1
        if var4 == 3:
            winner()
        var5 = 0
        for j in range(1, 9, 3):
            if game[j] == b:
                var5 += 1
        if var5 == 3:
            winner()
        var6 = 0
        for j in range(2, 9, 3):
            if game[j] == b:
                var6 += 1
        if var6 == 3:
            winner()
        var7 = 0
        for j in range(0, 9, 4):
            if game[j] == b:
                var7 += 1
        if var7 == 3:
            winner()
        var8 = 0
        for j in range(2, 8, 2):
            if game[j] == b:
                var8 += 1
        if var8 == 3:
            winner()


def XClicked(x, y, z):
    global v, game, winningBoard
    if v % 2 == 0:
        Button(text=" X ", padx=45, pady=45, font=25).grid(row=x, column=y)
        game[z] = "X"
        checkWinner()
        v = v + 1
        winningBoard.append([x, y, "X"])
    else:
        Button(text=" O ", padx=45, pady=45, font=25).grid(row=x, column=y)
        v = 0
        game[z] = "O"
        winningBoard.append([x, y, "O"])
        checkWinner()


main.title("TicTacToe")
main.geometry("500x500")

main.rowconfigure(1, weight=3)
main.rowconfigure(2, weight=3)
main.rowconfigure(3, weight=3)

main.columnconfigure(0, weight=3)
main.columnconfigure(1, weight=3)
main.columnconfigure(2, weight=3)

Title = Label(text="Tic Tac Toe", fg="Purple", padx=25, pady=25, font=25).grid(row=0, column=1)

allButtons()

main.mainloop()

