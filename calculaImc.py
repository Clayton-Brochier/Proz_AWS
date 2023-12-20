'''Problema: João precisa calcular seu Índice de Massa Corporal (IMC) para avaliar seu peso ideal. 
Sabendo que a fórmula para calcular o IMC é: peso ÷ altura², 
crie um programa que calcule e informe a classificação do IMC.'''

def calculaImc(peso, altura):
    media = peso / (altura * altura)
    return media

resultado = calculaImc(78, 1.83)

if resultado < 18.5:
    print("Baixo peso")
elif 18.5 <= resultado <= 24.9:
    print("Peso normal")
elif 25 <= resultado <= 29.9:
    print("Excesso de peso")
elif 30 <= resultado <= 34.9:
    print("Obesidade grau 1")
elif 35 <= resultado <= 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade morbida grau 3")