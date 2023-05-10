
#frase=str(input('Digite uma frase: ')).strip()
#verifc_a=frase.upper().count('A')
#p_posicao=frase.find(verifc_a)+1
#u_posicao=frase.rfind(verifc_a)+1
#print('Analisando a frase inserida.. ')
#print(f'A frase inserida contém {verifc_a} letras "A/a"')
#print(f'A primeira letra "A/a" apareceu na posição: {p_posicao}')
#print(f'A ultima letra "A/a" apareceu na posição: {u_posicao}')



#codigo AI

frase=input("Insira uma informação: ")
contador = 0
p_letra = len(frase)
u_letra = -1

for i in range (len(frase)):
    if frase[i] == "A" or frase[i] == "a":
        contador += 1
        if i < p_letra:
            p_letra = i
        if i > u_letra:
            u_letra = i

print(f'Quantidade de vezes que a letra A/a aparece: {contador}')
if contador > 0:
    print(f'Posição em que a letra aparece a primeira vez: {p_letra}')
    print(f'Posição em que a letra aparece a última vez: {u_letra}')
else:
    print('Não existe a letra A/a na informação inserida!')