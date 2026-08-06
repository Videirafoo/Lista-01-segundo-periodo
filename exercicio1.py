# Lista de Exercícios – Revisão Inicial de Algoritmos em Python

# Objetivo: Revisar os principais conceitos de algoritmos utilizando Python.

# 1. Leia dois números e exiba a soma, subtração, multiplicação e divisão.


def exercicio1():


    print("1. Leia dois números e exiba a soma, subtração, multiplicação e divisão.")

    print()

    numero1 = float(input("Digite o primeiro número: "))

    numero2 = float(input("Digite o segundo número: "))

    print()

    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2

    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")

    if numero2 != 0:

        divisao = numero1 / numero2

        print(f"Divisão: {divisao}")

    else:

        print("Não é possível dividir por zero.")

    print()

if __name__ == "__main__":

    exercicio1()