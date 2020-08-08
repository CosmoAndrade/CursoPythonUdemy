# class -> Classes
# Atributos e Métodos

# class Pessoa:
#     # Atributos
#     nome = ''
#     idade = 0

#     # Métodos
#     def dados(self):
#         return(f'Nome:{self.nome} Idade:{self.idade}')


# # objeto
# p1 = Pessoa()
# p1.nome = 'Cosmo'
# p1.idade = 35
# print(p1.nome,p1.idade)
# print(p1.dados())


class Pessoa:
    # Método construtor ou inicial
    def __init__(self,valor_nome,valor_idade):
        self.nome = valor_nome
        self.idade = valor_idade

    def dados (self):
        return (f'Nome:{self.nome} Idade:{self.idade}')

    # get 
    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade     

    # set
    def set_nome (self,novo_nome):
        self.nome = novo_nome

    def set_idade(self,nova_idade):
        self.nome = nova_idade



p2 = Pessoa('Cosmo',35)
print (p2.dados())
print (p2.get_nome)
print (p2.set_nome('Lucas'))
print(p2.dados())

