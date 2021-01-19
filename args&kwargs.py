def soma_2_numeros(arg1, arg2):
  return arg1 + arg2

print(soma_2_numeros(5,6))

def soma_5_numeros(arg1, arg2, arg3, arg4, arg5):
  return arg1 + arg2 + arg3 + arg4 + arg5

print(soma_5_numeros(5,6,5,6,2)) 

def lista_somada(lista):
  return sum(lista)

print(lista_somada([3,6,7,3,2]))

def soma_simplificada(*args):
  return sum(args)

print(soma_simplificada(6,3,5,7,4))

def metodo_kwargs(*args, **kwargs):
  print(args)
  print(kwargs)

metodo_kwargs(3,'sasa',4,'qualque coisa',nome='Junior',idade=27)

# args vem antes dos kwargs
