# 7. Leia 10 números e informe a soma e a média.

def exercicio7():

    print("\n 7. Leia 10 números e informe a soma e a média.")

    print()

    numeros = []

    for i in range(10):
        numero = float(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)

    soma = sum(numeros)
    media = soma / len(numeros)

    print(f"\nA soma dos números é: {soma}")
    print()
    print(f"A média dos números é: {media}")

if __name__ == "__main__":

    exercicio7()