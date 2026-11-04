# Algoritmo: movimentos do cavalo em um tabuleiro de xadrez

tabuleiro = [["." for coluna in range(8)] for linha in range(8)]

while True:
    try:
        linha = int(input("Digite a linha do cavalo (0 a 7): "))
        coluna = int(input("Digite a coluna do cavalo (0 a 7): "))

        if 0 <= linha <= 7 and 0 <= coluna <= 7:
            break
        print("Posicao invalida! Digite numeros entre 0 e 7.")
    except ValueError:
        print("Entrada invalida! Digite apenas numeros inteiros.")

tabuleiro[linha][coluna] = "C"

movimentos = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

for movimento_linha, movimento_coluna in movimentos:
    nova_linha = linha + movimento_linha
    nova_coluna = coluna + movimento_coluna

    if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
        tabuleiro[nova_linha][nova_coluna] = "*"

print("\nTabuleiro com os movimentos do cavalo:\n")
for linha_tabuleiro in tabuleiro:
    print(" ".join(linha_tabuleiro))
