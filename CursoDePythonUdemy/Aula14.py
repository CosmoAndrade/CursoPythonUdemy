import random
# while -> Enquanto

# x = 0
# while x < 10:
#     print (x)
#     x = x + 1

senha = random.randint(0,10)
# senha = 12345
leitura = 0
while senha != leitura:
    leitura = int (input('Digite a senha!'))
    if senha == leitura:
        print ('Acesso liberado!')
    else:
        print ('Senha incorreta , tente novamente')