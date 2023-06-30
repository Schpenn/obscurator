from tkinter import *

root = Tk()
root.geometry("300x450")
root.title(" Obscurator ")

def Obscure_text():
    input = inputtxt.get("1.0", "end-1c")
    print(input)
    input_list = list(input)

    while len(input_list) % 4 != 0:
        input_list.append(' ')

    rows = int((len(input_list)) / 4)

    input_grid = [[0] * 4 for i in range(rows)]
    o = 0
    for i in range(0, rows, 1):
        for j in range(0, 4, 1):
            input_grid[i][j] = ord(input_list[o]) + 3
            o += 1

    output_str = ""
    for i in range(0, 4, 1):
        for j in range(0, rows, 1):
            output_str += chr(input_grid[j][i])

    Output.insert(END, output_str)

def Unobscure_text():
    input = inputtxt.get("1.0", "end-1c")
    print(input)
    input_list = list(input)

    rows = int((len(input_list)) / 4)

    input_grid = [[0] * 4 for i in range(rows)]
    o = 0
    for i in range(0, 4, 1):
        for j in range(0, rows, 1):
            input_grid[j][i] = ord(input_list[o]) - 3
            o += 1
        
    output_str = ""
    for i in range(0, rows, 1):
        for j in range(0, 4, 1):
            output_str += chr(input_grid[i][j])

    Output.insert(END, output_str.rstrip())

def Clear_input():
    inputtxt.delete("1.0", "end-1c")
    
def Clear_output():
    Output.delete("1.0", "end-1c")

def Clear_all():
    Clear_input()
    Clear_output()

l_top = Label(text="Unobscured text:")
l_bottom = Label(text="Obscured text:")
inputtxt = Text(root, height=10, width=30, bg="light yellow")
Output = Text(root, height=10, width=30, bg="light cyan")
buttons = Frame(root)
Btn1 = Button(buttons, height=2, width=10, text="Obscure", command=lambda: Obscure_text())
Btn2 = Button(buttons, height=2, width=10, text="Unobscure", command=lambda: Unobscure_text())
Btn3 = Button(buttons, height=2, width=10, text="Clear all", command=lambda: Clear_all())

l_top.pack()
inputtxt.pack()
buttons.pack(pady = 5)
Btn1.pack(side=LEFT)
Btn2.pack(side=LEFT)
Btn3.pack(side=LEFT)
l_bottom.pack()
Output.pack()

root.mainloop()
