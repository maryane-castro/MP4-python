from pytube import YouTube


lista = []
def menu():
    
    quant = int(input('Quantas musicas quer baixar? '))
    while quant != 0:
        link = input(f'Falta {quant} musicas para você colocar o link: ')
        lista.append(link)
        quant -= 1

    

    while quant != len(lista):
        audio = YouTube(lista[quant])
        audio = audio.streams.get_audio_only()
        audio.download(output_path='C:\\Users\\kookp\\OneDrive\\Documentos\\vscode\\testeM\\musicas')
        print(lista[quant])
        quant += 1

menu()

'''
audio = YouTube(lista[0])
audio = audio.streams.get_audio_only()
audio.download()'''