class Funcionario():
  def __init__(self, nome, salario):
    self.nome = nome
    self.salario = salario
  
  def dados(self):
    return {'nome': self.nome, 'salario': self.salario}

fabio = Funcionario('Fabio', 1200)

print(fabio.dados())

class Admin(Funcionario):
  def __init__(self, nome, salario):
    super().__init__(nome, salario)

  def atualizar_dados(self, nome):
    self.nome = nome
    return self.dados()

print(fabio.dados())

fernando = Admin('Junior', 25000)

print(fernando.dados())

fernando.atualizar_dados('Fernando')

print(fernando.dados())
