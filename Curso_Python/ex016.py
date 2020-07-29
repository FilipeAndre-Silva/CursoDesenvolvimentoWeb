#Herança em Python

class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def msg_nomeCompleto(self):
        return print(self.nome + " " + self.sobrenome)

pessoa1 = Pessoa("Filipe","André")
pessoa1.msg_nomeCompleto()

#Uma classe chamada Aluno, que herdará as propriedades e métodos da Pessoa
class Aluno(Pessoa):
    pass

aluno1 = Aluno("Lucas","Ernanes")
aluno1.msg_nomeCompleto()

########################################################################################################################

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

aluno2 = Student("Filipq","André",2020)
aluno2.welcome()
aluno2.printname()
