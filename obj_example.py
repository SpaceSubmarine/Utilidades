class Pokemon:
    def __init__(self, name, type, level):
        self.name = name
        self.type = type
        self.level = level


# Crea dos objetos de la clase Pokemon
pikachu = Pokemon("Pikachu", "electric", 5)
charmander = Pokemon("Charmander", "fire", 3)

# Accede a las propiedades de cada objeto
print(pikachu.name)  # imprime "Pikachu"
print(charmander.type)  # imprime "fire"
print(pikachu.level)  # imprime 5
