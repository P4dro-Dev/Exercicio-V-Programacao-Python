# Um estacionamento possui vagas para carros e motos. Para controlar a entrada de veículos, é necessário
# criar um programa que receba o número de vagas disponíveis e verifique se há vagas disponíveis.
# • Se houver vaga disponível, o programa deve reduzir em 1 o número de vagas disponíveis e
# exibir a mensagem: “Entrada permitida! Vagas disponíveis restantes: XX”, onde XX representa
# a quantidade de vagas disponíveis.
# • Caso contrário, exibir uma mensagem de "Sem vagas disponíveis!".
# Exemplo de entrada Exemplo de saída
# Vagas: 10 Entrada permitida!
# Vagas disponíveis restantes: 9
# Vagas: 1 Entrada permitida!
# Vagas disponíveis restantes: 0
# Vagas: 0 Sem vagas disponíveis!

def verificar_vagas(vagas):
    if vagas > 0:
        vagas -= 1
        print(f"Entrada permitida! Vagas disponíveis restantes: {vagas}")
    else:
        print("Sem vagas disponíveis!")

# Exemplo de uso
vagas = int(input("Vagas: "))
verificar_vagas(vagas)
