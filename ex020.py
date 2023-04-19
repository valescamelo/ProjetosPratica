from random import sample

a_1=str(input('Primeiro aluno: '))
a_2=str(input('Segundo aluno: '))
a_3=str(input('Terceiro aluno: '))
a_4=str(input('Quarto aluno: '))
alunos=([a_1, a_2, a_3, a_4])
result=sample(alunos, k=4)
print(f'Os alunos informados são: {alunos}')
print(f'Resultado: {result}')
