class Pessoa:
    olhos = 2

    def __init__(self,*filhos, nome = None, idade=33,):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
        olhos=2

    def cumprimentar(self):
        return f'Olá {id(self)}{self}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    vinicius = Pessoa(nome='Vinicius G')
    antonio = Pessoa(vinicius, nome = 'Antonio')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(vinicius.olhos)
    print(antonio.olhos)
    print(id(Pessoa.olhos), id(antonio.olhos), id(vinicius.olhos))
    print(Pessoa.metodo_estatico(),antonio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),antonio.nome_e_atributos_de_classe())