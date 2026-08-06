# Importa as funções que estão nos arquivos dos exercícios

from exercicio1 import exercicio1
from exercicio2 import exercicio2
from exercicio3 import exercicio3
from exercicio4 import exercicio4
from exercicio5 import exercicio5
from exercicio6 import exercicio6
from exercicio7 import exercicio7
from exercicio8 import exercicio8
from exercicio9 import exercicio9
from exercicio10 import exercicio10


exercicios = [
    exercicio1,
    exercicio2,
    exercicio3,
    exercicio4,
    exercicio5,
    exercicio6,
    exercicio7,
    exercicio8,
    exercicio9,
    exercicio10
]


print()
print("LISTA DE EXERCÍCIOS — ALGORITMOS EM PYTHON")
print()


for numero, exercicio in enumerate(exercicios, start=1):

    exercicio()

    if numero < len(exercicios):

        input(f"Pressione Enter para continuar para a questão {numero + 1}...")

        print("\n")


print()
print(" CHEGAMOS AO FIM (03/08/2026) — LISTA DE EXERCÍCIOS CONCLUÍDA 2° PERIODO (ALGORITMOS EM PYTHON)")
print()