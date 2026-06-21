# Controle de Estoque

Um sistema completo de controle de estoque com funcionalidades de entrada e saída de produtos.

## Funcionalidades

✅ **Gerenciamento de Produtos**
- Adicionar novos produtos ao estoque
- Visualizar informações de produtos específicos
- Listar todos os produtos com valores

✅ **Entradas e Saídas**
- Registrar entrada de estoque (compras, devoluções, etc.)
- Registrar saída de estoque (vendas, perdas, etc.)
- Validação automática de quantidade disponível

✅ **Histórico e Relatórios**
- Histórico completo de movimentações
- Filtrar movimentações por produto
- Relatório completo com valor total do estoque
- Persistência de dados em JSON

## Instalação

Não requer dependências externas! O programa usa apenas bibliotecas padrão do Python 3.6+

## Como Usar

Execute o programa:
```bash
python estoque.py
```

### Menu de Opções

1. **Adicionar Produto** - Registra um novo produto no sistema
2. **Entrada de Estoque** - Registra uma entrada (compra, devolução, etc.)
3. **Saída de Estoque** - Registra uma saída (venda, perda, etc.)
4. **Listar Produtos** - Exibe todos os produtos e seu valor total
5. **Listar Movimentações** - Exibe histórico de entradas/saídas
6. **Informações de um Produto** - Consulta detalhes específicos
7. **Relatório Completo** - Gera relatório geral do estoque
8. **Sair** - Encerra o programa

## Estrutura de Dados

Os dados são salvos automaticamente em `estoque.json` com a seguinte estrutura:

```json
{
  "produtos": [
    {
      "codigo": "P001",
      "nome": "Notebook",
      "preco": 2500.00,
      "quantidade": 5
    }
  ],
  "movimentacoes": [
    {
      "tipo": "entrada",
      "codigo_produto": "P001",
      "quantidade": 10,
      "motivo": "Compra",
      "data": "2026-06-21 14:30:45"
    }
  ]
}
```

## Exemplo de Uso

```
1. Adicionar Produto
   - Código: P001
   - Nome: Mouse
   - Preço: 50.00
   - Quantidade: 100

2. Entrada de Estoque
   - Código: P001
   - Quantidade: 50
   - Motivo: Reposição

3. Saída de Estoque
   - Código: P001
   - Quantidade: 30
   - Motivo: Venda
```

## Características Técnicas

- **Programação Orientada a Objetos** - Classes bem estruturadas
- **Persistência de Dados** - Salva automaticamente em JSON
- **Validação de Entradas** - Evita erros de quantidade e produtos duplicados
- **Interface Amigável** - Menu interativo com feedback visual
- **Histórico Completo** - Rastreamento de todas as operações

## Notas Importantes

- O sistema valida automaticamente se há quantidade suficiente para saída
- Todas as operações são registradas com data e hora
- Os dados são persistidos em tempo real
- Suporta múltiplos motivos de entrada/saída

## Licença

Este projeto é de código aberto e pode ser usado livremente.
