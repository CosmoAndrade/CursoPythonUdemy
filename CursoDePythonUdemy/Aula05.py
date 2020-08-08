# Manipulação de strings

# len ()        -> Retorna o tamanho da string
# capitalize () -> Retorna a string com a primeira letra maiúsculas
# upper ()      -> Retorna a string com as letra maiúsculas
# lower ()      -> Retorna a string com as letra minúsculas
# title ()      -> Retorna todas a primeiras letras de cada palavra em maiúsculas
# split ()      -> Retorna uma lista , utilizando espaços como referência
# cout  ()       -> Retorna quantas vezes um caracteres aparece na string
# strip ()      -> Remove os espaços em branco da string

print ('Curso de Python')
print ("Curso de Java")
#        0123456789     
curso = 'Curso de Python'
print (len(curso))
print (curso[0:5])

print (curso.capitalize())

print(curso.lower())

print (curso.title())

print (curso.split())

print (curso.count('o'))

fruta = '     Banana     '
print(fruta.strip())




