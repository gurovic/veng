#coding:utf-8
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.commondialog import Dialog
import sys
import time

from tkinter import Frame, Text, Scrollbar, Pack, Grid, Place
from tkinter.constants import RIGHT, LEFT, Y, BOTH

askcolor = None
Banswer = None
answer = None

def move(x):
    if x1 != 475:
        x += 5
    else:
        pass
    return x

    

def color1():  
    global askcolor
    
    
    class Chooser(Dialog):
        "Ask for a color"
    
        command = "tk_chooseColor"
    
        def _fixoptions(self):
            try:
                # make sure initialcolor is a tk color string
                color = self.options["initialcolor"]
                if isinstance(color, tuple):
                    # assume an RGB triplet
                    self.options["initialcolor"] = "#%02x%02x%02x" % color
            except KeyError:
                pass
    
        def _fixresult(self, widget, result):
            if not result or not str(result):
                return None, None # canceled
    
    
            r, g, b = widget.winfo_rgb(result)
            return (r/256, g/256, b/256), str(result)
    
    
    def askcolor(color = None, **options):
        "Ask for a color"
    
        if color:
            options = options.copy()
            options["initialcolor"] = color
    
        return Chooser(**options).show()
    
    if __name__ == "__main__":
        askcolor = str(askcolor())
        
    a = askcolor.find("'")
    b = askcolor.find("')") + 1
    askcolor = askcolor[askcolor.find("'") + 1:askcolor.find("')")]
    return askcolor


def loading():
    global x1
    x1 = move(x1)
    can.create_rectangle(20, 70, 5 + x1, 80, fill = "green", width = 3)
    root.after(50, loading)

def start():
    root.destroy()

def change_size1(event):
    global but1
    but1.place(relx = 0.518, rely = 0.522, width = 170, height = 45)

def liv1(event):
    global but1
    but1.place(relx = 0.514, rely = 0.525, width = 165, height = 40)

def change_size2(event):
    global but2
    but2.place(relx = 0.459, rely = 0.592, width = 168, height = 45)

def liv2(event):
    global but2
    but2.place(relx = 0.455, rely = 0.595, width = 162, height = 38)
    
def change_size3(event):
    global but3
    but3.place(relx = 0.414, rely = 0.662, width = 151, height = 53)

def liv3(event):
    global but3
    but3.place(relx = 0.41, rely = 0.665, width = 146, height = 47)
    
def change_size4(event):
    global but4
    but4.place(relx = 0.374, rely = 0.745, width = 151, height = 49)

def liv4(event):
    global but4
    but4.place(relx = 0.37, rely = 0.748, width = 146, height = 43)
    
def change_size5(event):
    global but5
    but5.place(relx = 0.346, rely = 0.822, width = 154, height = 49)

def liv5(event):
    global but5
    but5.place(relx = 0.35, rely = 0.825, width = 149, height = 43)


def tutorial(event):
    global askcolor
    
    color1()  
    
    root=Tk()
    
    l, h = root.winfo_screenwidth() / 8, root.winfo_screenheight() / 17
    root.wm_geometry("+%d+%d" % (l, h))
    root.title('учебник')
    tut = Canvas(root, width = 990 , height = 500)
    tut.create_rectangle(-100, -100, 9290, 980, fill = askcolor)    
    background = Button(root, text = 'CHOOSE BACKGROUND', bg = 'mint cream', fg = '#00affb', font = 'arial 8')
    background.place(relx = 0.01, rely = 0.01, width = 125, height = 30)
    background.bind('<Button-1>', tutorial) 
    hello = Label(root, text = '''Данная программа является одним из немногих интерактивных учебников языка 
    программирования python 3.x. В нашу программу входят несколько типов заданий: 
    задания на проверку ваших знаний по сортировкам в языке python и задания на 
    знания основных операторов.  Чтобы приступить к заданиям, кликните по ним левой
    кнопкой мыши. Ответы к заданиям пишите в специально выделенной строке. Перед 
    выполнением заданий, настоятельно рекомендуем вам прочитать пункт меню “MANUAL”,
    где изложена основная теория, необходимая для выполнения заданий.''', bg = askcolor, font = 'aharoni 15')
    hello.place(relx = -0.03, rely = 0.1, width =1030, height = 400)
    
    tut.pack()   
    
    
def reincarnation(event):
    global Banswer
    Banswer = answer.get()
    return Banswer

def ex1(event):    
    global answer
    
    root = Tk()
    root.title('сортировки')
    root.geometry(newGeometry="300x200+500+250")
    lab = Label(root, text="ответ.", font="Arial 10")
    answer = Entry(root,width=20,bd=3)
    lab.pack()
    answer.pack()
    button = Button(root,text='OK',width=9)
    button.bind("<Button-1>", reincarnation)
    button.pack()
    root.mainloop()
    
    return answer    

def ex2(event):
    root = Tk()
    root.title('DONAT')
    root.geometry(newGeometry="300x200+500+250")
    lab = Label(root, text="чтобы открыть \n все задания,\n необходимо купить\n полную версию.", font="Arial 15")
    lab.pack()
    root.mainloop()    

def choose_color(event):
    pass

def manual(event):
    global askcolor
        
    color1()  
    
    root=Tk()
           
    l, h = root.winfo_screenwidth() / 8, root.winfo_screenheight() / 17
    root.wm_geometry("+%d+%d" % (l, h))
    root.title(' теоретическая информация')
    man = Canvas(root, width = 1000 , height = 400)
    man.create_rectangle(0, 0, 990, 980, fill = askcolor)    
    background = Button(root, text = 'CHOOSE BACKGROUND', bg = 'mint cream', fg = '#00affb', font = 'arial 8')
    background.place(relx = 0.01, rely = 0.01, width = 125, height = 30)
    background.bind('<Button-1>', manual) 
    hello = Label(root, text = ' rfrqnj текст.\n непонятный.', bg = askcolor, font = 'aharoni 25')
    hello.place(relx = 0.2, rely = 0.1, width = 300, height = 100)
    
    man.pack()

    
def exit(event):
    sys.exit()
    
    

root=Tk()

x1 = 20

l, h = root.winfo_screenwidth() / 3.5, root.winfo_screenheight() / 3
root.wm_geometry("+%d+%d" % (l, h))
can = Canvas(root, width = 500 , height = 100)
can.create_rectangle(0, 0, 10000, 10000, fill = "white")
can.create_rectangle(20, 70, 480, 80, fill = "red", width = 3)

hello = Label(root, text = ' Loading. Please, wait.', bg = 'white', fg = 'black', font = 'batang 20')
hello.place(relx = 0.14, rely = 0.1, width = 350)

can.pack()
root.after(200, loading) 
root.overrideredirect(1)
root.after(7000, start)

root.mainloop()


root=Tk()
l, h = root.winfo_screenwidth() / 4, root.winfo_screenheight() / 17
root.wm_geometry("+%d+%d" % (l, h))
root.title('БУДЬ МУЖИКОМ,  УЧИ ПИТОН!!!!!!!!!!!')
can = PhotoImage(file = "sky.gif")
w = Label(root, compound = CENTER, image = can).pack(side = "right")


but1 = Button(root, text = 'TUTORIAL', bg = 'grey', fg = '#00affb', font = 'arial 15')
but2 = Button(root, text = 'SORT', bg = 'grey', fg = '#00affb', font = 'arial 15')
but3 = Button(root, text = 'EXERCICE 2', bg = 'grey', fg = '#00affb', font = 'arial 15')
but4 = Button(root, text = 'MANUAL', bg = 'grey', fg = '#00affb', font = 'arial 15')
but5 = Button(root, text = 'EXIT', bg = 'grey', fg = '#00affb', font = 'arial 15')



but1.place(relx = 0.514, rely = 0.525, width = 165, height = 40)
but2.place(relx = 0.455, rely = 0.595, width = 162, height = 38)
but3.place(relx = 0.41, rely = 0.665, width = 146, height = 47)
but4.place(relx = 0.37, rely = 0.748, width = 146, height = 43)
but5.place(relx = 0.35, rely = 0.825, width = 149, height = 43)


but1.bind('<Motion>', change_size1)
but1.bind('<Leave>', liv1)
but2.bind('<Motion>', change_size2)
but2.bind('<Leave>', liv2)
but3.bind('<Motion>', change_size3)
but3.bind('<Leave>', liv3)
but4.bind('<Motion>', change_size4)
but4.bind('<Leave>', liv4)
but5.bind('<Motion>', change_size5)
but5.bind('<Leave>', liv5)

but1.bind('<Button-1>', tutorial)
but2.bind('<Button-1>', ex1)
but3.bind('<Button-1>', ex2)
but4.bind('<Button-1>', manual)
but5.bind('<Button-1>', exit)


root.mainloop()
