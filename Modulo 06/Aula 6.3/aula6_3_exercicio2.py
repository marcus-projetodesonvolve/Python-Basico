# Lista original de URLs
urls = ["www.google.com", "www.microsoft.com", "www.amazon.com", "www.uol.com"]

# Lista de nomes principais dos domínios
dominios = [url[4:-4] for url in urls]

print("Lista de domínios principais:", dominios)