"""First line docstring"""
from abc import ABC
from collections.abc import MutableSequence
from numbers import Complex

class Programa:
    """Modelo de Programa"""
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        """Sobrescrevendo nome"""
        return self._nome.title()
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @property
    def ano(self):
        """Sobrescrevendo ano"""
        return self.__ano
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def dar_like(self):
        """dar like"""
        self._likes += 1
    def __str__(self):
        """imprime"""
        return f'{self.nome}-{self.ano}-{self._likes}'

class Filme(Programa):
    """Modelo de Filme"""
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        """Sobrescrevendo duracao"""
        return self.__duracao
    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao
    def __str__(self):
        """imprime"""
        return f'{self.nome}-{self.ano}-{self.duracao}-{self._likes}'


class Serie(Programa):
    """Modelo de Serie"""
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        """Sobrescrevendo temporadas"""
        return self.__temporadas
    @temporadas.setter
    def temporadas(self, temporadas):
        self.__temporadas = temporadas

    def __str__(self):
        """imprime"""
        return f'{self.nome}-{self.ano}-{self.temporadas}-{self._likes}'

class Playlist():
    """modelo de playlist"""
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        """posso tratar a instancia dessa classe \
        agora como uma lista ex instancia[0]"""
        return self._programas[item]

    def __len__(self):
        """posso agora fazer len(instancia)"""
        return len(self._programas)

    def __eq__(self, outra_playlist):
        """agora posso comparar objetos do tipo Playlist \
        por nome"""
        return self.nome == outra_playlist.nome

    def __ne__(self, outra_playlist):
        """sempre que implemtar o __eq__() é bom implementar
        o __ne__()"""
        return self.nome != outra_playlist.nome

    @property
    def listagem(self):
        """sobreescrever get listagem"""
        return self._programas
    @property
    def tamanho(self):
        """return tamanho"""
        return len(self._programas)



vingadores = Filme('vingadores', 2018, 160)
print(vingadores.nome)
print(vingadores.ano)
print(vingadores.duracao)
serie = Serie('star trek', 2020, 3)
print(serie.nome)
print(serie.ano)
print(serie.temporadas)

print('teste de string '
      'que deveria estar na mesma linha')

filmes_e_series = [vingadores, serie]
playlist = Playlist('fim de semana', filmes_e_series)
for programa in filmes_e_series:
    print(programa)

livros = Numero()

print(playlist.tamanho)
print(playlist[0])
print(len(playlist))

# Um atributo de classe quando mudado na instância não é mudado na classe
# ou seja o valor para novas instâncias continua o inicial definido na classe
