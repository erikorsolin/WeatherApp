from chaves import chave

import requests
class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.descricao = ''
        self.temperatura = 0
        self.sensacao = 0 
        self.minima = 0
        self.maxima = 0
        self.pressao = 0
        self.umidade = 0
        self.speedVento = 0

    
    #Set
    def call_api(self):
        link = f"https://api.openweathermap.org/data/2.5/weather?q={self.nome}&appid={chave}&lang=pt_br"
        requisicao = requests.get(link)
        dic = requisicao.json()
        
        self.descricao = dic['weather'][0]['description']
        self.temperatura = '{:.2f}'.format(dic['main']['temp'] - 273.15)
        self.sensacao = '{:.2f}'.format(dic['main']['feels_like']- 273.15)
        self.minima = '{:.2f}'.format(dic['main']['temp_min'] - 273.15)
        self.maxima = '{:.2f}'.format(dic['main']['temp_max'] - 273.15)
        self.pressao = dic['main']['pressure']
        self.umidade = dic['main']['humidity']
        self.speedVento = '{:.2f}'.format(dic['wind']['speed'] * 3.6)