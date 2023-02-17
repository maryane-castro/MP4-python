from pytube import YouTube
import PySimpleGUI as sg
from time import sleep
lista = []

sg.theme('BlueMono')

tela = [
[sg.Text('Coloque um link de uma música')],
[sg.Input(key='link', do_not_clear=False)],
[sg.Text(key='saida')],
[sg.Button('Confirmar'), sg.Button('Sair')],
[sg.Button('Baixar todas as confirmadas')]
]


window = sg.Window('Pytube MP4', tela)

while True:
    event, values = window.read()
    if event == "Confirmar":
        if values['link'] != '':
            print('ok')
            window['saida'].update('Musica ok!' )
            lista.append(values['link'])
            print(lista)
        else:
            window['saida'].update('Vazio' )





    if event == 'Baixar todas as confirmadas':
        print('baixar')
        lista.append(values['link'])
        
        quant = 0
        while quant != len(lista):
            audio = YouTube(lista[quant])
            audio = audio.streams.get_audio_only()
            audio.download(output_path='C:\\Users\\kookp\\OneDrive\\Documentos\\vscode\\testeM\\musicas')
            print(lista[quant])
            quant += 1
         



    if event == sg.WINDOW_CLOSED or event == 'Sair': 
            break  

window.close()










'''lista = []

quant = int(input('Quantas musicas quer baixar? '))
while quant != 0:
    link = input(f'Falta {quant} musicas para você colocar o link: ')
    lista.append(link)
    quant -= 1



while quant != len(lista):
    audio = YouTube(lista[quant])
    audio = audio.streams.get_audio_only()
    audio.download(output_path='/home/aluno/Documentos/GitHub/testeM/musicas')
    print(lista[quant])
    quant += 1'''