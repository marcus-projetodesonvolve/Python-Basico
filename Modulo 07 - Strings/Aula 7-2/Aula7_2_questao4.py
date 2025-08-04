import re

def validador_senha(senha):
    erros = []

    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")

    if not re.search(r"[A-Z]", senha):
        erros.append("A senha deve conter ao menos uma letra maiúscula.")

    if not re.search(r"[a-z]", senha):
        erros.append("A senha deve conter ao menos uma letra minúscula.")

    if not re.search(r"\d", senha):
        erros.append("A senha deve conter ao menos um número.")

    if not re.search(r"[@#$]", senha):
        erros.append("A senha deve conter ao menos um caractere especial (@, # ou $).")

    if erros:
        print("Senha inválida:")
        for erro in erros:
            print(erro)
    else:
        print("Senha válida!")

# Exemplo de uso
senha = input("Digite sua senha: ")
validador_senha(senha)