import sys

# Estruturas de dados globais
usuarios = {}
produtos = {}
usuario_logado = None

# --- Funções de Gerenciamento de Arquivos ---
def carregar_dados():
    """Carrega dados de usuários e produtos dos arquivos TXT."""
    global usuarios, produtos
    try:
        # Carregar usuários
        with open('usuarios.txt', 'r', encoding='utf-8') as f:
            for line in f:
                nome_usuario, senha, tipo = line.strip().split(',')
                usuarios[nome_usuario] = {'senha': senha, 'tipo': tipo}
        
        # Carregar produtos
        with open('produtos.txt', 'r', encoding='utf-8') as f:
            for line in f:
                codigo, nome, preco, quantidade = line.strip().split(',')
                produtos[codigo] = {
                    'nome': nome,
                    'preco': float(preco),
                    'quantidade': int(quantidade)
                }
    except FileNotFoundError:
        print("Arquivos de dados não encontrados. Criando arquivos com dados iniciais.")
        # Criar arquivos com dados padrão caso não existam
        with open('usuarios.txt', 'w', encoding='utf-8') as f:
            f.write('gerente1,123,gerente\n')
            f.write('funcionario1,abc,funcionario\n')
            f.write('funcionario2,456,funcionario\n')
        
        with open('produtos.txt', 'w', encoding='utf-8') as f:
            f.write('P001,Pão Francês,0.5,150\n')
            f.write('P002,Pão de Queijo,1.5,50\n')
            f.write('B001,Bolo de Chocolate,25.0,5\n')
            f.write('S001,Coxinha de Frango,6.0,30\n')
            f.write('D001,Brigadeiro,2.5,40\n')
        
        # Recarregar os dados após a criação dos arquivos
        carregar_dados()

def salvar_usuarios():
    """Salva os dados de usuários no arquivo TXT."""
    with open('usuarios.txt', 'w', encoding='utf-8') as f:
        for nome_usuario, info in usuarios.items():
            f.write(f"{nome_usuario},{info['senha']},{info['tipo']}\n")

def salvar_produtos():
    """Salva os dados de produtos no arquivo TXT."""
    with open('produtos.txt', 'w', encoding='utf-8') as f:
        for codigo, info in produtos.items():
            f.write(f"{codigo},{info['nome']},{info['preco']},{info['quantidade']}\n")

# --- Funções de Login e Menu ---
def login():
    """Realiza o login do usuário."""
    global usuario_logado
    print("\n--- Login ---")
    nome_usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    
    if nome_usuario in usuarios and usuarios[nome_usuario]['senha'] == senha:
        usuario_logado = usuarios[nome_usuario]
        print(f"Login bem-sucedido! Bem-vindo(a), {nome_usuario}.")
        return True
    else:
        print("Nome de usuário ou senha incorretos.")
        return False

def logout():
    """Faz o logout do usuário atual."""
    global usuario_logado
    usuario_logado = None
    print("Logout realizado.")

def menu_principal():
    """Exibe o menu principal para o usuário logado."""
    while True:
        if usuario_logado['tipo'] == 'gerente':
            menu_gerente()
        elif usuario_logado['tipo'] == 'funcionario':
            menu_funcionario()
        
        # Permite ao usuário fazer logout ou sair do programa
        print("\nO que deseja fazer agora?")
        print("1. Fazer logout")
        print("2. Sair do programa")
        
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            logout()
            break
        elif escolha == '2':
            sys.exit("Saindo do programa.")
        else:
            print("Opção inválida.")

# --- Funções de CRUD de Usuários (Gerente) ---
def criar_usuario():
    """(C)ria um novo usuário."""
    print("\n--- Cadastrar Novo Usuário ---")
    nome_usuario = input("Nome de usuário: ")
    if nome_usuario in usuarios:
        print("Erro: Nome de usuário já existe.")
        return
    
    senha = input("Senha: ")
    tipo = input("Tipo (gerente/funcionario): ").lower()
    while tipo not in ['gerente', 'funcionario']:
        print("Tipo inválido. Por favor, escolha 'gerente' ou 'funcionario'.")
        tipo = input("Tipo (gerente/funcionario): ").lower()
    
    usuarios[nome_usuario] = {'senha': senha, 'tipo': tipo}
    salvar_usuarios()
    print(f"Usuário '{nome_usuario}' cadastrado com sucesso!")

def listar_usuarios():
    """(R)ead: Lista todos os usuários cadastrados."""
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    for nome_usuario, info in usuarios.items():
        print(f"Nome: {nome_usuario}, Tipo: {info['tipo']}")

def atualizar_usuario():
    """(U)pdate: Atualiza a senha de um usuário."""
    print("\n--- Atualizar Senha de Usuário ---")
    nome_usuario = input("Digite o nome do usuário a ser atualizado: ")
    
    if nome_usuario not in usuarios:
        print("Erro: Usuário não encontrado.")
        return
    
    nova_senha = input(f"Digite a nova senha para '{nome_usuario}': ")
    usuarios[nome_usuario]['senha'] = nova_senha
    salvar_usuarios()
    print(f"Senha do usuário '{nome_usuario}' atualizada com sucesso!")

def excluir_usuario():
    """(D)elete: Exclui um usuário do sistema."""
    print("\n--- Excluir Usuário ---")
    nome_usuario = input("Digite o nome do usuário a ser excluído: ")
    
    if nome_usuario not in usuarios:
        print("Erro: Usuário não encontrado.")
        return
        
    del usuarios[nome_usuario]
    salvar_usuarios()
    print(f"Usuário '{nome_usuario}' excluído com sucesso.")

# --- Funções de CRUD de Produtos ---
def criar_produto():
    """(C)ria um novo produto."""
    print("\n--- Cadastrar Novo Produto ---")
    codigo = input("Código do produto: ")
    if codigo in produtos:
        print("Erro: Código de produto já existe.")
        return
    
    nome = input("Nome do produto: ")
    try:
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Erro: Preço e quantidade devem ser números.")
        return
    
    produtos[codigo] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
    salvar_produtos()
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_produtos():
    """(R)ead: Lista todos os produtos."""
    print("\n--- Lista de Produtos ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    for codigo, produto in produtos.items():
        print(f"Código: {codigo:<5} | Nome: {produto['nome']:<20} | Preço: R$ {produto['preco']:>5.2f} | Quantidade: {produto['quantidade']}")

def atualizar_produto():
    """(U)pdate: Atualiza as informações de um produto."""
    print("\n--- Atualizar Produto ---")
    codigo = input("Digite o código do produto a ser atualizado: ")
    
    if codigo not in produtos:
        print("Erro: Produto não encontrado.")
        return
        
    print(f"Produto selecionado: {produtos[codigo]['nome']}")
    print("O que você deseja atualizar?")
    print("1. Nome")
    print("2. Preço")
    print("3. Quantidade")
    
    escolha = input("Digite sua escolha: ")
    
    if escolha == '1':
        novo_nome = input("Novo nome: ")
        produtos[codigo]['nome'] = novo_nome
    elif escolha == '2':
        try:
            novo_preco = float(input("Novo preço: "))
            produtos[codigo]['preco'] = novo_preco
        except ValueError:
            print("Erro: O preço deve ser um número.")
            return
    elif escolha == '3':
        try:
            nova_quantidade = int(input("Nova quantidade: "))
            produtos[codigo]['quantidade'] = nova_quantidade
        except ValueError:
            print("Erro: A quantidade deve ser um número inteiro.")
            return
    else:
        print("Opção inválida.")
        return
        
    salvar_produtos()
    print("Produto atualizado com sucesso!")

def excluir_produto():
    """(D)elete: Exclui um produto do sistema."""
    print("\n--- Excluir Produto ---")
    codigo = input("Digite o código do produto a ser excluído: ")
    
    if codigo not in produtos:
        print("Erro: Produto não encontrado.")
        return
        
    del produtos[codigo]
    salvar_produtos()
    print("Produto excluído com sucesso!")

# --- Menus de Navegação ---
def menu_gerente():
    """Exibe as opções do menu para o Gerente."""
    while True:
        print("\n--- Menu Gerente ---")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Produtos")
        print("3. Voltar")
        
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            sub_menu_gerenciar_usuarios()
        elif escolha == '2':
            sub_menu_gerenciar_produtos()
        elif escolha == '3':
            return
        else:
            print("Opção inválida.")

def sub_menu_gerenciar_usuarios():
    """Sub-menu para gerenciar usuários."""
    while True:
        print("\n--- Gerenciar Usuários ---")
        print("1. Cadastrar novo usuário (C)")
        print("2. Listar todos os usuários (R)")
        print("3. Atualizar senha de usuário (U)")
        print("4. Excluir usuário (D)")
        print("5. Voltar")
        
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            criar_usuario()
        elif escolha == '2':
            listar_usuarios()
        elif escolha == '3':
            atualizar_usuario()
        elif escolha == '4':
            excluir_usuario()
        elif escolha == '5':
            return
        else:
            print("Opção inválida.")
            
def sub_menu_gerenciar_produtos():
    """Sub-menu para gerenciar produtos (Gerente)."""
    while True:
        print("\n--- Gerenciar Produtos ---")
        print("1. Cadastrar novo produto (C)")
        print("2. Listar todos os produtos (R)")
        print("3. Atualizar informações do produto (U)")
        print("4. Excluir produto (D)")
        print("5. Voltar")
        
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            criar_produto()
        elif escolha == '2':
            listar_produtos()
        elif escolha == '3':
            atualizar_produto()
        elif escolha == '4':
            excluir_produto()
        elif escolha == '5':
            return
        else:
            print("Opção inválida.")

def menu_funcionario():
    """Exibe as opções do menu para o Funcionário."""
    while True:
        print("\n--- Menu Funcionário ---")
        print("1. Listar todos os produtos (R)")
        print("2. Voltar")
        
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            listar_produtos()
        elif escolha == '2':
            return
        else:
            print("Opção inválida.")

# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    carregar_dados()
    while True:
        if login():
            menu_principal()
        else:
            # Opção de tentar novamente ou sair após login falho
            print("Deseja tentar novamente? (s/n)")
            tentar_novamente = input("> ").lower()
            if tentar_novamente != 's':
                sys.exit("Saindo do programa.")
