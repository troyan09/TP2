def DeckMain(names, goals,goals_avoided ,assits):
    deck ={}
    print(type(deck))
    for jugador in names:
        ide=names.index(jugador);
        stats = [goals[ide],goals_avoided[ide], assits[ide]]
        deck[jugador] = stats; 
    return deck

def GolesXjugado(decks):
    for elem in decks:
        print(f"EL jugador, {elem} anoto un total de:{decks[elem][0]} goles")
    pass