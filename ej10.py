import modulos
names = """Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA,
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia,
Francsica', FEDERICO, Fernanda, GONZALO, Nancy"""
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0,11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2,3, 0, 0]
assits = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1,0]

jugadores = names.replace(",","")
jugadores = jugadores.lower()
jugadores = jugadores.replace("\n"," ")
jugadores= jugadores.split(" ")

#print(jugadores.index("Agustin"))
deck = modulos.DeckMain1(jugadores, goals, goals_avoided, assits)
modulos.GolesXjugador(deck);
#modulos.GolesXjugado(deck)
modulos.elMejorJugador(deck)
print(f"Lel promedio de goles por partido fue de: {modulos.promGoles(goals)}")
print(modulos.promGolesXjugador(deck))