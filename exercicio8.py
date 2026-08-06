# 8. Leia vários números até que o usuário digite 0. Ao final, informe a soma dos valores digitados.

def exercicio8():

    print("\n 8. Leia vários números até que o usuário digite 0. Ao final, informe a soma dos valores digitados.")

    print()

    soma = 0

    while True:
    
        numero = float(input("Digite um número ou 0 para finalizar: "))

        if numero == 0:
            break

        soma += numero

    print()

    print(f"A soma dos valores digitados é {soma}.")

if __name__ == "__main__":

    exercicio8()