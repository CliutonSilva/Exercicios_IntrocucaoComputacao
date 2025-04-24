valor_produto = float(input("Digite o valor do produto: "))

print("""Digite a forma de pagamento
        1 - À vista em dinheiro ou pix (15% de desconto)
        2 - À vista no cartão de credito (10% de desconto)
        3 - Em até 2x no cartão de credito (sem desconto)
        4 - Em 3x ou mais no cartão de credito (10% de juros)""")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
  valor_final = valor_produto * 0.85
  print(f"Valor a ser pago: R$ {valor_final:.2f}")
elif opcao == 2:
  valor_final = valor_produto * 0.90
  print(f"Valor a ser pago: R$ {valor_final:.2f}")
elif opcao == 3:
  valor_final = valor_produto
  print(f"Valor a ser pago: R$ {valor_final:.2f}")
elif opcao == 4:
  parcelas = int(input("Digite o número de parcelas: "))
  valor_final = valor_produto * 1.10
  valor_parcela = valor_final / parcelas
  print(f"Valor a ser pago: R$ {valor_final:.2f}")
  print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
else:
  print("Opção inválida")