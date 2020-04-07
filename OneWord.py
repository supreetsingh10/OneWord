import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
from PyDictionary import PyDictionary as Pd


def test(wow):
    print("This is the "+ wow)


def display(shabad, matlab):
    if (shabad=="This is not a valid input") & (matlab== "try again"):
        var = StringVar()
        label = Label(lowerframe, textvariable=var, relief=RAISED)
        var.set("try again")
        label.pack()
    else:
        var = StringVar()
        label = Label(lowerframe,textvariable = var, relief = RAISED)
        var.set(str(shabad)+" : "+str(matlab))
        label.pack()


def mean(wordly):
    if (wordly == ' ') or (wordly ==''):
        error = "This is not a valid input"
        error2 = "try again"
        display(error,error2)

    else:
        mean = Pd.meaning(wordly)
        matlab = str(mean.values())
        display(wordly, matlab)
        return matlab


def safe(word, meaning):
    if(word==''):
        return 0
    else:
        with open('save.txt','w') as s:
            s.write(word+" "+meaning)


# wordsapiv1.p.rapidapi.com
# api key  "06b5cae637msh0f1de5811e195ecp1cdc0djsna313ddf3d7cf"
# http://127.0.0.1:8000/ my server

# setup

root = tk.Tk()
canvas = tk.Canvas(root, height = 500 ,width = 500 , bg = 'black')

frame = tk.Frame(root, bg = 'white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
canvas.pack()

record = tk.Button(root,text='vocabulary', padx=10, pady=5,fg='#076DD0', command=lambda: open('save.txt','r'))
record.place(relwidth=0.2, relheight=0.1, relx=0.6, rely=0.8)

lowerframe = tk.Frame(root, bg= '#73ABE1')
lowerframe.place(relwidth= 0.8,relheight =0.5,relx=0.1,rely=0.3)

label = tk.Label(lowerframe)
label.place(relwidth = 1, relheight = 1)

entry = tk.Entry(root, bg= "#076DD0")
entry.place(relw=0.6, relh=0.1, relx=0.2,rely=0.1)

go = tk.Button(root,text = 'Go', padx=10,pady=5, fg = "#076DD0",command=lambda: mean(entry.get()))
go.place(relwidth = 0.1, relheight = 0.1, relx = 0.8,rely=0.1)

save = tk.Button(root, text = "Save",padx = 10, pady = 5, fg='#076DD0', command=lambda: safe(entry.get(),mean(entry.get())))
save.place(relwidth = 0.2, relheight = 0.1, relx = 0.2, rely = 0.8)

search = tk.Label(root,text = 'definition',bg = '#076DD0')
search.place(relw = 0.4,relh=.1, relx= 0.3,rely= 0.2)

root.mainloop()
