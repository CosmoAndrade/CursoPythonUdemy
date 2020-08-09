class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} está comendo")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)        

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

gato = Gato("Bichano", "Branco")
cachorro = Cachorro("Totó", "Preto")
coelho = Coelho("Pernalonga", "Cinza")

gato.comer()
cachorro.comer()
coelho.comer()