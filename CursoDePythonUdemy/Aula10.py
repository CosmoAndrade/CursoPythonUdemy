# if - else - elif
# if -> se 
# else -> senão
# elif -> senão se 

idade = int (input ('Digite sua idade: '))

# if idade >= 18:
#     print ('Maior de idade!')
# else:
#     print ('Menor de idade!')    

maior = idade >=18 and idade < 60
menor = idade < 18

if maior:
    print ('Maior de idade!')
elif menor:
    print ('Menor de idade!')
else:
    print ('Melhor idade!')        