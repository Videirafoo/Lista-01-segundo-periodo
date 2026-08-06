# 6. Leia um número N e calcule a soma dos números de 1 até N.

def exercicio6():

    print("\n 6. Leia um número N e calcule a soma dos números de 1 até N.")

    print()

    n = int(input("Digite um número inteiro N: "))

    soma = sum(range(1, n + 1))

    print(f"A soma dos números de 1 até {n} é: {soma}")

if __name__ == "__main__":

    exercicio6()