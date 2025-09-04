# Contar-palavras
Ele recebe um arquivo .txt e conta quantas palavras existem dentro dele.

def contar_palavras(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            palavras = conteudo.split()
            return len(palavras)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado.")
        return 0

if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo .txt: ")
    total = contar_palavras(caminho)
    print(f"Total de palavras: {total}")
# Não há bibliotecas externas neste projeto.
__pycache__/
*.pyc
venv/

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
