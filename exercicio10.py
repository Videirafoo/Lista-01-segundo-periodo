# 10. Desafio: Faça um programa que leia 5 números e informe o maior e o menor valor.

def exercicio10():

    print("\n 10. Desafio: Faça um programa que leia 5 números e informe o maior e o menor valor.")

    print()

    numeros = []

    for i in range(5):
        numero = float(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)

    maior = max(numeros)
    menor = min(numeros)

    print(f"\nO maior número é: {maior}")
    print(f"O menor número é: {menor}")

if __name__ == "__main__":

    exercicio10()