from Automovel import Automovel

class Moto(Automovel):
    """ Classe de Moto que herda de Automóvel"""

    # velocidade maxima é um atributo de classe de Moto que
    # será herdada por todas as instancias de Moto
    VELOCIDADE_MAXIMA = 160

    # O def init aqui está herdando o init de automóvel com o método especial super
    # Não precisamos passar um parâmetro velocidade pois o super também não passa
    def __init__(self, marca=None, modelo=None):
        super().__init__(marca, modelo)

    def acelera(self):
        # aqui o super está pegando a velocidade definida em Automovel
        if self.velocidade >= self.VELOCIDADE_MAXIMA:
            self.velocidade = 160
            raise ValueError('Velocidade Máxima atinginda')

        self.velocidade += 30
   