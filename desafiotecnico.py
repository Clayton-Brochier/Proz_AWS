'''Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro 
e continuará perguntando até que um valor correto seja preenchido.'''

# Iniciando o desenvolvimento

nome = input("Insira seu nome: ")

while True:
    try:
        anoNascimento = int(input("Insira a data de nascimento no formato xxxx: "))

        if 1922 <= anoNascimento <= 2021:
            idade = 2023 - anoNascimento
            print(nome + ", você tem " + str(idade) + " anos.")
            break 
        else:
            print("Você digitou uma data anterior a 1922 ou superior a 2021, ou seja, fora do intervalo desejado.")
    except ValueError:
        print("Caractere inválido. Por favor, digite uma data válida entre 1922 e 2021.")

# Correção Proz:
        
print("Digite seu nome:")
nome = input()

executar = True

while(executar == True):
    print("Digite seu ano de nascimento:")
    try:
        ano = int(input())
        if(ano < 1922) or (ano > 2021):
            print("O ano precisa ser entre 1922 e 2021")
        else:
            idade = 2023 - ano
            print("O usuário ", nome, "completou ou completará ", idade, "anos em 2023.")
            executar = False
    except:
        print("Entrada inválida. Digite uma data:")