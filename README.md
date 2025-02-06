# 🚀 Projeto Paradigmas: Criação de Página HTML com PLY

Este projeto implementa uma linguagem de comandos para gerar páginas HTML e CSS de forma dinâmica, permitindo a criação de telas, containers, botões, listas e muito mais.

## 👥 Autores
- Douglas Costa Bezerra
- Célio Vieira de Lima Junior

## 📜 Comandos Disponíveis

### 🖥️ Estrutura da Tela
- `CRIAR TELA NUMERO X NUMERO` → Cria uma tela com dimensões específicas.
- `CRIAR TELA` → Cria uma tela padrão (100% x 100%).

### ✍️ Texto
- `ADICIONAR TEXTO STRING` → Adiciona um parágrafo de texto.
- `COLORIR TEXTO STRING PARA STRING` → Altera a cor de um texto.
- `ADICIONAR CABECALHO COM TEXTO STRING` → Adiciona um cabeçalho (`h1`).
- `ADICIONAR CABECALHO SECUNDARIO COM TEXTO STRING` → Adiciona um subtítulo (`h3`).
- `ADICIONAR AJUDA PARA ITEM STRING COM TEXTO STRING` → Adiciona um tooltip (ajuda) a um elemento.

### 📦 Containers e Layout
- `ABRIR CONTAINER STRING NUMERO X NUMERO` → Abre um container com dimensões específicas.
- `ABRIR CONTAINER STRING` → Abre um container padrão (100% x 100%).
- `FECHAR CONTAINER` → Fecha um container.
- `ADICIONAR IMAGEM STRING COMO FUNDO NO CONTAINER STRING` → Define uma imagem como fundo de um container.
- `ALINHAR ITENS STRING STRING` → Alinha os itens dentro de um container (`align-items`).
- `JUSTIFICAR ITENS STRING STRING` → Define o posicionamento horizontal (`justify-content`).
- `ORGANIZAR STRING STRING` → Define a direção dos elementos (`flex-direction`).
- `ARREDONDAR STRING STRING` → Define o arredondamento das bordas (`border-radius`).

### 🎛️ Botões e Formulários
- `ADICIONAR BOTAO COM ROTULO STRING` → Adiciona um botão com rótulo.
- `ADICIONAR ENTRADA TIPO STRING COM ROTULO STRING` → Adiciona um campo de entrada (`input`).

### 🎨 Estilos e Aparência
- `APLICAR SOMBRA STRING NO STRING` → Aplica sombra a um elemento (`box-shadow`).
- `COLORIR STRING PARA STRING` → Altera a cor de fundo de um elemento.

### 📋 Listas
- `CRIAR LISTA STRING COM ITENS LISTAGEM` → Cria uma lista não ordenada (`ul`).
- `CRIAR LISTA ORDENADA STRING COM ITENS LISTAGEM` → Cria uma lista ordenada (`ol`).

## 🛠️ Como Usar
1. Clone este repositório.
2. Execute o interpretador da linguagem.
3. Digite os comandos para gerar os elementos desejados.
4. O código HTML e CSS será gerado automaticamente.

## 📌 Exemplo de Uso
```text
CRIAR TELA 800 X 600
ABRIR CONTAINER "principal" 400 X 400
ADICIONAR TEXTO "Bem-vindo ao meu site!"
COLORIR TEXTO "Bem-vindo ao meu site!" PARA "azul"
FECHAR CONTAINER
```
Isso gerará um HTML e CSS correspondente a uma tela com um container contendo um texto azul.

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## 📜 Licença
Este projeto está sob a licença MIT.

