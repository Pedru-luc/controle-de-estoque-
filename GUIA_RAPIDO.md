# 🚀 Guia Rápido - Interface Web de Estoque

## Passo 1: Instalar Dependências

Abra o terminal na pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

Ou simplesmente **clique duas vezes em `iniciar.bat`** (Windows) ou `iniciar.sh` (Linux/Mac)

## Passo 2: Iniciar o Servidor

### Opção A: Clicando no arquivo (Mais Fácil)
- **Windows**: Clique duas vezes em `iniciar.bat`
- **Linux/Mac**: Abra o terminal e execute `./iniciar.sh`

### Opção B: Pelo Terminal
```bash
python app.py
```

Você verá:
```
 * Running on http://127.0.0.1:5000
```

## Passo 3: Abrir a Interface

Com o servidor rodando, clique duas vezes em **`index.html`** para abrir no navegador.

Ou acesse diretamente: http://localhost:5000

---

## 📊 Interface - Guia de Abas

### 1. **📊 Estoque** (Aba Inicial)

Exibe todos os produtos em cards bonitos com:
- ✅ Quantidade em estoque
- 💰 Preço unitário
- 📊 Valor total do produto

**Ações Rápidas:**
- ➕ **Entrada**: Adiciona unidades ao estoque
- ➖ **Saída**: Remove unidades do estoque
- ✏️ **Editar**: Muda nome e preço
- 🗑️ **Deletar**: Remove o produto

![Exemplo: Cards dos produtos]

```
┌─────────────────────────────────┐
│ Mouse Logitech                  │
│ Código: P001                    │
│ ┌─────────┬──────────┬────────┐ │
│ │70      │R$ 89,90  │R$ 6.293│ │
│ │unidades│unitário  │total   │ │
│ └─────────┴──────────┴────────┘ │
│ [➕ Entrada] [➖ Saída]          │
│ [✏️ Editar] [🗑️ Deletar]        │
└─────────────────────────────────┘
```

---

### 2. **🏷️ Produtos** (Gerenciamento)

#### Adicionar Novo Produto:
1. Preencha o formulário:
   - **Código**: P001, P002, etc
   - **Nome**: Nome do produto
   - **Preço**: Valor unitário (ex: 89.90)
   - **Quantidade**: Inicial (ex: 10)
2. Clique em **"Adicionar Produto"**

#### Tabela de Produtos:
Visualize todos em uma tabela com:
- Código
- Nome
- Preço
- Quantidade
- Botões de ação

---

### 3. **📝 Movimentações** (Histórico)

Exibe TODAS as entradas e saídas com:
- Data e Hora
- Tipo (Entrada 🔼 ou Saída 🔽)
- Código do Produto
- Quantidade
- Motivo

**Filtro:** Digite um código para ver apenas as movimentações daquele produto

---

### 4. **📈 Relatório** (Resumo)

Mostra:
- 📌 **Total de Produtos**: Quantos produtos diferentes
- 💰 **Valor Total do Estoque**: Soma de tudo
- 📊 **Total de Movimentações**: Quantas operações foram feitas

**Tabela Detalhada:**
Cada produto com:
- Código
- Nome
- Preço Unitário
- Quantidade
- Valor Total

**Botão 📄 Exportar PDF**: Imprime o relatório

---

## 🎨 Interface Visual

### Header (Topo)
```
┌──────────────────────────────────────────────┐
│         📦 Controle de Estoque               │
│  6 Produtos │ R$ 12.345,67 │ 120 Movim.    │
└──────────────────────────────────────────────┘
```

### Menu (Abas)
```
[📊 Estoque] [🏷️ Produtos] [📝 Movimentações] [📈 Relatório]
```

### Cores
- 🔵 **Azul** (Primário): Ações principais
- 🟢 **Verde** (Sucesso): Entradas, confirmações
- 🔴 **Vermelho** (Perigo): Saídas, deleções

---

## 🎯 Tarefas Comuns

### ➕ Registrar Entrada de Estoque

1. Vá para **"📊 Estoque"**
2. Encontre o produto
3. Clique em **"➕ Entrada"**
4. Na janela:
   - **Quantidade**: Digite quantas unidades
   - **Motivo**: Compra, Devolução, etc.
5. Clique em **"Confirmar"**

✅ Pronto! A quantidade foi aumentada e a movimentação registrada.

---

### ➖ Registrar Saída de Estoque

1. Vá para **"📊 Estoque"**
2. Encontre o produto
3. Clique em **"➖ Saída"**
4. Na janela:
   - **Quantidade**: Digite quantas unidades
   - **Motivo**: Venda, Perda, Dvolução, etc.
5. Clique em **"Confirmar"**

✅ Pronto! A quantidade foi diminuída e a movimentação registrada.

---

### 🆕 Adicionar Novo Produto

1. Vá para **"🏷️ Produtos"**
2. No formulário no topo:
   - **Código**: P010 (ou outro código único)
   - **Nome**: Nome do Produto
   - **Preço**: 199.90
   - **Quantidade**: 5
3. Clique em **"Adicionar Produto"**

✅ O produto aparecerá na tabela e no estoque!

---

### 🔍 Consultar Movimentações de um Produto

1. Vá para **"📝 Movimentações"**
2. No campo **"Filtrar por código"**, digite: P001
3. Veja apenas as movimentações daquele produto

---

### 📄 Gerar Relatório para Impressão

1. Vá para **"📈 Relatório"**
2. Veja o resumo e a tabela
3. Clique em **"📄 Exportar PDF"**
4. Seu navegador abrirá a janela de impressão
5. Clique em **"Imprimir"** ou **"Salvar como PDF"**

---

## ⚠️ Mensagens

### ✅ Sucesso (Verde)
```
✓ Entrada registrada: +50 unidades de 'Mouse Logitech'
```

### ❌ Erro (Vermelho)
```
❌ Erro: Quantidade insuficiente! Disponível: 45
```

### ℹ️ Informação (Azul)
```
ℹ️ Preencha todos os campos obrigatórios
```

---

## 💡 Dicas Úteis

1. **Atualização em Tempo Real**: Tudo se atualiza automaticamente
2. **Responsivo**: Funciona em celular, tablet e computador
3. **Sem Banco de Dados**: Usa JSON, não precisa de servidor complexo
4. **Dados Persistem**: Tudo é salvo automaticamente
5. **Sem Login**: Acesso direto (pode adicionar segurança depois)

---

## 🆘 Problemas Comuns

### "Erro ao conectar ao servidor"
- ✅ Verifique se `app.py` está rodando
- ✅ A porta 5000 está livre?
- ✅ Recarregue a página (F5)

### "ModuleNotFoundError: flask"
```bash
pip install -r requirements.txt
```

### "index.html não encontra dados"
- ✅ Certifique-se que `app.py` está rodando
- ✅ Recarregue a página
- ✅ Abra o console (F12) e veja os erros

### "Dados não aparecem"
- ✅ Verifique se `estoque.json` existe
- ✅ Não mexa no arquivo manualmente
- ✅ Deixe o sistema gerenciar os dados

---

## 📞 Suporte

Para dúvidas:
1. Veja o arquivo `README.md` (documentação do sistema)
2. Veja o arquivo `README_WEB.md` (documentação da web)
3. Verifique o arquivo `estoque.json` para entender a estrutura

---

**Desenvolvido com ❤️ para facilitar seu controle de estoque!** 🎉
