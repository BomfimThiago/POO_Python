"missing first line"
class Cliente:
    """classe cliente"""
    def __init__(self, nome):
        """funcao init"""
        self.__nome = nome

    # se eu quiser sobreescrever o método get de um atributo
    # eu posso declarar um método com o nome do atributo
    @property
    def nome(self):
        """sobreescrevendo o método get_nome"""
        print('chamando nome')
        return self.__nome.title()

    # é possível também reescrever o set
    @nome.setter
    def nome(self, nome):
        """seta o nome"""
        print('chamando o setter nome')
        self.__nome = nome
