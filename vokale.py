#Martin Kreuzer
#Stringbearbeitung

#Eingabe

word = input("Eingabe: ")

#Vokale entfernen
vokale = "AEIOUaeiou"

for v in word: 
    if v in vokale:
        word = word.replace(v, "")
print(word)
