bebidaFavorita = "coca-cola"
valorBebida = 8.99
alcoolica = False

print(bebidaFavorita)
print(type(bebidaFavorita))

print(valorBebida)
print(type(valorBebida))

print(alcoolica)
print(type(alcoolica))

print("Minha bebida favorita é:", bebidaFavorita, "e o valor é R$ " , valorBebida)

if alcoolica:
    print("Esta bebida é alcoólica.")
else:
    print("Esta bebida não é alcoólica.")
    
    
almoco_favorito = "churrasco"
preco = 69.90
orcamento = 50.00
troco = orcamento - preco
mensagem = "Meu almoço favorito é " + almoco_favorito + " e custa R$ " + str(preco)

print(mensagem)

if(preco < orcamento):
  print("Hoje tem churrasco e sobrou dinheiro!")
elif(preco == orcamento):
  print("Você estorou seu orçamento")
else:
  print("Você não tem o valor suficiente para esse almoço. Arrume uma vaga na TI!")