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