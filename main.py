from pytube import YouTube


lista = []
def menu():
    
    while True:
        quant = int(input('Quantas musicas quer baixar? '))
        if quant <= 0:
            continue
        else:
            break

    local = input('Digite o local da pasta para baixar!')

    while local == '':
        local = input('É obrigatório digitar o local da pasta para baixar! ')

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