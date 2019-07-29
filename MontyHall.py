
##### Imports #####
import tkinter as tk
import ctypes
from ctypes import wintypes
import time
import tempfile
import os
import sys
import random as rnd

##### Create Vars #####
rbDoors=[]
ans=rnd.randrange(0,3)
createDoors=[
    "1",
    "2",
    "3"
]

## Called when run is clicked ##
def RND1():
    print(ans)
    choice=[
        0,
        1,
        2
    ]
    choice.remove(ans)
    try:
        choice.remove(door.get())
    except:
        #time.sleep(1)
        print(ans)
        print(door.get())
    if(len(choice)==2):
        rbDoors[choice[rnd.randrange(0,2)]].config(text="SHIT ALL")
    else:
        rbDoors[choice[0]].config(text="SHIT ALL")

    btnRun.config(text="Confirm 2nd Choice", command=RND2)

def RND2():
    for val in range(0,3):
        if (val==ans):
            rbDoors[val].config(text="WINNER WINNER")
        else:
            rbDoors[val].config(text="SHIT ALL")
    btnRun.config(text="RESET?", command=RST)

def RST():
    global ans
    ans=rnd.randrange(0,3)
    btnRun.config(text="Confirm 1st Choice", command=RND1)
    for val in range(0,3):
        rbDoors[val].config(text=createDoors[val])


##### Create the GUI #####
#Create the window container
w=tk.Tk()
w.title("Monty Hall Simulator")
#w.iconbitmap(default=os.path.join(application_path, iconFile))
w.resizable(False, False)

## createDoors ##
door=tk.IntVar()
door.set(0)
col=0
for val in createDoors:
    rbDoors.append(tk.Radiobutton(w, text=val, variable=door, value=col, indicatoron=0, width=18, height=25))
    rbDoors[col].grid(row=0, column=col, padx=10, pady=10)
    col=col+1

rbDoors[0].select()

### Create run button ###
btnRun=tk.Button(w, text='Confirm 1st Choice', width=25, command=RND1)
btnRun.grid(row=3, column=0, columnspan=3, pady=7)

##### Run some code #####
w.mainloop()
# main()
