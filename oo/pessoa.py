class Pessoa:
    def __init__(self,*filhos, nome = None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}{self}'

if __name__ == '__main__':
    vinicius = Pessoa(nome='Vinicius G')
    antonio = Pessoa(vinicius, nome = 'Antonio')
    print(Pessoa.cumprimentar(antonio))
    print(id(antonio))
    print(antonio.cumprimentar())
    print(antonio.nome)
    print(antonio''.idade)
    for filho in antonio.filhos:
        print(filho.nome)
    antonio.sobrenome = 'Giacomini'
    del antonio.filhos
    print(antonio.__dict__)
    print(vinicius.__dict__)
    print(antonio.sobrenome)
