#Feld
gr = 9
feld = []
for e in range(gr):
    feld.append(0)

for i in range(gr):
    cols = []
    for j in range(gr):
        cols.append(0)
    feld[i] = cols
    print(feld[i])

#Gameloop

end = False
while not end:
    
    player = True
    
    #Chip Eingabe
    if player:
        print("Spieler 1")

    else:
        print("Spieler 2")


    drop = int(input("Spalte(1-9): ")) - 1
    li = feld[drop]

    for n in li:
        if n == 0:
            if player:
                li[n] = 1
                player = False
                break
            else:
                li[n] = -1
                player = True
                break
    
    #Korrekte Ausgabe
    #out = []
    #for p in range(gr):
        #line = []
        #for p2 in range(gr):
            #ramfeld = feld[::-1][::-1]
            #line.append(ram)


    #Checken
    #Check y-achse
    for y in range(gr):

        sumy = 0

        for a in feld[y]:
            sumy += a

        #Ende
        if sumy == 4:
            print("Spieler 1 hat gewonnen.")
            end = True

        elif sumy == -4:
            print("Spieler 2 hat gewonnen.")
            end = True

        else:
            end = False

    #Check x-achse
   
    for x in range(gr):
        sumx = 0

        for b in range(gr):
            sumx += feld[b][x]
    
        #Ende
        if sumx == 4:
            print("Spieler 1 hat gewonnen.")
            end = True

        elif sumx == -4:
            print("Spieler 2 hat gewonnen.")
            end = True

        else:
            end = False