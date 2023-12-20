'''Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o 
usuário escolha a opção de sair. 
No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. '''

'''Mostrar lista de operações'''
def mostra_menu():
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

'''Criar funçao de calculo'''
def calcula_operacoes():
    op = -1  # Iniciando operador com um numero diferente dos propostos no menu.

    while op != 0: # while(enquanto) o operador for diferente de 0, a função chamará a função menu num loop.
        mostra_menu()
        op = int(input("Digite a operação que deseja realizar: "))

        if op == 1:
            n1 = float(input("Insira o primeiro número: "))
            n2 = float(input("Insira o segundo número: "))
            soma = n1 + n2
            print("A soma de", n1, "e", n2, "foi de:", soma)
        elif op == 2:
            n1 = float(input("Informe o primeiro valor: "))
            n2 = float(input("Informe o segundo valor: "))
            subtracao = n1 - n2
            print("A subtração de", n1, "-", n2, "é igual a:", subtracao)
        elif op == 3:
            n1 = float(input("Informe o primeiro valor: "))
            n2 = float(input("Informe o segundo valor: "))
            multiplicacao = n1 * n2
            print("A multiplicação de", n1, "e", n2, "foi de:", multiplicacao)
        elif op == 4:
            n1 = float(input("Informe o primeiro valor: "))
            n2 = float(input("Informe o segundo valor: "))
            if n2 == 0:
                print("Não é possível dividir por zero.")
            else:
                divisao = n1 / n2
                print("A divisão de", n1, "/", n2, "é igual a:", divisao)
        elif op == 0:
            print("Saindo do programa")
        else:
            print("Opção inválida")

# Chamar a função
calcula_operacoes()
