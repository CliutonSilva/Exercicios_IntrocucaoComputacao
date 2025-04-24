salario_minino = 1293.20

salario_usuario = float(input("Digite o salário: "))

qtd_salarios = salario_usuario / salario_minino 

if salario_usuario <= salario_minino:
    print("Salário abaixo do mínimo.")
else:
    print(f"Você recebe aproximadamente: {qtd_salarios:.0f} salarios mínimos.")