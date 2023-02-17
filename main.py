from cidade import Cidade
from tkinter import *

def main():
    nome = entrada.get()
    c1 = Cidade(nome)
    try:
        c1.call_api()

        texto = f'''
        Descrição: {c1.descricao}
        Umidade: {c1.umidade}
        Temperatura: {c1.temperatura} C
        Sensação térmica: {c1.sensacao} C
        Temperatura Mínima: {c1.minima} C
        Temperatura Máxima: {c1.maxima} C
        Pressão Atmosférica: {c1.pressao}"Hg    
        Velocidade do vento: {c1.speedVento} KM/h'''
        texto_condicoes['text'] = texto
    except:
        texto_condicoes['text'] = 'Cidade não encontrada :('



interface = Tk()
interface.title('Weather App')
interface.geometry('500x400')
interface['bg'] = "#5C7394"
msg = Label(interface, text='Condições meteorológicas atualizadas', font='Times 15', bg='#5C7394')
msg.grid(column=0, row=0, padx=15, pady=15)

txt = Label(interface, text='Digite o nome da cidade ', font= 'Arial 9 italic', bg='#5C7394')
txt.grid(column=0, row=1, padx=10, pady=10)
entrada = Entry(interface, width=27)
entrada.grid(column=0, row=3, padx=10, pady=10)


botao = Button(interface, text='Obter',command=main, bg='#447BC7')
botao.grid(column=1, row=3, padx=15, pady=15)

    
texto_condicoes = Label(interface, text='', bg='#5C7394', font='Arial 12')
texto_condicoes.grid(column=0, row=4, padx=15, pady=15)

interface.mainloop()
