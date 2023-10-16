# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.

viagemk = float(input("distancia da sua viagem em km: "))
if viagemk <= 200:
    print(f"o preço da sua passagem é: {0.50*viagemk}" )
else:
    print(f"o preço da sua passagem é: {0.45*viagemk}")

   