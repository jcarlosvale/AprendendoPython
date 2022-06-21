import aluno

def menu():
    print("\n\n\n\n\n##### Sistema de Gerenciamento de Alunos #####")
    print("\nMenu: ")
    print("1 - Cadastrar Aluno")
    print("2 - Listar Alunos")
    print("3 - Atualizar Nota do Aluno")
    print("4 - Remover Aluno")
    print("5 - Sair")

def execute(command):
    if command == "1":
        print("\n\n-----Cadastrar Aluno-----")
        aluno.cadastrar()
    elif command == "2":
        print("\n\n-----Listar Alunos-----")
        aluno.listar()
    elif command == "3":
        print("\n\n-----Atualizar Aluno-----")
        aluno.atualizar()
    elif command == "4":
        print("\n\n-----Remover Aluno-----")
        aluno.remover()
    elif command == "5":
        print("Finalizando o programa...")
    else:
        print("Comando invalido")
    input("\nPressione qualquer tecla para continuar...")        

command = "0"
while command != "5":
    menu()
    command = input("Digite a opção desejada: ")
    execute(command)

