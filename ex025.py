nome=str(input('Informe seu nome completo: ')).strip()
print('Analisando o nome inserido ')
if 'SILVA' in nome.upper():
    print('O seu nome contém a palavra Silva.')
else:
    print('O nome completo inserido NÃO contém a palavra Silva.')