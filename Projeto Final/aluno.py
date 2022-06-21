alunos = {}

def analisar(media):
    if media >= 5: 
        return "Aprovado"
    else:
        return "Reprovado"

def cadastrar():
    nome  = input("Nome: ")

    if not nome.upper() in alunos:
        email = input("Email: ")    
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        media = (nota1 + nota2) / 2
        status = analisar(media)
        alunos[nome.upper()] = {
                        "nome": nome,
                        "email": email,
                        "nota1": nota1,
                        "nota2": nota2,
                        "media": media,
                        "status": status
                        }
        print(f"Aluno cadastrado com sucesso: {alunos[nome.upper()]}")
    else:
        print(f"Aluno já cadastrado: {alunos[nome.upper()]}")

def atualizar():
    nome  = input("Nome: ")

    if nome.upper() in alunos:

        aluno = alunos[nome.upper()]
        nota1 = aluno['nota1']
        nota2 = aluno['nota2']
        print(f"Notas do aluno {aluno['nome']}: {nota1} e {nota2}")

        opcao = ""
        while opcao.upper() != "S" or opcao.upper() != "N":
            opcao = input("Deseja alterar a nota 1? (S/N) ")        
        if opcao.upper() == "S":
            nota1 = float(input("Nota 1: "))
            aluno['nota1'] = nota1

        while opcao.upper() != "S" or opcao.upper() != "N":
            opcao = input("Deseja alterar a nota 2? (S/N) ")        
        if opcao.upper() == "S":
            nota2 = float(input("Nota 2: "))
            aluno['nota2'] = nota2

        aluno['media']  = (nota1 + nota2) / 2
        aluno['status'] = analisar(aluno['media'])
        print(f"Aluno atualizado com sucesso: {alunos[nome.upper()]}")
    else:
        print(f"Aluno não cadastrado: {nome}")        

def listar():
    print("Lista de Alunos: ")
    for aluno in alunos:
        print(alunos[aluno])

def remover():
    nome  = input("Nome: ")

    if nome.upper() in alunos:
        del alunos[nome.upper()]
        print(f"Aluno removido com sucesso: {nome}")
    else:
        print(f"Aluno não cadastrado: {nome}")
