# 2. Leia o nome e a idade de uma pessoa e exiba uma mensagem com essas informações.

def exercicio2():

    print("\n 2. Leia o nome e a idade de uma pessoa e exiba uma mensagem com essas informações.")

    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    
    print()

    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")

if __name__ == "__main__":

    exercicio2()