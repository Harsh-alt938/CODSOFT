from tkinter import *
from tkinter import messagebox
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

cal = Tk()                      # Creating basic window
cal.geometry("312x394")         # Size of the window width:- 312, height:- 394
cal.resizable(0, 0)             # This prevents from resizing the window
cal.title("Calculator")
cal.configure(bg="light pink")   # Setting background color

# Function to play button press sound
def play_sound():
    pygame.mixer.Sound("button_press.mp3").play()  # Play the sound effect

# Functions for calculator operations
def about():
    messagebox.showinfo('About'," \n Created by Harsh Bhardwaj \n \n  LinkedIn :\n  https://linkedin.com/in/harsh-bhardwaj-465369194")

def click_button(item):
    global expression
    inputText.set(inputText.get() + str(item))
    play_sound()  # Play button press sound

def clear_button():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])
    play_sound()  # Play button press sound

def clear_all():
    inputText.set("")
    play_sound()  # Play button press sound

def equal_button():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "_ERROR_"
        inputText.set(result)
    play_sound()  # Play button press sound

# Menu bar setup
menubar = Menu(cal, bg="light blue", fg="white")
filemenu = Menu(menubar, tearoff=0, bg="light blue", fg="white")
filemenu.add_command(label="Cut", accelerator="Ctrl+X")
filemenu.add_command(label="Copy", accelerator="Ctrl+C")
filemenu.add_command(label="Paste", accelerator="Ctrl+V")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=cal.quit)
menubar.add_cascade(label="Edit", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0, bg="light blue", fg="white")
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

cal.config(bg="light pink", menu=menubar)

# Input frame setup
expression = ""
inputText = StringVar()
inputFrame = Frame(cal, width=312, height=50, bd=0, highlightbackground="light blue", highlightcolor="yellow", highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 17 ), textvariable=inputText, width=50, fg="black", bg="white", bd=0, justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=19)

# Button frame setup
button_frame = Frame(cal, width=312, height=272.5, bg="light pink")
button_frame.pack()

# Buttons setup
clearall = Button(button_frame, text="C", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: clear_all())
clearall.grid(row=1, column=0, padx=1, pady=1)

l_bracket = Button(button_frame, text="(", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: click_button("("))
l_bracket.grid(row=1, column=1, padx=1, pady=1)

r_bracket = Button(button_frame, text=")", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: click_button(")"))
r_bracket.grid(row=1, column=2, padx=1, pady=1)

clear = Button(button_frame, text="<", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: clear_button())
clear.grid(row=1, column=3, padx=1, pady=1)

power = Button(button_frame, text="^", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: click_button("**"))
power.grid(row=2, column=0, padx=1, pady=1)

pie = Button(button_frame, text="π", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: click_button(3.1415))
pie.grid(row=2, column=1, padx=1, pady=1)

exp = Button(button_frame, text="e", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: click_button(2.7182))
exp.grid(row=2, column=2, padx=1, pady=1)

divide_ = Button(button_frame, text="/", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: click_button("/"))
divide_.grid(row=2, column=3, padx=1, pady=1)

seven = Button(button_frame, text="7", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: click_button(7))
seven.grid(row=3, column=0, padx=1, pady=1)

eight = Button(button_frame, text="8", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: click_button(8))
eight.grid(row=3, column=1, padx=1, pady=1)

nine = Button(button_frame, text="9", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: click_button(9))
nine.grid(row=3, column=2, padx=1, pady=1)

multiply = Button(button_frame, text="*", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: click_button("*"))
multiply.grid(row=3, column=3, padx=1, pady=1)

four = Button(button_frame, text="4", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: click_button(4))
four.grid(row=4, column=0, padx=1, pady=1)

five = Button(button_frame, text="5", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: click_button(5))
five.grid(row=4, column=1, padx=1, pady=1)

six = Button(button_frame, text="6", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: click_button(6))
six.grid(row=4, column=2, padx=1, pady=1)

minus = Button(button_frame, text="-", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: click_button("-"))
minus.grid(row=4, column=3, padx=1, pady=1)

one = Button(button_frame, text="1", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: click_button(1))
one.grid(row=5, column=0, padx=1, pady=1)

two = Button(button_frame, text="2", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: click_button(2))
two.grid(row=5, column=1, padx=1, pady=1)

three = Button(button_frame, text="3", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: click_button(3))
three.grid(row=5, column=2, padx=1, pady=1)

plus = Button(button_frame, text="+", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: click_button("+"))
plus.grid(row=5, column=3, padx=1, pady=1)

point = Button(button_frame, text=".", fg="black", width=10, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: click_button("."))
point.grid(row=6, column=0, padx=1, pady=1)

zero = Button(button_frame, text="0", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: click_button(0))
zero.grid(row=6, column=1, padx=1, pady=1)

equals = Button(button_frame, text="=", fg="crimson", width=21, height=3, bd=0, bg="light blue", cursor="hand2", command=lambda: equal_button())
equals.grid(row=6, column=2, columnspan=2, padx=1, pady=1)

# Additional text
made_by_label = Label(cal, text="Made by:- Harsh Bhardwaj", font=('arial', 10), bg="light pink")
made_by_label.pack(side=BOTTOM, pady=5)

cal.mainloop()  # mainloop() is an infinite loop used to run the application
