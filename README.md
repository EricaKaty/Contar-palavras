# Contador de palavras, linhas e caracteres
# Recebe um arquivo .txt e conta palavras, linhas e caracteres.

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
    caminho = input("Digite o caminho do arquivo .txt: ")
    total_palavras, total_linhas, total_caracteres = contar_arquivo(caminho)
    
    print(f"✅ Total de palavras: {total_palavras}")
    print(f"✅ Total de linhas: {total_linhas}")
    print(f"✅ Total de caracteres: {total_caracteres}")


# 📝 Contador de Palavras

Este é um projeto simples em Python que conta o número de palavras em um arquivo `.txt`.

---

## ⚙️ Como funciona

O script pede o caminho para um arquivo `.txt`, abre o arquivo e conta quantas palavras ele contém.

---

## 🚀 Como executar

1. **Clone o repositório**:
```bash
git clone https://github.com/seu-usuario/contador-palavras.git
cd contador-palavras


contador-palavras/
│── contar_palavras.py   # seu código Python
│── README.md            # documentação
│── .gitignore           # lista de arquivos para ignorar no Git