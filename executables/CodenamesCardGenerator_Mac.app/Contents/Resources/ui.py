import tkinter as tk
import v1


def clicked():
    #do stuff on click
   # print("pressed")
    drawGrid()

def drawGrid():
    grid, redFirst = v1.main()


    first = ""
    if redFirst:
        first += "Red"
    else:
        first += "Blue"

    first += " goes first!"

    lbl = tk.Label(window, text=first, font=("Arial Bold", 18))
    lbl.grid(row=0, column=0, columnspan = 20, pady=10)

    ########################  ONE  #########################

    lbl00 = tk.Label(window, width=10, height=4, bg=grid[0][0])
    lbl00.grid( pady=2, padx=2, column=1, row=1)

    lbl01 = tk.Label(window, width=10, height=4, bg=grid[0][1])
    lbl01.grid( pady=2, padx=2, column=1, row=2)

    lbl02 = tk.Label(window, width=10, height=4, bg=grid[0][2])
    lbl02.grid( pady=2, padx=2, column=1, row=3)

    lbl03 = tk.Label(window, width=10, height=4, bg=grid[0][3])
    lbl03.grid( pady=2, padx=2, column=1, row=4)

    lbl04 = tk.Label(window, width=10, height=4, bg=grid[0][4])
    lbl04.grid( pady=2, padx=2, column=1, row=5)

    ########################  TWO  #########################


    lbl10 = tk.Label(window, width=10, height=4, bg=grid[1][0])
    lbl10.grid( pady=2, padx=2, column=2, row=1)

    lbl11 = tk.Label(window, width=10, height=4, bg=grid[1][1])
    lbl11.grid( pady=2, padx=2, column=2, row=2)

    lbl12 = tk.Label(window, width=10, height=4, bg=grid[1][2])
    lbl12.grid( pady=2, padx=2, column=2, row=3)

    lbl13 = tk.Label(window, width=10, height=4, bg=grid[1][3])
    lbl13.grid( pady=2, padx=2, column=2, row=4)

    lbl14 = tk.Label(window, width=10, height=4, bg=grid[1][4])
    lbl14.grid( pady=2, padx=2, column=2, row=5)

    ########################  THREE  #########################


    lbl20 = tk.Label(window, width=10, height=4, bg=grid[2][0])
    lbl20.grid( pady=2, padx=2, column=3, row=1)

    lbl21 = tk.Label(window, width=10, height=4, bg=grid[2][1])
    lbl21.grid( pady=2, padx=2, column=3, row=2)

    lbl22 = tk.Label(window, width=10, height=4, bg=grid[2][2])
    lbl22.grid( pady=2, padx=2, column=3, row=3)

    lbl23 = tk.Label(window, width=10, height=4, bg=grid[2][3])
    lbl23.grid( pady=2, padx=2, column=3, row=4)

    lbl24 = tk.Label(window, width=10, height=4, bg=grid[2][4])
    lbl24.grid( pady=2, padx=2, column=3, row=5)

    ########################  FOUR  #########################


    lbl30 = tk.Label(window, width=10, height=4, bg=grid[3][0])
    lbl30.grid( pady=2, padx=2, column=4, row=1)

    lbl31 = tk.Label(window, width=10, height=4, bg=grid[3][1])
    lbl31.grid( pady=2, padx=2, column=4, row=2)

    lbl32 = tk.Label(window, width=10, height=4, bg=grid[3][2])
    lbl32.grid( pady=2, padx=2, column=4, row=3)

    lbl33 = tk.Label(window, width=10, height=4, bg=grid[3][3])
    lbl33.grid( pady=2, padx=2, column=4, row=4)

    lbl34 = tk.Label(window, width=10, height=4, bg=grid[3][4])
    lbl34.grid( pady=2, padx=2, column=4, row=5)


    ########################  FIVE  #########################


    lbl40 = tk.Label(window, width=10, height=4, bg=grid[4][0])
    lbl40.grid( pady=2, padx=2, column=5, row=1)

    lbl41 = tk.Label(window, width=10, height=4, bg=grid[4][1])
    lbl41.grid( pady=2, padx=2, column=5, row=2)

    lbl42 = tk.Label(window, width=10, height=4, bg=grid[4][2])
    lbl42.grid( pady=2, padx=2, column=5, row=3)

    lbl43 = tk.Label(window, width=10, height=4, bg=grid[4][3])
    lbl43.grid( pady=2, padx=2, column=5, row=4)

    lbl44 = tk.Label(window, width=10, height=4, bg=grid[4][4])
    lbl44.grid( pady=2, padx=2, column=5, row=5)




window = tk.Tk()
window.title("Codemaster Card Randomizer")
window.geometry('500x500')
drawGrid()

btn = tk.Button(window, text="New Card!", command = clicked,)
btn.grid(column=2, row=10, columnspan=3, pady=20,)
window.mainloop()




