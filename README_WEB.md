# Interface Web - Controle de Estoque

Interface HTML moderna e responsiva para o sistema de controle de estoque.

## Instalação

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Iniciar o servidor

```bash
python app.py
```

O servidor iniciará em `http://localhost:5000`

### 3. Abrir a interface

Abra a interface pelo servidor Flask em:
```bash
http://localhost:5000
```

Se quiser acessar no celular, use o IP do computador na rede local:
```bash
http://<IP-do-PC>:5000
```

## Funcionalidades da Interface

### 📊 Aba Estoque
- Visualiza todos os produtos em cards interativos
- Exibe quantidade, preço e valor total de cada produto
- Botões rápidos para entrada/saída de produtos
- Editar e deletar produtos

### 🏷️ Aba Produtos
- Adicionar novos produtos
- Tabela com todos os produtos
- Filtros e buscas rápidas
- Gerenciamento completo

### 📝 Aba Movimentações
- Histórico de todas as entradas e saídas
- Filtrar por código de produto
- Visualizar motivos e datas
- Últimas 100 movimentações

### 📈 Aba Relatório
- Resumo completo do estoque
- Valor total do estoque
- Tabela detalhada de todos os produtos
- Exportar para PDF

## Recursos

✅ **Interface Responsiva** - Funciona em desktop, tablet e celular  
✅ **Design Moderno** - Cores profissionais e animações suaves  
✅ **Validações** - Verifica dados antes de enviar  
✅ **Alertas em Tempo Real** - Feedback visual de ações  
✅ **Modal de Operações** - Diálogo para entrada/saída  
✅ **Estatísticas ao Vivo** - Atualiza automaticamente  

## Estrutura

```
📁 piton/
├── estoque.py          # Classes do sistema
├── app.py              # API Flask
├── index.html          # Interface web
├── estoque.json        # Dados persistidos
├── requirements.txt    # Dependências
└── README_WEB.md       # Este arquivo
```

## Como Usar

### Adicionar Produto
1. Vá para "🏷️ Produtos"
2. Preencha o formulário (Código, Nome, Preço, Quantidade)
3. Clique em "Adicionar Produto"

### Registrar Entrada
1. Clique no botão "➕ Entrada" do produto
2. Digite a quantidade e motivo
3. Confirme

### Registrar Saída
1. Clique no botão "➖ Saída" do produto
2. Digite a quantidade e motivo
3. Confirme

### Ver Movimentações
1. Vá para "📝 Movimentações"
2. Veja o histórico completo
3. Filtre por código de produto (opcional)

### Gerar Relatório
1. Vá para "📈 Relatório"
2. Visualize as informações
3. Clique em "📄 Exportar PDF" para imprimir

## Troubleshooting

**Erro: "Não consegue se conectar ao servidor"**
- Certifique-se de que `app.py` está rodando
- Verifique se a porta 5000 está disponível

**Erro: "ModuleNotFoundError: No module named 'flask'"**
- Execute: `pip install -r requirements.txt`

**Dados não aparecem**
- Verifique se `estoque.json` existe no mesmo diretório
- Recarregue a página (F5)

## API Endpoints

- `GET /api/produtos` - Lista todos os produtos
- `POST /api/produtos` - Adiciona novo produto
- `POST /api/entrada` - Registra entrada
- `POST /api/saida` - Registra saída
- `GET /api/movimentacoes` - Lista movimentações
- `GET /api/relatorio` - Gera relatório
- `DELETE /api/deletar/<codigo>` - Deleta produto
- `PUT /api/editar/<codigo>` - Edita produto

## Notas

- Todos os dados são salvos automaticamente em JSON
- A interface se atualiza em tempo real
- Suporta múltiplos usuários (qualquer um com acesso à URL)
- Não requer banco de dados

## Próximas Melhorias

- [ ] Login e autenticação
- [ ] Gráficos e estatísticas avançadas
- [ ] Backup automático
- [ ] Notificações de produtos com pouco estoque
- [ ] Integração com código de barras
- [ ] Relatórios em Excel/PDF avançados
