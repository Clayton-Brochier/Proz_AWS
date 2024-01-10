#Faça um programa que leia um número inteiro e mostre na tela o seus sucessor e antecessor.

numero = int(input("Digite um número inteiro:"))
antecessor = numero - 1
sucessor = numero + 1
print("O antecessor de {}, é {} e o sucessor é {}.".format(numero, antecessor, sucessor))


#Crie um programa que leia um número e mostre seu dobro, triplo e raiz quadrada

n1 = int(input("Digite um número:"))
dobro = n1 * 2
triplo = n1 * 3
raiz2 = n1 ** (1/2)
print("O dobro de {} é: {}, seu triplo é: {} e sua raiz quadra é {}.".format(n1, dobro, triplo, raiz2))

#Crie um programa que leia duas notas de um aluno, calcule e mostre sua média.

nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
media = (nota1 + nota2) / 2
print("A média das notas é {}.".format(media))

#Escreva um progra que leia um valor em metros e o exiba convertido em centímetros e milimetros.

medida = float(input("Digite um valor em metros:"))
convertido_cm = medida * 100
convertido_mm = medida * 1000

print("{} metros convertido para centímetros é {} e convertido para milímetros é {}.".format(medida, convertido_cm, convertido_mm))

#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
nRecebido = int(input("Digite um número inteiro: "))

print("A tabuada de {}:".format(nRecebido))

for i in range (1, 11):#range acrescenta o incremento, basta informar vInicial e vFinal.
    resultado = nRecebido * i
    print("{} x {} = {}.".format(nRecebido, i, resultado))