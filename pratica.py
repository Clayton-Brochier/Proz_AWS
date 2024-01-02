'''Problema: Desenvolva um programa que só deve aceitar números pares. Siga as seguintes instruções:

caso um número ímpar seja digitado, informe ao usuário que ele digitou um valor ímpar e peça novamente por um número par;

caso uma letra seja digitada, informe ao usuário que ele digitou um caractere inválido e peça novamente por um número par.'''



numeroCorreto = False
while(numeroCorreto == False):
    try:
        print("Insira um número par!")
        numero = int(input())

        if(numero % 2 == 0):
            numeroCorreto = True
            print("Você digitou um número par!")
        else:
            print("Você digitou um número ímpar.")

    except ValueError:
        print("Caractere inválido. Por favor, digite um número inteiro par.")
