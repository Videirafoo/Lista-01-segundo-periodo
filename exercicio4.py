# 4. Leia a nota de um aluno e informe se ele foi aprovado (nota ≥ 7) ou reprovado.

def exercicio4():
    print("\n 4. Leia a nota de um aluno e informe se ele foi aprovado (nota ≥ 7) ou reprovado.")

    print()

    nota = float(input("Digite a nota do aluno: "))
    if nota >= 7:
        print("O aluno foi aprovado.")
    else:
        print("O aluno foi reprovado.")

if __name__ == "__main__":

    exercicio4()