# 5. Leia um número inteiro e mostre sua tabuada de 1 a 10.

def exercicio5():

    print("\n 5. Leia um número inteiro e mostre sua tabuada de 1 a 10.")

    print()

    numero = int(input("Digite um número inteiro: "))

    print(f"Tabuada de {numero}:")

    for i in range(1, 11):

        print(f"{numero} x {i} = {numero * i}")

if __name__ == "__main__":

    exercicio5()