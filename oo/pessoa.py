class Pessoa:
    olhos = 2

    def __init__(self,*filhos, nome = None, idade=33,):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
        olhos=2

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    vinicius = Mutante(nome='Vinicius G')
    antonio = Homem(vinicius, nome = 'Antonio')
    print(Pessoa.cumprimentar(antonio))
    print(id(antonio))
    print(antonio.cumprimentar())
    print(antonio.nome)
    print(antonio.idade)
    for filho in antonio.filhos:
        print(filho.nome)
    antonio.sobrenome = 'Giacomini'
    del antonio.filhos
    vinicius.olhos = 1
    del vinicius.olhos
    print(antonio.__dict__)
    print(vinicius.__dict__)
    print(Pessoa.olhos)
    print(vinicius.olhos)
    print(antonio.olhos)
    print(id(Pessoa.olhos), id(antonio.olhos), id(vinicius.olhos))
    print(Pessoa.metodo_estatico(),antonio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),antonio.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(vinicius, Homem))
    print(isinstance(vinicius, Homem))
    print(vinicius.olhos)
    print(vinicius.cumprimentar())
    print(antonio.cumprimentar())