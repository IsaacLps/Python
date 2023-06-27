# Lista contendo 3 possiveis filmes para cada gênero.
from tracemalloc import stop


filmesdeacao = ["Mad Max", "John Wick", "Resgate do soldado Ryan"]
filmesdeaventura = ["Senhor do Anéis", "Harry Potter: E o Prisineiro de Azcaban", "Piratas do Caribe"]
filmesdesuspense = ['Fragmentado', 'A Caça', 'Ilha do Medo']

# Variável para escolha de gênero
genero = input("Dos generos a seguir escolha um: 'Ação', 'Aventura' ou 'suspense' " )

# Variável faiza etária
faixaetaria = input("Voce é maior de idade? ")

# Variável para chegar se é uma pessoa tolerante
tolerancia = input("Voce se considera uma pessoa tolerante a cenas pesadas? ")

# Condicionais para o genero de Ação
if genero == "açao" and faixaetaria == "sim" and tolerancia == "sim":
    print("Recomendação: ", filmesdeacao[1])
elif genero == "açao" and faixaetaria == "sim" and tolerancia == "nao":
    print("Recomendação: ", filmesdeacao[0])
elif genero == "açao" and faixaetaria == "nao" and tolerancia == "nao":
    print("Recomendação: ", filmesdeacao[2])
elif genero == "açao" and faixaetaria == "nao" and tolerancia == "sim":
    print('Chame um responsável para assistir com voce!')

# Condicionais para o genero de Aventura
if genero == "aventura" and faixaetaria == "sim" and tolerancia == "sim":
    print("Recomendação: ", filmesdeaventura[0])
elif genero == "aventura" and faixaetaria == "sim" and tolerancia == "nao":
    print("Recomendação: ", filmesdeaventura[1])
elif genero == "açao" and faixaetaria == "nao" and tolerancia == "nao":
    print("Recomendação: ", filmesdeaventura[2])
elif genero == "aventura" and faixaetaria == "nao" and tolerancia == "sim":
    print('Chame um responsável para assistir com voce!')

# Condicionais para o genero de Suspense
if genero == "suspense" and faixaetaria == "sim" and tolerancia == "sim":
    print("Recomendação: ", filmesdesuspense[1])
elif genero == "suspense" and faixaetaria == "sim" and tolerancia == "nao":
    print("Recomendação: ", filmesdesuspense[2])
elif genero == "suspense" and faixaetaria == "nao" and tolerancia == "nao":
    print("Recomendação: ", filmesdesuspense[0])
elif genero == "suspense" and faixaetaria == "nao" and tolerancia == "sim":
    print('Chame um responsável para assistir com voce!')