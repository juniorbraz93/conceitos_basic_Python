minha_variavel = 'ola mundo'

print(len(minha_variavel))

# for ==> Para
# While ==> Enquanto

for caracter in minha_variavel:
  print(caracter)


lista = [0,1,2,3,4,5,6,7,8,9,10]

print(lista)

print(list(range(11)))

print(list(range(1,10,2)))

n_parers = list(range(0, 11, 2))


print(n_parers)

for numero in n_parers:
  quadrado = numero ** 2
  print(quadrado)