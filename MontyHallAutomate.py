
##### Imports #####
import tkinter as tk
from tkinter import messagebox
import ctypes
from ctypes import wintypes
import time
import tempfile
import os
import sys
import random as rnd

##### Create Vars #####
door=0
tgames=0
twins=0
tloss=0

wgames=0
wwins=0
wloss=0

rgames=0
rwins=0
rloss=0

def displayStats():
    buStr = "Stay Win Percent: "
    if tgames != 0:
        buStr = buStr + str(round(float(twins)/float(tgames)*float(100),2)) + "% "
    else:
        buStr = buStr + "..% "
    buStr = buStr + "Wins: " + str(twins)
    buStr = buStr + " Loss: " + str(tloss)
    lblStayStats.config(text=buStr)

    buStr = "Swap Win Percent: "
    if wgames != 0:
        buStr = buStr + str(round(float(wwins)/float(wgames)*float(100),2)) + "% "
    else:
        buStr = buStr + "..% "
    buStr = buStr + "Wins: " + str(wwins)
    buStr = buStr + " Loss: " + str(wloss)
    lblSwapStats.config(text=buStr)

    buStr = "Rand Win Percent: "
    if rgames != 0:
        buStr = buStr + str(round(float(rwins)/float(rgames)*float(100),2)) + "% "
    else:
        buStr = buStr + "..% "
    buStr = buStr + "Wins: " + str(rwins)
    buStr = buStr + " Loss: " + str(rloss)
    lblRandStats.config(text=buStr)

def iterateOnce():
    closedDoors=[
        0,
        1,
        2
    ]
    ans=rnd.randrange(0,3)
    slct=rnd.randrange(0,3)
    #print("##### ROUND START #####")
    #print("Strat: " + str(strat.get()))
    #print("answer is: " + str(ans) + " player first selection is: " + str(slct))

    #open a door
    choice=[
        0,
        1,
        2
    ]
    choice.remove(ans)
    try:
        choice.remove(slct)
        closedDoors.remove(choice[0])
        #print("Player wasn't right first time")
    except:
        #print("Player was right the first time")
        closedDoors.remove(choice[rnd.randrange(0,2)])
        #time.sleep(1)

    #swap or stay
    if(strat.get()=="swap"):
        closedDoors.remove(slct)
        slct=closedDoors[0]
    elif(strat.get()=="rand"):
        if(rnd.randrange(0,2)):
            closedDoors.remove(slct)
            slct=closedDoors[0]

    #determine the win/Loss and assign to stats based on strategy
    global tgames
    global twins
    global tloss
    global wgames
    global wwins
    global wloss
    global rgames
    global rwins
    global rloss

    if(strat.get()=="swap"):
        wgames = wgames + 1
        if(ans==slct):
            #winner winner
            wwins = wwins + 1
            #print("player wins")
        else:
            wloss = wloss + 1
            #print("player losses")
    elif(strat.get()=="stay"):
        tgames = tgames + 1
        if(ans==slct):
            #winner winner
            twins = twins + 1
            #print("player wins")
        else:
            tloss = tloss + 1
            #print("player losses")
    else:
        rgames = rgames + 1
        if(ans==slct):
            #winner winner
            rwins = rwins + 1
            #print("player wins")
        else:
            rloss = rloss + 1
            #print("player losses")

def iterate():
    if(verNum):
        times=int(txtTTR.get())
        for i in range(0,times):
            iterateOnce()
            #print("remaining iterations: " + str(times-1-i))

        displayStats()

def verNum():
    print("check")
    if(not str(txtTTR.get()).isdigit()):
        messagebox.showinfo("ERROR", "Times to run requires a interger")
        txtTTR.delete(0,'end')
        return False
    else:
        return True

##### Create the GUI #####
#Create the window container
w=tk.Tk()
w.title("Monty Hall Simulator")
#w.iconbitmap(default=os.path.join(application_path, iconFile))
w.resizable(False, False)

## Create time to run lbl ##
lblTTR=tk.Label(w,text="Times to Run:")
lblTTR.grid(row=0, column=0, pady=7, sticky="e")

## Create Times to iterate ##
txtTTR=tk.Entry(w,text=10)
txtTTR.grid(row=0, column=1, pady=7, sticky="w")

## Create Strategy ##
strat=tk.StringVar()
strat.set("stay")
rbSwap=tk.Radiobutton(w, text="Swap Strategy", variable=strat, value="swap", indicatoron=0, width=15, height=5)
rbSwap.grid(row=1, column=0, padx= 5, pady=10)
rbStay=tk.Radiobutton(w, text="Stay Strategy", variable=strat, value="stay", indicatoron=0, width=15, height=5)
rbStay.grid(row=1, column=1, padx= 5, pady=10)
rbStay=tk.Radiobutton(w, text="Random Strategy", variable=strat, value="rand", indicatoron=0, width=15, height=5)
rbStay.grid(row=1, column=2, padx= 5, pady=10)

### Create run button ###
btnRun=tk.Button(w, text='Iterate', width=25, command=iterate)
btnRun.grid(row=2, column=0, columnspan=3, pady=7)

### Create statistics label ###
lblStayStats=tk.Label(w,text="xxx")
lblStayStats.grid(row=3, columnspan=3, pady=7)
lblSwapStats=tk.Label(w,text="xxx")
lblSwapStats.grid(row=4, columnspan=3, pady=7)
lblRandStats=tk.Label(w,text="xxx")
lblRandStats.grid(row=5, columnspan=3, pady=7)

##### Run some code #####
displayStats()
w.mainloop()
# main()
