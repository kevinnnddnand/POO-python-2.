
class Mago:
    def hechizos(self):
        print("Lanza un hechizo")

class Guerrero(Mago):
    def defensa(self):
        print("Usa una defensa")

class Elfo(Mago):
    def aura(self):
        print("Activa un aura ")

class DarkLord(Guerrero, Elfo):
    pass

dark = DarkLord()

dark.hechizos()
dark.defensa()
dark.aura()

print(DarkLord.__mro__)