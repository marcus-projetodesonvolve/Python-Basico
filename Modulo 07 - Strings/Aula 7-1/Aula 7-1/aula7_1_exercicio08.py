import re

def validar_cpf(cpf_str):
    # Verifica o formato usando regex
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf_str):
        return "Inválido"

    # Remove pontos e traço
    cpf = re.sub(r'\D', '', cpf_str)

    # Verifica se todos os dígitos são iguais (caso inválido)
    if cpf == cpf[0] * 11:
        return "Inválido"

    # Calcula o primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    # Calcula o segundo dígito verificador
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    # Verifica se os dígitos calculados batem com os fornecidos
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return "Válido"
    else:
        return "Inválido"

# Solicita o CPF do usuário
cpf_input = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")
resultado = validar_cpf(cpf_input)
print(resultado)