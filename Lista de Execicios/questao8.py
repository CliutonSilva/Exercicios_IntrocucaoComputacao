numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
aux = 0

if numero1 > numero2:
  aux = numero1
  numero1 = numero2
  numero2 = aux
if numero1 > numero3:
  aux = numero1
  numero1 = numero3
  numero3 = aux
if numero2 > numero3:
  aux = numero2
  numero2 = numero3
  numero3 = aux

print(f"Os números em ordem crescente são: {numero1}, {numero2}, {numero3}")