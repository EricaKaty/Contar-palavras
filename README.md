# 📄 Contar_palavras.py.
# Recebe um arquivo .txt e retorna a contagem de palavras, linhas e caracteres.

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

## ⚙️ Como funciona

O script solicita ao usuário o caminho para um arquivo `.txt`, abre o arquivo e realiza a contagem.

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


📊 Contador de palavras, linhas e caracteres
Digite o caminho do arquivo .txt: exemplo.txt

✅ Total de palavras: 120
✅ Total de linhas: 10
✅ Total de caracteres: 650