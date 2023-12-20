'''Instruções:

#Desenvolva um algoritmo que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; 
E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

Desenvolvimento
Definir uma função de verificação'''
def verificaCategoria(rodas, peso, pessoas):    
    if rodas == 2 or rodas == 3:
        return 'Categoria A'
    elif rodas == 4 and pessoas <= 8 and peso <= 3500:
        return 'Categoria B'
    elif rodas == 4 and 3500 < peso <= 6000:
        return 'Categoria C'
    elif rodas >= 4 and pessoas > 8:
        return 'Categoria D'
    elif rodas >= 4 and peso > 6000:
        return 'Categoria E'
    else:
        return 'Categoria não determinada'
    
# Entrada de dados
qtdeRodas = int(input("Informe a quantidade de rodas do veículo: "))
pesoBruto = float(input("Informe o peso do veículo em quilogramas (kg):"))
qtdePessoas = int(input("Informe a quantidade de pessoas no veículo: "))

# Chamar a função
categoria = verificaCategoria(qtdeRodas, pesoBruto, qtdePessoas)

# Saída de dados
print(f"A categoria de habilitação para o veículo informado é: {categoria}")
