# Contador de Palavras, Linhas e Caracteres

Este projeto conta palavras, linhas e caracteres de arquivos `.txt`.

## Como executar

1. Clone o repositório:

2. Execute o script:

3. Exemplo:

Entendi! Sem problemas — podemos simplificar para que você consiga organizar o GitHub sem complicações.

Você pode deixar tudo bem simples assim:


---

1️⃣ Código Python

Crie apenas o arquivo contar_palavras.py

Copie apenas o código Python dentro dele (sem README, sem instruções)


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


---

2️⃣ README.md simples

Crie um arquivo chamado README.md na mesma pasta

Cole apenas isso dentro dele:


# Contador de Palavras, Linhas e Caracteres

Este projeto conta palavras, linhas e caracteres de arquivos `.txt`.

## Como executar

1. Clone o repositório:

git clone https://github.com/seu-usuario/contador-palavras.git cd contador-palavras

2. Execute o script:

python contar_palavras.py

3. Exemplo:

📊 Contador de palavras, linhas e caracteres Digite o caminho do arquivo .txt: exemplo.txt

✅ Total de palavras: 120 ✅ Total de linhas: 10 ✅ Total de caracteres: 

