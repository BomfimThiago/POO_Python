from abc import ABC, abstractmethod

# ao fazer a classe Automovel herdar de ABC eu estou dizendo que ela é uma classe abstrata
# que todas ou algumas das suas funções serão obrigatórias a ser implementadas pelas classes filhas
# Essa forma de herdar de ABC é um meio de fazer uma interface de maneira formal no python
# Automovel é então uma Interface que será usada por outras classes
class Automovel(ABC):
    """ Classe de automóvel que será herdade pela classe carro e moto"""

    def __init__(self, marca=None, modelo=None):
        """Na função init que é uma função construtora nós escrevemos como um objeto
        Automóvel poderia ser inicializado, com a marca e o modelo que por padrão serão None"""

        # Em python é possível criar parâmetros em tempo de execução, por isso o self._marca
        # cria em tempo de execução um parâmetro marca na classe automóvel,
        # o mesmo ocorre para o _modelo e _velocidade
        # quando usamos o underscore por convenção dizemos que esse é um atributo protegido
        # que só será acessível por meio de um get e um set
        self._velocidade = 100
        self._marca = marca
        self._modelo = modelo

    # Para definir um getter e setter em python podemos usar os decorators @property que é o getter
    # E @atributo.setter que é o setter
    @property
    def velocidade(self):
        return self._velocidade

    @velocidade.setter
    def velocidade(self, vel):
        self._velocidade = vel

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    # Esse método abstract obriga a classe filha de automovel a implementar uma função acelera
    # Implementei assim porque o acelera vai depender da velocidade máxima da classe de Carro ou Moto
    @abstractmethod
    def acelera(self):
        return

    def desalecera(self):
        if self.velocidade <= 0:
            self.velocidade = 0
            raise ValueError('Automóvel já com velocidade igual a 0')
        self._velocidade -= 30
