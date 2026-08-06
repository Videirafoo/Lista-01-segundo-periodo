# 3. Leia um número e informe se ele é positivo, negativo ou zero.

def exercicio3():

    print("\n 3. Leia um número e informe se ele é positivo, negativo ou zero.")

    print()

    numero = float(input("Digite um número: "))

    if numero > 0:

        print("O número é positivo.")

    elif numero < 0:

        print("O número é negativo.")

    else:

        print("O número é zero.")

if __name__ == "__main__":

    exercicio3()