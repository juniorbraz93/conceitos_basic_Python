jogador_loteria1 = {
  'nome': 'João',
  'numeros': (13,4,52,23,67,82)
}

jogador_loteria2 = {
  'nome': 'João',
  'numeros': (13,4,52,23,67,82)
}


print(jogador_loteria1 == jogador_loteria2) # Objeto não resceve um valor true mesmo sendo iguais


# Classe pe um modelo ou uma representação de um objeto
# Objeto e uma instância de um classe


class JogadorLoteria:
  def __init__(self):
    self.nome = 'Pedro'
    self.numeros = (13,4,52,23,67,82)
  def total(self):
    return sum(self.numeros)

jogador_1 = JogadorLoteria()

jogador_2 = JogadorLoteria()

print(jogador_1.nome)
print(jogador_1.numeros)
print(jogador_1.total())


print(jogador_1 == jogador_2) # Objeto não resceve um valor true mesmo sendo iguais
