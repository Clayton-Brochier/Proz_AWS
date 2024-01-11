'''Copie o array apresentado embaixo no seu editor de código, e imprima no terminal: a quantidade de elementos que ele possui, 
o dado salvo no índice 2, o dado salvo no índice 9, e dado salvo no índice 14.
lista_musicos = [ 'Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal', 'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa'] '''

#Copie o array apresentado embaixo no seu editor de código
lista_musicos = [ 'Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal', 'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa']

#imprima no terminal: a quantidade de elementos que ele possui
print(len(lista_musicos))

#imprima no terminal: o dado salvo no índice 2
print(lista_musicos[2])

#imprima no terminal: o dado salvo no índice 9
print(lista_musicos[9])


#imprima no terminal: o dado salvo no índice 14
print(lista_musicos[14])


'''Uma nova loja de cosméticos abriu no seu bairro e pediram para você elaborar um sistema que imprime na tela na frente da loja os novos 
produtos que chegaram. O sistema da loja já tem um array com os produtos, você precisa apenas imprimir eles no terminal, um por um.

Como desafio opcional, tente imprimir cada produto com a frase "Temos [produto] à venda!" (ex. "Temos máscaras faciais à venda!"). 
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 
'''

#elaborar um sistema que imprime na tela na frente da loja os novos produtos que chegaram um por um.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
for i in range(len(lista_produtos)):
    print("Temos {} à venda!".format(lista_produtos[i]))

#https://colab.research.google.com/drive/1Oc-Bkhhunm4TnpUdxdBHZPXusTzaNaL-?usp=sharing
    

'''A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente! Dessa vez, eles precisam que você atualize o array 
de produtos. Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções. 
Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos. 
Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

Como desafio, adicione dois novos produtos da sua escolha à lista. '''

nova_lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

#trocar dois produtos: batons por rímel e loções por cremes hidratantes
nova_lista_produtos[1], nova_lista_produtos[4] = 'rímel', 'cremes hidratantes'

#delineadores, remova ele da lista de produtos.
nova_lista_produtos.pop()

#Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.
print(nova_lista_produtos)

#https://colab.research.google.com/drive/143ur2ao8Yfdr0MIN517i_TUhchyCD8xu?usp=sharing
#adicione dois novos produtos da sua escolha à lista.
nova_lista_produtos.append('Pomada de cabelo')
nova_lista_produtos.append('Cremes de mãos')

#Imprimir novos itens
for i in range(len(nova_lista_produtos)):
    print("Temos {} à venda!".format(nova_lista_produtos[i]))