#==========================================================================================
# Estruturas de repetição
# Loops --> Responsáveis por executar blocos de códigos(ações) repetidas vezes até que a condição seja concluída.

#==========================================================================================
#2 Tipos de Estruturas 
# While
# For
#==========================================================================================
# While

pessoas = 1

# Enquanto o valor de 'pessoas' for menor ou igual a 38, o bloco de código será executado.

while pessoas < 38:
    print(f'A querida instrutora fernanda deve {pessoas} pessoas')
    pessoas+=1

# Obs: Cuidado com loops 'while' que não alteram a condição de parada, pois podem gerar loops infinitos.

# pesquisa = 'Air Friyer'

# while pesquisa == 'Air Friyer':
#     print(f'Este bloco seria executado infinitamente!')

# -----------------------------------------------------------------------------------------


# For --> Ele é mais utilizado para percorrer informações e executar ações em cima dessas informações

# for fofoqueiro in local:
#     print(f'Fofoqueiro percorre a informação')

lista_pessoas_fernanda_deve = ["Emanuelle", "Karyne", "Leonardos", "Jakeline" "Danilo", "Yuri", "Graziele"]

for item in lista_pessoas_fernanda_deve:
    print(item)

airfrier = ['Philco', 'Polishop', 'Samsung', 'Mondial', 'Wallita', 'Brastemp', 'Cadense']

for item in airfrier:
    print(item)

#------------------------------------------------------------------------------------------
# Exemplo utilizando o range
# range --> forma de utilizar pedindo começando de um número até quanto

# for numero in range(10):  --> range(10) gera números de 0 até 9
#    print(numero)
for item in range(5):
    print(item)

# for numero in range(1,11,2) inicio: 1, final: 10, pular: 2
for item in range(0,11,2):
    print(item)

# =========================================================================================
#Manipulação de Strings
# =========================================================================================

# 1) upper -> converter essas informações em Maiúsculo
# 2) lower -> converter essas informações em Minúsculo

usuaria = "fernanda pix"

print(usuaria.upper())
print(usuaria.lower())

#------------------------------------------------------------------------------------------
# 3) replace -> trocar uma informação

print(usuaria.replace("pix", "Correa").upper())

#------------------------------------------------------------------------------------------
# 4) capitalize -> converte para maiusculo a primeira letra
print(usuaria.capitalize().replace("pix", ""))

#------------------------------------------------------------------------------------------
# 5) join -> Usado para unir os elementos de uma lista 
usuario = ["Xavier", "do X-men"]
print(" ".join(usuario))

#------------------------------------------------------------------------------------------
# 6) split --> dividir uma string em partes transformando em uma lista

# print('Manipulação de String (exemplo com uma lista de strings)')
nomes = 'Alice Bob Charlie David'

print('Lista de nomes: ', nomes.split())

# separador = Uma caracter que será usado para se dividir a string
# maxsplit = O número máximo de divisões que devem ser feitas

texto = 'nome,idade,cidade,país'

print(texto.split(',',2))

#------------------------------------------------------------------------------------------

# Se quisermos aplicar um método de string a cada elemento da lista, podemos iterar sobre ela:

print('Elementos da lista em lowercase: ')
nome = "Gabrielle"

for elemento in nome:
    print(elemento.upper())


