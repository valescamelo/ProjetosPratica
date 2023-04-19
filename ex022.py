
nome=str(input('Informe seu nome completo: ')).strip()
print('Verificando seu nome...')
print('Seu nome em  letras maiúsculas: ' , (nome.upper()))
print('Seu nome em letras minúsculas: ', (nome.lower()))
print('Quantidade de letras que seu nome tem ao todo: ' , (len(nome)) - nome.count(' '))
separa=nome.split() #separando os nome e incluindo em uma lista 
#no final vai imprimir o primeiro nome que esta na lista no indice 0 e ler a quantidade de letras que tem
print('Quantidade de letras que seu primeiro nome tem: ', (separa[0]) , len(separa[0]))
