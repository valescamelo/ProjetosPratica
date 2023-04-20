cidade=str(input('Informe o nome de uma cidade brasileira: ')).strip() #elimina os espaços
primeiro_item=cidade.split() #divide a string 
item_extra=primeiro_item[0]
print('Analisando nome da cidade..')
print(f'Nome: {cidade}')
if (item_extra.upper() =='SANTO'):
    print('O primeiro nome da cidade brasileira inserida contém a palavra Santo!')
else:
    print('O primeiro nome da cidade brasileira inserida NÃO contém a palavra Santo!')
