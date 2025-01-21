# Um banco deseja criar um programa para calcular a taxa de juros sobre empréstimos com base no valor
# solicitado e no prazo de pagamento (quantidade de meses):
# • Empréstimos até R$ 5.000,00: taxa de 5%.
# • Empréstimos acima de R$ 5.000,00: taxa de 2%.
# O programa deve receber o valor do empréstimo, o número de meses e calcular o valor total a ser pago
# com base na taxa correspondente. O programa deve exibir o valor total a ser pago, a quantidade de
# meses e o valor da parcela.
# Exemplo de entrada Exemplo de saída
# Empréstimo: 1000.00
# Prazo: 10
# Valor total a ser pago: R$ 1050.00
# Quantidade de meses: 10
# Valor da parcela: R$ 105.00
# Empréstimo: 9000.00
# Prazo: 12
# Valor total a ser pago: R$ 9180.00
# Quantidade de meses: 12
# Valor da parcela: R$ 765.00

def calcular_emprestimo(valor, meses):
    if valor <= 5000:
        taxa = 0.05
    else:
        taxa = 0.02

    valor_total = valor * (1 + taxa)
    valor_parcela = valor_total / meses

    print(f"Valor total a ser pago: R$ {valor_total:.2f}")
    print(f"Quantidade de meses: {meses}")
    print(f"Valor da parcela: R$ {valor_parcela:.2f}")

# Exemplo de uso
valor = float(input("Empréstimo: "))
meses = int(input("Prazo (meses): "))
calcular_emprestimo(valor, meses)
