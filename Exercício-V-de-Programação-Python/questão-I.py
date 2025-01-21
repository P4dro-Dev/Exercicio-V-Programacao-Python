# 1. Crie um programa que receba a idade de uma pessoa e informe se ela é:
# • "Obrigada a votar", se a idade for entre 18 e 70 anos.
# • "Voto opcional", caso contrário.
# Exemplo de entrada Exemplo de saída
# Idade: 18 Obrigada a votar
# Idade: 80 Voto opcional

def verificar_voto(idade):
    if 18 <= idade <= 70:
        return "Obrigada a votar"
    else:
        return "Voto opcional"

# Exemplo de uso
idade = int(input("Idade: "))
print(verificar_voto(idade))
