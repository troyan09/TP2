"""def DeckMain(names, goals,goals_avoided ,assits):
    deck ={}
    print(type(deck))
    for jugador in names:
        ide=names.index(jugador);
        stats = [goals[ide],goals_avoided[ide], assits[ide]]
        deck[jugador] = stats; 
    return deck"""

def DeckMain1(names, golas, golas_avaided, assits):
    stats = zip(golas, golas_avaided, assits);
    deck = dict(zip(names, stats))
    #print (deck);
    return deck;


def GolesXjugador(decks):
    for elem in decks:
        print(f"El jugador {elem}  anoto un total de:{ decks[elem][0]}")
    pass

def elMejorJugador(deck):
    golesAf = 1.5
    golesEvi = 1.25
    asist = 1;
    prom_max = -1
    nom = ""
    for jugador in deck:
        #Sumamos la lista de sus estadisticas[...]
        suma = deck[jugador][0] * golesAf + deck[jugador][1] * golesEvi + deck[jugador][2]*asist
        if suma > prom_max:
            prom_max = suma;
            nomb = jugador;
    print(f"El jugar mas influyente fue: {nomb} con un promedio de: {suma}")

def promGoles(goles):
    total = sum(goles)
    return total / 25 
    
def promGolesXjugador(decks):
    nom = input("Ingrese un nombre para ver su promedio de goles: ... ")
    if(nom in decks):
        prom = decks[nom][0]
        prom /= 25
        return f"El promedio de goles a lo largo de 25 partidos del jugador {nom}, fue de: {prom}"
    else:
        return "El nombre que escriviste no se encuentra en los datos:..."