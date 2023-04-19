from random import choices

a_um=str(input('Informe o nome do primeiro aluno: '))
a_dois=str(input('Informe o nome do segundo aluno: '))
a_tres=str(input('Informe o nome do terceiro aluno: '))
a_quarto=str(input('Informe o nome do quarto aluno: '))
lista = [a_um, a_dois, a_tres, a_quarto]
result=choices(lista)
print(f'O aluno sorteado para realizar a limpeza do quadro foi: {result}')