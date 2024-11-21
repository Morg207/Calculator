from tkinter import *
from tkinter import ttk
import tkinter.font

def on_button(sign):
    global text, button_clicked
    text += str(sign)
    if not button_clicked and sign != 0:
        result_text_l = list(text)
        result_text_l = result_text_l[1:]
        text = "".join(result_text_l)
    button_clicked = True
    label.configure(text=text)

def on_equals_button():
    global text
    try:
        sum = str(eval(text))
        float_sum = float(sum)
        if float_sum.is_integer():
            float_sum = int(float_sum)
        sum = str(float_sum)
        label.configure(text=sum)
        text = sum
    except SyntaxError:
        label.configure(text="Error")
        text = ""
    except ZeroDivisionError:
        label.configure(text="Error")
        text = ""

def on_negate():
    global text
    try:
        if int(text) < 0:
            text = str(abs(int(text)))
        elif int(text) > 0:
            text_list = list(text)
            text_list.insert(0,"-")
            text = ''.join(text_list)
        label.configure(text=text)
    except ValueError:
        pass

def on_clear_button():
    global text, button_clicked
    text = "0"
    label.configure(text=text)
    button_clicked = False
    
def create_buttons():
    buttons = {"mod":ttk.Button(window_frame,width=5,text="%",command=lambda: on_button("%")),"CE":ttk.Button(window_frame,width=5,text="CE",command=on_clear_button),
           "C":ttk.Button(window_frame,width=5,text="C",command=on_clear_button),"divide":ttk.Button(window_frame,width=5,text="÷",command=lambda: on_button("/")),
           "7":ttk.Button(window_frame,width=5,text="7",command=lambda: on_button(7)),"8":ttk.Button(window_frame,width=5,text="8",command=lambda: on_button(8)),
           "9":ttk.Button(window_frame,width=5,text="9",command=lambda: on_button(9)),"multiply":ttk.Button(window_frame,width=5,text="x",command=lambda: on_button("*")),
           "4":ttk.Button(window_frame,width=5,text="4",command=lambda: on_button(4)),"5":ttk.Button(window_frame,text="5",width=5,command=lambda: on_button(5)),
           "6":ttk.Button(window_frame,width=5,text="6",command=lambda: on_button(6)),"subtract":ttk.Button(window_frame,width=5,text="-",command=lambda: on_button("-")),
           "1":ttk.Button(window_frame,width=5,text="1",command=lambda: on_button(1)),"2":ttk.Button(window_frame,text="2",width=5,command=lambda: on_button(2)),
           "3":ttk.Button(window_frame,width=5,text="3",command=lambda: on_button(3)),"plus":ttk.Button(window_frame,width=5,text="+",command=lambda: on_button("+")),
           "+/-":ttk.Button(window_frame,width=5,text="+/-",command=on_negate),"0":ttk.Button(window_frame,width=5,text="0",command=lambda: on_button(0)),
           ".":ttk.Button(window_frame,width=5,text=".",command=lambda: on_button(".")),"equals":ttk.Button(window_frame,width=5,text="=",command=on_equals_button)}
    return buttons

def setup_window():
    window.title("Calculator")
    icon_image = PhotoImage(file="icon.png")
    window.iconphoto(False,icon_image)
    window_frame = ttk.Frame(window,padding="12 0 12 20")
    window_frame.pack()
    return window_frame

def setup_buttons():
    buttons["mod"].grid(row=1,column=0)
    buttons["CE"].grid(row=1,column=1)
    buttons["C"].grid(row=1,column=2,sticky="w")
    buttons["divide"].grid(row=2,column=2,sticky="w")
    buttons["7"].grid(row=2,column=1)
    buttons["8"].grid(row=2,column=0)
    buttons["9"].grid(row=3,column=0)
    buttons["multiply"].grid(row=3,column=2,sticky="w")
    buttons["4"].grid(row=3,column=1)
    buttons["5"].grid(row=4,column=0)
    buttons["6"].grid(row=4,column=1)
    buttons["subtract"].grid(row=4,column=2,sticky="w")
    buttons["1"].grid(row=5,column=0)
    buttons["2"].grid(row=5,column=1)
    buttons["3"].grid(row=6,column=0)
    buttons["plus"].grid(row=5,column=2,sticky="w")
    buttons["+/-"].grid(row=6,column=1)
    buttons["0"].grid(row=6,column=2,sticky="w")
    buttons["."].grid(row=7,column=0)
    buttons["equals"].grid(row=7,column=1)

def create_labels():
    label = ttk.Label(window,text=text,width=20)
    label_font = tkinter.font.Font(font=tkinter.font.nametofont("TkDefaultFont"))
    label_font.configure(size=19)
    label["font"] = label_font
    label.configure(anchor="e",background=window.cget("bg"))
    label.pack(padx=(0,40))
    return label

if __name__ == "__main__":
    window = ThemedTk()
    button_clicked = False
    text = "0"
    label = create_labels()
    window_frame = setup_window()
    buttons = create_buttons()
    setup_buttons()
    style = ttk.Style()
    style.theme_use("radiance")
    style.configure("TFrame",background=window.cget("bg"))
    window.mainloop()
