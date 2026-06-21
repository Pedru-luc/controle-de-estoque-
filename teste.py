"""
Script de teste para demonstrar o uso do sistema de controle de estoque
"""

from estoque import ControleEstoque

def teste_rapido():
    """Executa um teste rápido do sistema"""
    
    print("="*60)
    print("TESTE RÁPIDO DO SISTEMA DE CONTROLE DE ESTOQUE")
    print("="*60)
    
    # Carrega os dados existentes
    estoque = ControleEstoque()
    
    # 1. Lista todos os produtos
    print("\n1. LISTANDO TODOS OS PRODUTOS:")
    estoque.listar_produtos()
    
    # 2. Obtém informações de um produto específico
    print("2. INFORMAÇÕES DO PRODUTO P001:")
    produto = estoque.obter_produto("P001")
    if produto:
        print(f"   Nome: {produto.nome}")
        print(f"   Quantidade em estoque: {produto.quantidade}")
        print(f"   Preço unitário: R$ {produto.preco:.2f}")
        print(f"   Valor total: R$ {produto.preco * produto.quantidade:.2f}")
    
    # 3. Registra uma entrada
    print("\n3. REGISTRANDO ENTRADA:")
    estoque.entrada_estoque("P001", 25, "Reposição")
    
    # 4. Registra uma saída
    print("\n4. REGISTRANDO SAÍDA:")
    estoque.saida_estoque("P002", 3, "Venda Online")
    
    # 5. Mostra o novo estado do produto
    print("\n5. NOVO ESTADO DO ESTOQUE:")
    estoque.listar_produtos()
    
    # 6. Lista movimentações recentes
    print("\n6. ÚLTIMAS MOVIMENTAÇÕES:")
    estoque.listar_movimentacoes(limite=5)
    
    # 7. Movimentações de um produto específico
    print("7. MOVIMENTAÇÕES DO PRODUTO P001:")
    estoque.listar_movimentacoes(codigo_produto="P001", limite=10)
    
    # 8. Relatório completo
    print("8. RELATÓRIO COMPLETO:")
    estoque.relatorio_estoque()
    
    print("\n" + "="*60)
    print("TESTE CONCLUÍDO COM SUCESSO!")
    print("="*60)


if __name__ == "__main__":
    teste_rapido()
