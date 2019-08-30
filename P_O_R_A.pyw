#Autor: Kreuzer, Martin
#Datum: Freitag, 16.8.2019, 16:34
#Programm: Einfacher erster Assisstenzbot




from random import *
from tkinter import *
from os import *
from time import *
from webbrowser import *
from sys import *
import pyttsx3 as ts


#speak
id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
an = ""

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

#speaking
def speak(textspk):
    eg.say(textspk)
    eg.runAndWait()

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

    if "PORA" in task:
        task = task.replace("PORA", "")
        op()
        smltlk()
    else:
        exc.delete(0,erase)
    
#Begrüßung
def smltlk(): 

    if "hey" or "hi" or "hello" in task:
        
        count = randint(1,3)
        
        if count == 1:

            an = "Hello sir. What can I do for you?"
            answ.config(text = "Hello sir. What can I do for you?.\n")
            speak(an)
        
        elif count == 2:

            an = "Still here sir."
            answ.config(text = "Still here sir.\n")
            speak(an)
        
        else:

            an = "Hello sir."
            answ.config(text = "Hello sir.\n")
            speak(an)
    
    if "thank" in task:

        an = "You're welcome."
        answ.config(text = "You're welcome. :)\n")
        speak(an)

#Informationslieferung
def op():

    if "what" in task:

        if "name" and "your" in task:
            an = "My name is PORA."
            answ.config(text = "My name is PORA.\n")
            speak(an)
        
        elif "time" in task:
            date = asctime(localtime(time()))
            an = date +"."
            answ.config(text = str(date)+"\n")
            speak(an)
        
        else:
            an = "Opened Google-search."
            answ.config(text = "Opened Google-Search.\n")
            open("https://www.google.com/search?client=firefox-b-d&q="+task)
            speak(an)

    if "search" in task:
        an = "Searched for", (task.replace("search", ""))+"."
        answ.config(text = "Searched for "+(task.replace("search", ""))+"\n") 
        open("https://www.google.com/search?client=firefox-b-d&q="+(task.replace("search", "")))
        speak(an)
    
    if "open" in task:
        
        if "internet" or "firefox" in task:
            an = "Opened Google."
            answ.config(text = "Opened Google.\n")
            open("https://www.google.com/webhp?client=firefox-b-d", tab)
            speak(an)
            

    if "want" in task:
        
        if "number" in task:
            num = str(randint(0,10))
            an = num +"."
            answ.config(text = num + "\n")
            speak(an)

        if "password" in task:
            passwd()
            an = pwd +"."
            answ.config(text = pwd + "\n")
            speak(an)
            
                

    if task == "":
        an = "I do not know what you want. There was no task mentioned."
        answ.config(text = "I do not know what you want. \nThere was no task mentioned.\n")
        speak(an)

    if "goodbye" in task:
        an = "Goodbye sir."
        speak(an)
        win.destroy()
        exit()

    exc.delete(0, erase)
    

    
    

#Main---------------------------------------------------------Main------------------------------------------------------------------------------------------
#Sprache
eg = ts.init()
eg.setProperty("volume", 1)
eg.setProperty("voice", id)

#Fenster
window()
elem()
elem_init()
an = "Hello. I am PORA. How can I help you?"
speak(an)

#Erfassen der Eingabebestätigung
win.bind("<Return>", answer)
answ.config(fg = "black",bg = "white")

win.mainloop()
