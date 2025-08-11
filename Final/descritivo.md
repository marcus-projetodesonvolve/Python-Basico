Documento Descritivo do Trabalho Prático
1. Introdução
Este sistema foi modelado para a Panificadora "Sabor & Cia", uma empresa fictícia que oferece uma variedade de produtos frescos, como pães, bolos e salgados. O sistema é voltado para o gerenciamento interno de usuários e estoque de produtos.
Existem dois níveis de usuário no sistema:
Gerente: Possui permissão total (CRUD) para gerenciar usuários e produtos.
Funcionário: Possui permissão limitada, podendo apenas consultar (Read) as informações dos produtos.
2. Implementação
2.1. Usuários
Estrutura de Dados: Para armazenar os usuários em memória, foi escolhida a estrutura de dados dicionário. A chave de cada entrada é o nome de usuário (uma string única), e o valor é outro dicionário contendo a senha e o tipo de permissão do usuário. Essa abordagem permite uma busca e acesso eficientes por nome de usuário.
Exemplo: {'gerente1': {'senha': '123', 'tipo': 'gerente'}}
Estrutura do Arquivo: O arquivo usuarios.txt utiliza o formato de texto simples. Cada linha representa um usuário, com os campos nome_usuario, senha e tipo_usuario separados por vírgulas.
Funcionalidades (CRUD):
C (Create): O gerente pode cadastrar novos usuários.
R (Read): O gerente pode visualizar a lista de todos os usuários cadastrados.
U (Update): O gerente pode atualizar a senha de um usuário existente.
D (Delete): O gerente pode remover um usuário do sistema.
2.2. Produtos
Estrutura de Dados: Os produtos também são armazenados em um dicionário. A chave é o código do produto (uma string única), e o valor é um dicionário com os detalhes do produto, como nome, preco e quantidade. Isso permite o acesso rápido a um produto específico pelo seu código.
Exemplo: {'P001': {'nome': 'Pão Francês', 'preco': 0.50, 'quantidade': 100}}
Estrutura do Arquivo: O arquivo produtos.txt também é um arquivo de texto simples, com cada linha representando um produto e seus campos: codigo, nome, preco e quantidade separados por vírgulas.
Funcionalidades (CRUD):
C (Create): O gerente pode adicionar novos produtos ao estoque.
R (Read): A única funcionalidade de leitura disponível é a listagem de todos os produtos, que agora também exibe o código de cada item.
U (Update): O gerente pode alterar o nome, preço ou quantidade de um produto.
D (Delete): O gerente pode remover um produto do estoque.
3. Conclusão
A principal dificuldade encontrada foi garantir a persistência dos dados entre as execuções, o que foi resolvido com o uso de funções para carregar e salvar os dados nos arquivos TXT a cada alteração. A escolha de dicionários como estrutura de dados se mostrou muito eficiente para a busca e manipulação de informações, especialmente para o CRUD.
Em uma versão futura, seria interessante refatorar o código usando classes para representar "Usuário" e "Produto", o que tornaria a solução mais escalável e orientada a objetos. Além disso, a separação do código em diferentes arquivos (módulos) poderia melhorar a organização do projeto.
