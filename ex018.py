from math import radians, sin, cos, tan

angulo=float(input('Informe o ângulo que deseja: '))
seno=sin(radians(angulo))
con=cos(radians(angulo))
tang=tan(radians(angulo))

print(f'O ângulo informado foi: {angulo} \n'
f'O Seno do ângulo é: {seno} \n'
f'O Conseno do ângulo é: {con} \n'
f'A Tangente do ângulo é: {tang}')
