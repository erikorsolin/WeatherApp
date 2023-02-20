from cidade import Cidade
import tkinter
import customtkinter
from PIL import ImageTk, Image



def main(box):
    nome = entrada.get()
    c1 = Cidade(nome)
    try:
        c1.call_api()
        dados = f'''
        Descrição: {c1.descricao}
        Umidade: {c1.umidade}
        Temperatura: {c1.temperatura} C
        Sensação térmica: {c1.sensacao} C
        Temperatura Mínima: {c1.minima} C
        Temperatura Máxima: {c1.maxima} C
        Pressão Atmosférica: {c1.pressao}"Hg  
        Velocidade do vento: {c1.speedVento} KM/h'''
    except: 
        dados = 'Cidade não encontrada'

    box.configure(text=dados)    


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


interface = customtkinter.CTk()
interface.title('Weather App')
interface.geometry('600x440')


img1 = ImageTk.PhotoImage(Image.open('pingos.png'))
l = customtkinter.CTkLabel(master=interface, image=img1)
l.pack()



frame = customtkinter.CTkFrame(master=interface, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

msg = customtkinter.CTkLabel(master=frame, text='Condições meteorológicas atualizadas', text_color="#669EE8", font=customtkinter.CTkFont(family='Arial', size=13))
msg.place(x=49, y=6)

l2=customtkinter.CTkLabel(master=frame, text='Digite o nome da cidade', font=customtkinter.CTkFont(family='Century Gothic', size=20) )
l2.place(x=40, y=45)

entrada=customtkinter.CTkEntry(master=frame, width=220, placeholder_text= "cidade")
entrada.place(x=45, y=110)

botao=customtkinter.CTkButton(master=frame, width=220, text='Obter', corner_radius=6, command=lambda: main(l3))
botao.place(x=45, y=155)

l3 = customtkinter.CTkLabel(
    master=frame, 
    text='ola mundo',
    font=customtkinter.CTkFont(family='Arial', size=13)
    )
l3.place(x=15, y= 190)


interface.mainloop()

