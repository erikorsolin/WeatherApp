from cidade import Cidade
while True:
    nome = input('Digite o nome da cidade que deseja obter as condições meteorológicas: ')
    c1 = Cidade(nome)
    c1.call_api()
    print('Descrição: {}'.format(c1.descricao))
    print('Temperatura: {:.2f} C'.format(c1.temperatura))
    print('Sensação térmica: {:.2f} C'.format(c1.sensacao))
    print('Temperatura Mínima: {:.2f} C'.format(c1.minima))
    print('Temperatura Máxima: {:.2f} C'.format(c1.maxima))
    print('Pressão Atmosférica: {}"Hg'.format(c1.pressao))
    print('Umidade: {}'.format(c1.umidade))
    print('Velocidade do vento: {:.2f} KM/h'.format(c1.speedVento))

    w = input('Encerrar Programa[S/N]: ').upper()
    if w == "N":
        break

