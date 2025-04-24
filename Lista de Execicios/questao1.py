a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

soma = a + b

if soma > c:
  print(f"A soma de A: {a} + B: {b} = {soma} é maior que o valor de C: {c}")
else:
  print(f"A soma de A: {a} + B: {b} = {soma} não é maior que o valor de C: {c}")