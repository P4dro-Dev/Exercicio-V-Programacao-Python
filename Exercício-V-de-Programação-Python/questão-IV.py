# Uma ONG (Organização Não Governamental) oferece cursos gratuitos de programação de
# computadores, dança, música e culinária. Aproveitando a cozinha montada para os cursos de culinária,
# também vende pães integrais, doces e bolos para ajudar nas despesas. O diretor da ONG anunciou um
# incentivo para a venda da produção da cozinha: considerando que cada pão vale 1 ponto, cada doce vale
# 2 pontos e cada bolo vale 3 pontos, os colaboradores ganharão um prêmio dependendo da soma total dos
# pontos dos produtos vendidos durante a semana. Se a soma dos pontos de todos os produtos vendidos na
# semana for igual ou maior do que 150, cada colaborador recebe um bolo como prêmio; senão, cada
# colaborador recebe um doce como prêmio. Sabendo que você fez um curso de programação na ONG, o
# diretor pediu que você escreva um programa que, dados os números de pães, doces e bolos vendidos na
# semana, determine a quantidade de pontos e qual o prêmio merecido.
# Exemplo de entrada Exemplo de saída
# Pães: 10
# Doces: 20
# Bolos: 5
# Pontos: 65
# Prêmio: Doce
# Pães: 100
# Doces: 50
# Bolos: 50
# Pontos: 350
# Prêmio: Bolo
# Pães: 150
# Doces: 0
# Bolos: 0
# Pontos: 150
# Prêmio: Bolo

def calcular_pontos(paes, doces, bolos):
    pontos = paes * 1 + doces * 2 + bolos * 3
    if pontos >= 150:
        premio = "Bolo"
    else:
        premio = "Doce"
    return pontos, premio

# Exemplo de uso
paes = int(input("Pães: "))
doces = int(input("Doces: "))
bolos = int(input("Bolos: "))

pontos, premio = calcular_pontos(paes, doces, bolos)
print(f"Pontos: {pontos}")
print(f"Prêmio: {premio}")
