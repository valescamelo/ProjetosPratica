q_km=float(input("Quantidade de km percorridos? "))
q_dias=float(input("Quantidade de dias que foram passados com o carro? "))
v_km = q_km * 0.15
v_dias = q_dias * 60
valor_total =  v_km + v_dias
print(f'O valor total a ser pago é de: {valor_total} R$')