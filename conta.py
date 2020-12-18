"""missing docstring"""
class Conta:
    """clase de Conta"""
    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto...')
        # lembrando que o underscore significa que o atributo
        # é reservado
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        """Função que imprime o saldo"""
        print(self.__saldo)

    def deposita(self, valor):
        """Função que deposita"""
        self.__saldo += valor
    def __pode_sacar(self, valor):
        """função que analisa se o usuário pode sacar"""
        return self.__saldo + self.__limite >= valor

    def saca(self, valor):
        """Função que saca"""
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('você não tem saldo disponível para esse valor')

    def transfere(self, valor, destino):
        """Função que transfere"""
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        """Função que retorna o saldo"""
        return self.__saldo
    @property
    def titular(self):
        """Função que retorna o titular"""
        return self.__titular
    @property
    def limite(self):
        """Função que retorna o limite"""
        return self.__limite
    @limite.setter
    def limite(self, limite):
        """seta o limite"""
        self.__limite = limite

    @staticmethod
    def codigo():
        """
        método estático da classe, pode ser chamada
        sem instância
        """
        return '001'



# atributos é o que o objeto de uma classe tem
# métodos é o que o objeto de uma classe sabe fazer
# Para perceber se um método deve fazer parte de uma
# classe, verifique se é possível usar o self dentro
# dele.
# Uma classe deve ter apenas uma responsabilidade
