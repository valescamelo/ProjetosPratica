import random

numero_maquina=random.randint(0, 5)
numero_usuario=int(input('Digite um número de 0 a 5: '))
if numero_maquina == numero_usuario:
    print('Número informado correto.')
else:
    print(f'Erro! O número informado está incorreto. Número da máquina: {numero_maquina}')