"""x = 2
y = 6

soma = x + y

print("Olá mundo")
print(y == x)
print(soma >  y and x < y)
print(soma >=  y or x < y)
print(soma >=  y and x > y)"""

"""----------------ESTRUTURAS CONDICIONAIS---------------"""
"""x = 1
y = 1

if x == y:
    print("números iguais")
elif y > x:
    print("y é maior que x")
else: 
    print("números diferentes")"""

"""-----------------LAÇOS DE REPETIÇÕES-------------------"""

#COMANDO WHILE
"""x = 1

while x < 10:
    print(x)
    x += 1"""

#COMANDO FOR
"""lista1 = [1,2,3,4,5]
lista2 = ["Olá", "mundo", "!"]
lista3 = [0, "ola", "biscoito", "bolacha", 0.95, True]

for i in lista3:
    print(i)"""

#COMANDO FOR COM RANGE
"""for i in range(10, 20, 2):
    print(i)"""

"""----------------------OBJECTS-------------------------"""
"""class Endereco:
    cep = '73751-590'
    logradouro = 'Santa Maria'
    bairro = 'Setor Norte'
    complemento = 'Residencial Paris'
    numero = '32'

class Pessoa:
    nome = 'Rafael'
    cpf = '03523627311'
    endereco = Endereco

print(Pessoa.endereco.cep)"""

"""--------------------STRINGS----------------------------"""
"""nome = "Rafael"
sobrenome = "Neto"

concatenar = nome + " " + sobrenome + "\n"

print(concatenar)

tamanho = len(concatenar)
print(tamanho)

print(concatenar[3])
print(concatenar[6])
print(concatenar[8])

print(concatenar[3:8])

print(concatenar.lower())
print(concatenar.upper())
print(concatenar.strip())


minha_string = "O rato roeu a roupa do rei de Roma"

minha_string_com_split = minha_string.split(" ")
print(minha_string_com_split)

find_string = minha_string.find("rei")
print(find_string)
print(minha_string[find_string:])

minha_string = minha_string.replace("rei", "rainha")
print(minha_string)"""

"""---------------------------FUNÇÕES--------------------"""
"""def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

resultado_soma = soma(9, 3)
print(resultado_soma)

resultado_multiplicacao = multiplicacao(4, 2)
print(resultado_multiplicacao)

print(soma(resultado_soma, resultado_multiplicacao))
print(multiplicacao(resultado_soma, resultado_multiplicacao))"""

"""----------------------MANIPULAÇÃO DE ARQUIVOS------------------"""

"""arquivo = open("arquivo.txt")

linhas = arquivo.readlines()
print(linhas)

for linha in linhas:
    print(linha)

texto_completo = arquivo.read()
print(texto_completo)

criar_arquivo = open("arquivo_criado.txt", "w")

criar_arquivo.write("Meu primeiro arquivo criado com python")
criar_arquivo.close()

criar_arquivo_sem_apagar_dados = open("arquivo_sem_alteração.txt", "a")

criar_arquivo_sem_apagar_dados.write("------- Arquivo não deve ser modificado -------\n")
criar_arquivo_sem_apagar_dados.write("* Primeiro dado inserido")"""

"""------------------------LISTAS------------------------"""
"""lista_strings = ["abacaxi", "melancia", "abacate"]
lista_numeros = [1,2,3,4,5,6]
lista_mista = [True, "tijolo", 6.35, False]

print(lista_mista[2])

for item in lista_strings:
    print(item) 

tamanho_lista = len(lista_strings)
print("Tamanho da lista: "+ str(tamanho_lista))

lista_strings.append("limão")
print(lista_strings)

if 5 in lista_numeros:
    print("5 está na lista")

del lista_strings[3:]
print(lista_strings)"""

"""------------------------LISTAS COM FUNÇÕES------------------------"""
"""lista = [56,69,85,2,58,47,65,32,12,51,74]

lista.sort(reverse=True)

print(lista)

lista_strings = ["bola", "abacate", "abacaxi", "maracujá", "melancia", "caju", "queijo"]

lista_strings.sort(reverse=True)
print(lista_strings)"""

"""------------------------DICIONÁRIOS------------------------"""
"""dicionario = {"A": "ameixa", "B": "bola", "C": "cachorro"}

print(dicionario["A"]);

for chave in dicionario:
    print(chave + "-" + dicionario[chave])

for i in dicionario.items():
    print(i)

for i in dicionario.keys():
    print(i)"""

"""------------------------NÚMEROS ALEATÓRIOS------------------------"""
"""import random

lista = [6,45,9]
numero = random.randint(0,10)
escolha = random.choice(lista)
print(numero)
print(escolha)"""

"""------------------------TRATAMENTO DE EXCEÇÕES------------------------"""
"""a = 2
b = 0

try:
    print(a/b)
except:
    print("não é permitida divisão por zero.")"""

"""------------------------LIST COMPREHENSION------------------------"""
"""x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)

#OU
print("Exemplos de list comprehension:")
w = [i**2 for i in x]
z = [i for i in x if i%2==1]

print(w)
print(z)"""

"""------------------------FUNÇÃO ENUMERATE------------------------"""
"""lista = ["abacate", "bola", "cachorro"]

print("Sem função enumerate:")
for i in range(len(lista)):
    print(i, lista[i])

print("\nCom função enumerate:")
for i, nome in enumerate(lista):
    print(i, nome)"""

"""------------------------FUNÇÃO FILTER------------------------"""
"""def pares(i):
    if i % 2 == 0:
        return i

lista = [1,2,3,4,5,6,7,8,9,10]

lista_pares = filter(pares, lista)
print(list(lista_pares))"""

"""------------------------FUNÇÃO MAP------------------------"""
"""def dobro(x):
    return x * 2

valor = [1,2,3,4]

valor_dobrado = map(dobro, valor)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)"""

"""------------------------FUNÇÃO ZIP------------------------"""
"""lista_numerica = [1,2,3,4,5]
lista_strings = ["abacate", "arroz", "cenoura", "dinheiro"]
lista_precos = ["R$ 5,90", "R$ 9,99", "R$ 3,65", "Não tem preço", "Não tem referência"]

for numero, nome, valor in zip(lista_numerica, lista_strings, lista_precos):
print(numero, nome, valor)"""

