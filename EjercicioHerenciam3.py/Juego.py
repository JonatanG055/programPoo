class Juego:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        
    def empezar_juego(self):
        print("¡Que comience el juego!")
        
class Jugador1:
    def __init__(self, luchador):
        self.luchador = luchador
        self.vida = 100
        
    def golpear(self, jugador2):
        jugador2.vida -= 30
        print(f"{self.luchador} golpea a {jugador2.luchador} y le resta 30 puntos de vida.")
        print(f"La vida de {jugador2.luchador} es ahora {jugador2.vida}.")
        
class Jugador2:
    def __init__(self, luchador):
        self.luchador = luchador
        self.vida = 100
        
    def golpear(self, jugador1):
        jugador1.vida -= 30
        print(f"{self.luchador} golpea a {jugador1.luchador} y le resta 30 puntos de vida.")
        print(f"La vida de {jugador1.luchador} es ahora {jugador1.vida}.")
j1 = Jugador1("Luchador1")
j2 = Jugador2("Luchador2")

juego = Juego(j1, j2)
juego.empezar_juego()

j1.golpear(j2)
j2.golpear(j1)
