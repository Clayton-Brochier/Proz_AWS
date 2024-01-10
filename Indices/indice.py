#Se usarmos a função print() para “imprimir” um vetor, veremos todos os items da lista.

lista_frutas = ['maça', 'banana', 'pera']
print(lista_frutas) #saída: ['maça', 'banana', 'pera']

#Cada item do vetor tem um índice. O índice, nada mais é do que um valor inteiro que representa cada um dos valores do array, e que começa sempre do número 0 e vai aumentando de 1 em 1.
#Pense nos arrays como uma lista de pessoas esperando a ser atendidos no banco. Não sabemos o nome de cada uma delas, mas sabemos que todas elas tem uma senha diferente. 
#Para chamar a primeira pessoa da lista, basta escrever o nome do vetor, seguido por um par de colchetes, e dentro dos colchetes escrever o índice do item que queremos acessar.
print(lista_frutas[1]) #Saída: banana

# acessar um item do array usando o método descrito não elimina o item do array, ou altera ele de forma alguma. 
#O único que estamos fazendo é “chamar”, ou visualizar, o respectivo item.
frutas_preferidas = lista_frutas[0]
print(frutas_preferidas) #Saída: maça

#Função len()

#Os vetores são muito úteis para agrupas listas de itens, porém, em sistemas maiores e mais complexos, eles podem chegar a ter um número imenso de itens. 
#Em casos como esse, pode ser muito difícil saber algo tão simples como: quantos elementos esse array possui?

quantidade_frutas = len(lista_frutas)
print(quantidade_frutas)#Saída: 3

#É possível também passar a função len() como argumento da função print(), sem guardar ela previamente numa variável:
print(len(lista_frutas))#Saída 3

'''-------------------------------------------------------------------------------------------------------------------------------------'''

#Para percorrer um array com 10, 20 ou 100 itens.Utilizamos estruturas de repetição! Para demonstrar uma versão mais simples do exemplo anterior, usaremos um for loop:
#Estrutura de repetição
for i in range(3):
    print(lista_frutas[i])#Saída: maça, banana, pera

#a função range pode receber até três argumentos que representam: o valor inicial do contador, a condição de parada, o incremento do contador.
#Se, ao invés de passarmos os três valores, passarmos apenas um valor como argumento, ele representará a condição de parada.
#No exemplo acima, a condição de parada é 3, em outras palavras, que o contador seja menor que 3 (i < 3).
#Como não passamos mais argumentos, a função range() atribui um valor padrão para o valor inicial e o incremento do contador. Estes valores por padrão são 0 e +1, respectivamente.
    '''Dessa forma, ao usar a função range(3) os elementos para nossa estrutura de repetição ficam assim:

        - Valor inicial do contador = 0
        - Condição de parada = contador < 3
        - Incremento do contador = 1              '''
    
#quando não sabemos quantos indices há no array e precisamos da condição de parada, podemos utilizar a função range() juntamente com len().
lista_num = [2, 45, 65, 78, 126, 987, 457, 345, 679, 107, 2345, 452, 3, 34, 560]

for i in range(len(lista_num)):
    print(lista_num[i])
    



