# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.

distância = float(input("distância da viaguem:"))
print(f"A distância da sua viaguem {distância}km." )
if distância <= 200:
    print (f"preço de sua passagem será de R${distância * 0.50}")
else:
    print(f"o preço de sua passagem será de R${distância * 0.45}")
