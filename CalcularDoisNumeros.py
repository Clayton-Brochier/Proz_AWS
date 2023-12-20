def calcula_dois_numeros():
  n1 = float(input("Digite o primeiro número: "))
  n2 = float(input("Digite o segundo número: "))
  operacao = 0

  print("Escolha a operação desejada: 1(soma), 2(subtração), 3(multiplicação) ou 4(divisão)")
  operacao = int(input("Digite a operação desejada: "))

  if operacao == 1:
    resultado = n1 + n2
  
  elif operacao == 2:
    resultado = n1 - n2

  elif operacao == 3:
    resultado = n1 * n2

  elif operacao == 4:
     if n2 != 0:
      resultado = n1 / n2
  
  else:
      resultado = 0
        

  resultado = print("Resultado: ", resultado)

calcula_dois_numeros()