from math import hypot

cat_oposto=float(input('Informe o VR do cateto oposto: '))
cat_adj=float(input('Informe o VR do cateto adjacente: '))
hip=hypot(cat_oposto , cat_adj) #o quadrado da hipotenusa é igual à soma dos quadrados dos catetos
print(f'O valor da Hipotenusa é igual a: {hip}')