import emoji

# Dicionário de emojis disponíveis
emojis_disponiveis = {

    "❤️ - :red_heart:"
    "👍 - :thumbs_up:"
    "🤔 - :thinking_face:"
    "🥳 - :partying_face:"
  
}

# Exibindo a lista de emojis disponíveis
print("Lista de emojis disponíveis:")
for codigo, emoji in emojis_disponiveis.items():
    print("{codigo} => {emoji}")

# Solicitando frase codificada ao usuário
frase_codificada = input("\nDigite uma frase usando os códigos de emoji (ex: Olá :sorriso: tudo bem? :joinha:): ")

# Substituindo os códigos pelos emojis reais
frase_emojizada = frase_codificada
for codigo, emoji in emojis_disponiveis.items():
    frase_emojizada = frase_emojizada.replace(codigo, emoji)

# Mostrando a frase com emojis
print("\nFrase com emojis:")
print(frase_emojizada)