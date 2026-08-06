# 9. Crie uma função que receba dois números e retorne o maior deles.


def encontrar_maior(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2


def exercicio9():

    print("\n9. Crie uma função que receba dois números e retorne o maior deles.")
    print()

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    maior = encontrar_maior(numero1, numero2)

    print()

    if numero1 == numero2:
        print("Os dois números são iguais.")
    else:
        print(f"O maior número é: {maior}")


if __name__ == "__main__":
    exercicio9()