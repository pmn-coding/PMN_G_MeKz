#Autor: Kreuzer, Martin
#Datum: Freitag, 16.8.2019, 16:34
#Programm: Einfacher erster Assisstenzbot




from random import *
from tkinter import *
from os import *
from time import *
from webbrowser import *
from sys import *




#Functions--------------------------------------------------------------------------------------------------------------------------------------------------


#Fenster erstellen 
def window():
    global win
    win = Tk()
    win.title("J.A.R.V.I.S")
    win.geometry("300x300")
    win.config(bg = "white")

#Einführen er Elemente auf dem Fenster
def elem():
    global answ
    global exc

    answ = Label(win, text = "Hello. How can I help you?\n Oh and i am not that intelligent.\nPlease just one task after another, thank you.\n")
    exc = Entry(win)

#Anzeigen der Elemente auf dem Fenster
def elem_init():
    answ.pack()
    exc.pack()

def passwd():
    global pwd
    pwd = ""
    amt = randint(8, 20)
    for i in range(amt):
        #Bestimmt zufällige Zeichengruppe
        typ = randint(1,4)
    
        if typ == 1:
        
            #zufällige Zahl
            znum = chr(randint(48, 57))
        
        elif typ == 2:
        
            #zufälliger Großbuchstabe
            znum = chr(randint(65, 90))
            
        elif typ == 3:
        
            #zufälliger Kleinbuchstabe
            znum = chr(randint(97, 122))

        else:
        
            #zufälliges 'Symbol'
            znum = chr(randint(33, 47))
        
        #Zusammenfügen der Zeichen
        pwd += znum


#Hauptnebenprogramm-----------------------------------------------------------------------------------------------------------------------------------------

#Antwort
def answer(event):

    global tab
    global count
    global task
    global erase
    
    tab = 2
    count = 0
    task = ""

    task = exc.get()
    task = str(task)
    erase = len(task)

    smltlk()
    op()
    
#Begrüßung
def smltlk(): 
    if "hey" or "hi" or "hello" in task:                                                    #Achtung! Fehler!
        count = randint(1,3)
        if count == 1:
            answ.config(text = "Hello, sir. I can help you if you want.\n")
        elif count == 2:
            answ.config(text = "Still here, sir.\n")
        else:
            answ.config(text = "Hello, sir.\n")
    if "thank" in task:
        answ.config(text = "You're welcome. :)\n")

#Informationslieferung
def op():
    if "what" in task:
        if "name" and "your" in task:
            answ.config(text = "My name is Jarvis.\n")
        elif "time" in task:
            date = asctime(localtime(time()))
            answ.config(text = str(date)+"\n")
        else:
            answ.config(text = "Opened Google-Search.\n")
            open("https://www.google.com/search?client=firefox-b-d&q="+task)

    if "search" in task:
        answ.config(text = "Searched for "+(task.replace("search", ""))+"\n") 
        open("https://www.google.com/search?client=firefox-b-d&q="+(task.replace("search", "")))
    
    if "open" in task:
        if "internet" or "firefox" in task:
            open("https://www.google.com/webhp?client=firefox-b-d", tab)
            answ.config(text = "Opened Google.\n")

    if "want" in task:
        if "number" in task:
            num = str(randint(0,10))
            answ.config(text = num + "\n")

        if "password" in task:
            passwd()
            answ.config(text = pwd + "\n")
            
                

    if task == "":
        answ.config(text = "I do not know what you want. \nThere was no task mentioned.\n")

    if "goodbye" in task:
        win.destroy()
        exit()

    exc.delete(0, erase)
    

    
    

#Main---------------------------------------------------------Main------------------------------------------------------------------------------------------

window()
elem()
elem_init()

#Erfassen der Eingabebestätigung
win.bind("<Return>", answer)
answ.config(fg = "black",bg = "white")

win.mainloop()
