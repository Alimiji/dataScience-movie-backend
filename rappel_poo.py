class Chien:
    pass

### Instance ou objet de la classe

mon_chien = Chien()

print(type(mon_chien))


### Class et attributs

class Chien:
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race

mon_chien = Chien("Rèce", "Labrador")

print("Nom du chien:", mon_chien.nom, "Race du chien:", mon_chien.race)


#### Class + methode

class Chien:

    def __init__(self, nom, race):
        self.nom = nom
        self.race = race

    def aboyer(self):
        print(self.nom + " aboie")

rex = Chien("Rex", "Berger allemand")

rex.aboyer()