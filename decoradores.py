import functools

def meu_decorador(funcao):
  @functools.wraps(funcao)
  def funcao_rodar():
    print('Embrulhando a função no decorador!')
    funcao()
    print('Fechando Embulho')
  return funcao_rodar

@meu_decorador  
def minha_funcao():
  print('Eu sou uma FUNÇÂO')

minha_funcao()