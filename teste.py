'''a = 1
b = 'uir'


b1 = b.isnumeric()

if b1 == True:
    print('vdd')
if b1 == False:
    print('fal')'''

import pathlib

diretorio = pathlib.Path('D:\\')
arquivos = diretorio.glob('equipe6')

for arquivo in arquivos:
    print(arquivo)