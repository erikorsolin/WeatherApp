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
        chave = "abdcb2f05a1704c2ef9a456e893a3f41"
        link = f"https://api.openweathermap.org/data/2.5/weather?q={self.nome}&appid={chave}&lang=pt_br"
        requisicao = requests.get(link)
        dic = requisicao.json()

        self.descricao = dic['weather'][0]['description']
        self.temperatura = dic['main']['temp'] - 273.15
        self.sensacao = dic['main']['feels_like']
        self.minima = dic['main']['temp_min'] - 273.15
        self.maxima = dic['main']['temp_max'] - 273.15
        self.pressao = dic['main']['pressure']
        self.umidade = dic['main']['humidity']
        self.speedVento = dic['wind']['speed'] * 3.6


    
    
