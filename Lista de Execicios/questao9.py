# imc
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)

if imc < 18.5:
  print("Abaixo do peso")
elif imc < 25:
  print("Peso ideal (parabéns)")
elif imc < 30:
  print("Levemente acima do peso")
elif imc < 35:
  print("Obesidade grau I")
elif imc < 40:
  print("Obesidade grau II (severa)")
else:
  print("Obesidade grau III (mórbida)")