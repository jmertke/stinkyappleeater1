import tkinter as tk
from tkinter import filedialog, Text
import numpy as np
import random

##############################################################################

def takebite():
    eatbutton.num_clicked += 1
    if eatbutton.num_clicked == 1:
        canvas.create_oval(50,300,300,500, fill="light yellow", outline="light yellow")
    elif eatbutton.num_clicked == 2:
        canvas.create_oval(50,400,300,700, fill="light yellow", outline="light yellow")
    elif eatbutton.num_clicked == 3:
        canvas.create_oval(450,300,750,500, fill="light yellow", outline="light yellow")
    elif eatbutton.num_clicked == 4:
        canvas.create_oval(475,400,750,700, fill="light yellow", outline="light yellow")
    elif eatbutton.num_clicked == 5:
        canvas.create_oval(100,300,400,650, fill="tan", outline="tan")
        canvas.create_oval(250,300,600,650, fill="tan", outline="tan")
        canvas.create_oval(50,300,300,500, fill="light yellow", outline="light yellow")
        canvas.create_oval(50,400,300,700, fill="light yellow", outline="light yellow")
        canvas.create_oval(450,300,750,500, fill="light yellow", outline="light yellow")
        canvas.create_oval(475,400,750,700, fill="light yellow", outline="light yellow")
        canvas.create_oval(325,440,340,460, fill="saddlebrown", outline="saddlebrown")
        canvas.create_oval(400,440,450,460, fill="saddlebrown", outline="saddlebrown")
        canvas.create_oval(350,500,450,530, fill="saddlebrown", outline="saddlebrown")
        canvas.create_oval(415,430,435,470, fill="saddlebrown", outline="saddlebrown")
        canvas.create_oval(360,510,440,540, fill="tan", outline="tan")
        canvas.create_text(400,570,text="EW! YOU ATE A STINKY APPLE", fill="green", font="Times 40 italic bold")
        canvas.create_text(402,572,text="EW! YOU ATE A STINKY APPLE", fill="purple", font="Times 40 italic bold")
        canvas.itemconfig(applecountertext, text="1")
        

    elif eatbutton.num_clicked >= 6:
        appledivide=(np.floor(eatbutton.num_clicked/6))
        neweat = eatbutton.num_clicked-(6*appledivide)    

        if neweat == 0:
            canvas.create_rectangle(0,280, 800,700, fill="light yellow", outline="light yellow")

            randomapple=random.randint(1,20)
            if randomapple == 1:
                canvas.create_oval(100,250,500,700, fill="green", outline="green")
                canvas.create_oval(300,250,700,700, fill="green", outline="green")
            elif randomapple == 2:
                canvas.create_oval(100,250,500,700, fill="gold", outline="gold")
                canvas.create_oval(300,250,700,700, fill="gold", outline="gold")
            else:
                canvas.create_oval(100,250,500,700, fill="firebrick", outline="firebrick")
                canvas.create_oval(300,250,700,700, fill="firebrick", outline="firebrick")
                    
        elif neweat == 1:
            canvas.create_oval(50,300,300,500, fill="light yellow", outline="light yellow")
            neweat +=1
        elif neweat == 2:
            canvas.create_oval(50,400,300,700, fill="light yellow", outline="light yellow")
            neweat +=1
        elif neweat == 3:
            canvas.create_oval(450,300,750,500, fill="light yellow", outline="light yellow")
            neweat +=1
        elif neweat == 4:
            canvas.create_oval(475,400,750,700, fill="light yellow", outline="light yellow")
            neweat +=1
        elif neweat == 5:
            canvas.create_oval(100,300,400,650, fill="tan", outline="tan")
            canvas.create_oval(250,300,600,650, fill="tan", outline="tan")
            canvas.create_oval(50,300,300,500, fill="light yellow", outline="light yellow")
            canvas.create_oval(50,400,300,700, fill="light yellow", outline="light yellow")
            canvas.create_oval(450,300,750,500, fill="light yellow", outline="light yellow")
            canvas.create_oval(475,400,750,700, fill="light yellow", outline="light yellow")
            canvas.create_oval(325,440,340,460, fill="saddlebrown", outline="saddlebrown")
            canvas.create_oval(400,440,450,460, fill="saddlebrown", outline="saddlebrown")
            canvas.create_oval(350,500,450,530, fill="saddlebrown", outline="saddlebrown")
            canvas.create_oval(415,430,435,470, fill="saddlebrown", outline="saddlebrown")
            canvas.create_oval(360,510,440,540, fill="tan", outline="tan")
            canvas.create_text(400,570,text="EW! YOU ATE A STINKY APPLE", fill="green", font="Times 40 italic bold")
            canvas.create_text(402,572,text="EW! YOU ATE A STINKY APPLE", fill="purple", font="Times 40 italic bold")
            applecounter=int(np.ceil(eatbutton.num_clicked/6))
            print(applecounter)
            canvas.itemconfig(applecountertext, text=applecounter)
   

##############################################################################

root = tk.Tk()
root.title("Stinky Apple Eater")


canvas = tk.Canvas(root, height=700, width=800, bg="light yellow")
canvas.pack()

eatbutton = tk.Button(root, text="TAKE A BITE",
                      padx=10, pady=5, fg="firebrick", bg="green", command=takebite)
eatbutton.num_clicked = 0
eatbutton.pack()

canvas.create_rectangle(375,200, 425,300, fill="saddlebrown", outline="saddlebrown")
canvas.create_oval(100,250,500,700, fill="firebrick", outline="firebrick")
canvas.create_oval(300,250,700,700, fill="firebrick", outline="firebrick")

canvas.create_line(100,50, 150,100, 100,150, 150,200, smooth=1, width=30, fill="green")
canvas.create_line(200,50, 250,100, 200,150, 250,200, smooth=1, width=30, fill="green")
canvas.create_line(300,50, 350,100, 300,150, 350,200, smooth=1, width=30, fill="green")

canvas.create_line(550,50, 500,100, 550,150, 500,200, smooth=1, width=30, fill="green")
canvas.create_line(650,50, 600,100, 650,150, 600,200, smooth=1, width=30, fill="green")
canvas.create_line(750,50, 700,100, 750,150, 700,200, smooth=1, width=30, fill="green")

canvas.create_text(402,52,text="STINKY APPLE EATER", fill="light yellow", font="Times 70 italic bold") 
canvas.create_text(400,50,text="STINKY APPLE EATER", fill="firebrick", font="Times 70 italic bold")

applecountertext= canvas.create_text(400,240,text="", fill="black", font="Times 30 italic bold")

bitecounter=0
##############################################################################

root.mainloop()
