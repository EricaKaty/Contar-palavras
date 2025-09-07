# Contador de Palavras, Linhas e Caracteres

Este projeto conta palavras, linhas e caracteres de arquivos `.txt`.


## Como executar

1. Clone o repositório:

git clone https://github.com/EricaKaty/contador-palavras.git cd contador-palavras

2. Execute o script:

python contar_palavras.py exemplo.txt

3. Exemplo:

📊 Contador de palavras, linhas e caracteres Digite o caminho do arquivo .txt: exemplo.txt

✅ Total de palavras: 120 
✅ Total de linhas: 10 
✅ Total de caracteres: 543

## Requisitos

Python 3 instalado na sua maquina
Um arquivo .txt para testar





Conceitos aprendidos

1. Leitura de arquivos em Python

Você aprendeu a abrir arquivos .txt usando:

with open('arquivo.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()

Entendeu a importância de usar encoding='utf-8' para evitar problemas com caracteres especiais.



2. Manipulação de strings

Contagem de palavras usando split().

Contagem de caracteres usando len(conteudo).

Contagem de linhas usando conteudo.splitlines() ou percorrendo for linha in f:.



3. Tratamento de exceções

Você aprendeu a lidar com erros, como quando o arquivo não existe, usando try...except FileNotFoundError.



4. Entrada do usuário

Saber pedir o caminho do arquivo com input().



5. Exibição de resultados

Aprendeu a imprimir informações de forma clara e organizada usando print().



6. Organização de projetos

Criou um README explicativo para explicar o projeto, como executar, requisitos e exemplo de uso.

Aprendeu a estruturar comandos de terminal no README.
