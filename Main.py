from Automovel import Automovel
from Carro import Carro
from Moto import Moto

if __name__ == '__main__':
    c = Carro('Chevrolet', 'Onix')
    m = Moto('Yamaha', '300')
    # O python tem métodos especiais que podem ser usados fazendo __metodo__(
    # esses dois underlines juntos são chamdos de dunder no python)
    # são vaŕios os métodos especiais ,usaremos alguns para demonstração

    # doc faz referencia a toda docstring usada para documentar aquela classe
    print('c.__doc__ ', c.__doc__)
    # dict traz o objeto ctomovel criado
    print('c.__dict__ ', c.__dict__)
    # module significa o modulo de classe usada, que no nosso caso é Carro
    print('c.__module__ ', c.__module__)
    # getattribute pega o valor do atributo passado como parametro, que no nosso caso é marca
    print('c.__getattribute__ ', c.__getattribute__('marca'))
    # setattr seta um atributo novo nessa instancia de automovel, chamado velocidade maxima
    print('c.__setattr__ ', c.__setattr__('velocidade_maxima', 250))
    # poderiamos pegar o valor desse novo atributo criado
    print('c.__getattribute__ ', c.__getattribute__('velocidade_maxima'))
    # sizeof traz o tamanho da instancia em bytes
    print('c.__sizeof__ ', c.__sizeof__())
    # Podemos também ver se Carro é uma instancia de Automovel
    print('isinstance(c, Automovel) ',isinstance(c, Automovel))


    # Podemos também usar os métodos criados por nós na classe
    c.acelera()
    c.acelera()
    c.acelera()
    c.desalecera()
    print('c.velocidade ', c.velocidade)

    m.acelera()
    m.acelera()
    m.desalecera()
    print('m.velocidade', m.velocidade)
   