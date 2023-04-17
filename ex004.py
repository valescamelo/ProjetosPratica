#Tipos primitivos

var=input("Insira uma informação: ")
print("O tipo primitivo inserido: " , type(var)) #type refere-se a qual tipo de informação o usuário inseriu
print("Contém espaços? " , var.isspace()) #isspace verifica se a variavel contém espaços
print("Contém números?" , var.isnumeric()) #verifica é um número
print("É alfabeto?" , var.isalpha()) #verifica se é alfabeto
print("É alfanumérico?" ,  var.isalnum()) #verifica se existe numeros e letras
print("Está em maiuscula?" , var.isupper()) #verifica se esta em maiuscula 
print("Está em minuscula?" , var.islower()) #verifica se esta em minuscula
print("Está capitalizado?" , var.istitle()) #verifica se existe maiuscula e minuscula