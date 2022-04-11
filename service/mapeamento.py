from dados import produtos, pessoas, lista


# Apenas passando os preços da lista com o map (pode ser feito com list comprehension também)
precos = map(lambda p: p['preco'], produtos)

print('precos antigos:')
for preco in precos:
    print(preco)


# Criando função para aumentar preço e utilizando no map
def aumenta_preco(p):
    return round(p['preco'] * 1.05, 2)

produtos_novos = map(aumenta_preco, produtos)

print('precos novos:')
for produto in produtos_novos:
    print(produto)

# Criando função para aumentar idade adicionando uma nova informação ao dicionário de pessoas
def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

nomes = map(aumenta_idade, pessoas)
print('pessoas:')

for pessoa in nomes:
    print(pessoa)