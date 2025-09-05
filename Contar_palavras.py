def contar_arquivo(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            palavras = conteudo.split()
            linhas = conteudo.splitlines()
            caracteres = len(conteudo)
            return len(palavras), len(linhas), caracteres
    except FileNotFoundError:
        print(f"❌ Arquivo '{arquivo}' não encontrado.")
        return 0, 0, 0
    except PermissionError:
        print(f"❌ Sem permissão para ler o arquivo '{arquivo}'.")
        return 0, 0, 0
    except Exception as e:
        print(f"❌ Ocorreu um erro ao ler o arquivo: {e}")
        return 0, 0, 0

if __name__ == "__main__":
    print("📊 Contador de palavras, linhas e caracteres")
    caminho = input("Digite o caminho do arquivo .txt: ")
    total_palavras, total_linhas, total_caracteres = contar_arquivo(caminho)
    print(f"\n✅ Total de palavras: {total_palavras}")
    print(f"✅ Total de linhas: {total_linhas}")
    print(f"✅ Total de caracteres: {total_caracteres}")