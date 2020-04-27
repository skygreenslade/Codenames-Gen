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

    btn00 = tk.Button(window, width=3, height=2, bg=grid[0][0])
    btn00.grid(column=1, row=1)

    btn01 = tk.Button(window, width=3, height=2, bg=grid[0][1])
    btn01.grid(column=1, row=2)

    btn02 = tk.Button(window, width=3, height=2, bg=grid[0][2])
    btn02.grid(column=1, row=3)

    btn03 = tk.Button(window, width=3, height=2, bg=grid[0][3])
    btn03.grid(column=1, row=4)

    btn04 = tk.Button(window, width=3, height=2, bg=grid[0][4])
    btn04.grid(column=1, row=5)

    ########################  TWO  #########################


    btn10 = tk.Button(window, width=3, height=2, bg=grid[1][0])
    btn10.grid(column=2, row=1)

    btn11 = tk.Button(window, width=3, height=2, bg=grid[1][1])
    btn11.grid(column=2, row=2)

    btn12 = tk.Button(window, width=3, height=2, bg=grid[1][2])
    btn12.grid(column=2, row=3)

    btn13 = tk.Button(window, width=3, height=2, bg=grid[1][3])
    btn13.grid(column=2, row=4)

    btn14 = tk.Button(window, width=3, height=2, bg=grid[1][4])
    btn14.grid(column=2, row=5)

    ########################  THREE  #########################


    btn20 = tk.Button(window, width=3, height=2, bg=grid[2][0])
    btn20.grid(column=3, row=1)

    btn21 = tk.Button(window, width=3, height=2, bg=grid[2][1])
    btn21.grid(column=3, row=2)

    btn22 = tk.Button(window, width=3, height=2, bg=grid[2][2])
    btn22.grid(column=3, row=3)

    btn23 = tk.Button(window, width=3, height=2, bg=grid[2][3])
    btn23.grid(column=3, row=4)

    btn24 = tk.Button(window, width=3, height=2, bg=grid[2][4])
    btn24.grid(column=3, row=5)

    ########################  FOUR  #########################


    btn30 = tk.Button(window, width=3, height=2, bg=grid[3][0])
    btn30.grid(column=4, row=1)

    btn31 = tk.Button(window, width=3, height=2, bg=grid[3][1])
    btn31.grid(column=4, row=2)

    btn32 = tk.Button(window, width=3, height=2, bg=grid[3][2])
    btn32.grid(column=4, row=3)

    btn33 = tk.Button(window, width=3, height=2, bg=grid[3][3])
    btn33.grid(column=4, row=4)

    btn34 = tk.Button(window, width=3, height=2, bg=grid[3][4])
    btn34.grid(column=4, row=5)


    ########################  FIVE  #########################


    btn40 = tk.Button(window, width=3, height=2, bg=grid[4][0])
    btn40.grid(column=5, row=1)

    btn41 = tk.Button(window, width=3, height=2, bg=grid[4][1])
    btn41.grid(column=5, row=2)

    btn42 = tk.Button(window, width=3, height=2, bg=grid[4][2])
    btn42.grid(column=5, row=3)

    btn43 = tk.Button(window, width=3, height=2, bg=grid[4][3])
    btn43.grid(column=5, row=4)

    btn44 = tk.Button(window, width=3, height=2, bg=grid[4][4])
    btn44.grid(column=5, row=5)




window = tk.Tk()
window.title("Codemaster Card Randomizer")
window.geometry('450x450')
drawGrid()

btn = tk.Button(window, text="New Card!", command = clicked,)
btn.grid(column=2, row=10, columnspan=3, pady=20,)
window.mainloop()




