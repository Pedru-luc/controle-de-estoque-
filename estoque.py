import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class Produto:
    """Representa um produto no estoque"""
    def __init__(self, codigo: str, nome: str, preco: float, quantidade: int = 0):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def to_dict(self) -> Dict:
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'preco': self.preco,
            'quantidade': self.quantidade
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Produto':
        return Produto(data['codigo'], data['nome'], data['preco'], data['quantidade'])


class Movimentacao:
    """Representa uma movimentação (entrada ou saída) no estoque"""
    def __init__(self, tipo: str, codigo_produto: str, quantidade: int, motivo: str = ""):
        self.tipo = tipo  # 'entrada' ou 'saida'
        self.codigo_produto = codigo_produto
        self.quantidade = quantidade
        self.motivo = motivo
        self.data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def to_dict(self) -> Dict:
        return {
            'tipo': self.tipo,
            'codigo_produto': self.codigo_produto,
            'quantidade': self.quantidade,
            'motivo': self.motivo,
            'data': self.data
        }


class ControleEstoque:
    """Gerencia o controle de estoque"""
    
    def __init__(self, arquivo_dados: str = 'estoque.json'):
        self.arquivo_dados = arquivo_dados
        self.produtos: Dict[str, Produto] = {}
        self.movimentacoes: List[Movimentacao] = []
        self.carregar_dados()
    
    def carregar_dados(self):
        """Carrega dados do arquivo JSON"""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    for prod in dados.get('produtos', []):
                        p = Produto.from_dict(prod)
                        self.produtos[p.codigo] = p
                    for mov in dados.get('movimentacoes', []):
                        m = Movimentacao(
                            mov['tipo'],
                            mov['codigo_produto'],
                            mov['quantidade'],
                            mov.get('motivo', '')
                        )
                        m.data = mov['data']
                        self.movimentacoes.append(m)
            except Exception as e:
                print(f"Erro ao carregar dados: {e}")
    
    def salvar_dados(self):
        """Salva dados no arquivo JSON"""
        dados = {
            'produtos': [p.to_dict() for p in self.produtos.values()],
            'movimentacoes': [m.to_dict() for m in self.movimentacoes]
        }
        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
    
    def adicionar_produto(self, codigo: str, nome: str, preco: float, quantidade: int = 0) -> bool:
        """Adiciona um novo produto ao estoque"""
        if codigo in self.produtos:
            print(f"❌ Erro: Produto com código '{codigo}' já existe!")
            return False
        
        self.produtos[codigo] = Produto(codigo, nome, preco, quantidade)
        self.salvar_dados()
        print(f"✓ Produto '{nome}' adicionado com sucesso!")
        return True
    
    def entrada_estoque(self, codigo: str, quantidade: int, motivo: str = "Compra") -> bool:
        """Registra uma entrada no estoque"""
        if codigo not in self.produtos:
            print(f"❌ Erro: Produto com código '{codigo}' não encontrado!")
            return False
        
        if quantidade <= 0:
            print("❌ Erro: Quantidade deve ser maior que zero!")
            return False
        
        self.produtos[codigo].quantidade += quantidade
        mov = Movimentacao('entrada', codigo, quantidade, motivo)
        self.movimentacoes.append(mov)
        self.salvar_dados()
        print(f"✓ Entrada registrada: +{quantidade} unidades de '{self.produtos[codigo].nome}'")
        return True
    
    def saida_estoque(self, codigo: str, quantidade: int, motivo: str = "Venda") -> bool:
        """Registra uma saída do estoque"""
        if codigo not in self.produtos:
            print(f"❌ Erro: Produto com código '{codigo}' não encontrado!")
            return False
        
        if quantidade <= 0:
            print("❌ Erro: Quantidade deve ser maior que zero!")
            return False
        
        if self.produtos[codigo].quantidade < quantidade:
            print(f"❌ Erro: Quantidade insuficiente! Disponível: {self.produtos[codigo].quantidade}")
            return False
        
        self.produtos[codigo].quantidade -= quantidade
        mov = Movimentacao('saida', codigo, quantidade, motivo)
        self.movimentacoes.append(mov)
        self.salvar_dados()
        print(f"✓ Saída registrada: -{quantidade} unidades de '{self.produtos[codigo].nome}'")
        return True
    
    def listar_produtos(self):
        """Lista todos os produtos do estoque"""
        if not self.produtos:
            print("📦 Nenhum produto cadastrado.")
            return
        
        print("\n" + "="*80)
        print(f"{'Código':<12} {'Nome':<25} {'Preço':<12} {'Quantidade':<12} {'Total':<12}")
        print("="*80)
        
        for produto in self.produtos.values():
            total = produto.preco * produto.quantidade
            print(f"{produto.codigo:<12} {produto.nome:<25} R${produto.preco:<11.2f} {produto.quantidade:<12} R${total:<11.2f}")
        
        print("="*80)
        valor_total = sum(p.preco * p.quantidade for p in self.produtos.values())
        print(f"{'Valor total do estoque: R$' + f'{valor_total:.2f}':>80}")
        print()
    
    def listar_movimentacoes(self, codigo_produto: Optional[str] = None, limite: int = 20):
        """Lista as movimentações do estoque"""
        movs = self.movimentacoes
        
        if codigo_produto:
            movs = [m for m in movs if m.codigo_produto == codigo_produto]
        
        if not movs:
            print("📝 Nenhuma movimentação registrada.")
            return
        
        # Pega os últimos movimentos
        movs = movs[-limite:]
        
        print("\n" + "="*90)
        print(f"{'Data':<20} {'Tipo':<10} {'Produto':<12} {'Quantidade':<12} {'Motivo':<20}")
        print("="*90)
        
        for mov in movs:
            tipo_formatado = "⬆ ENTRADA" if mov.tipo == 'entrada' else "⬇ SAÍDA"
            print(f"{mov.data:<20} {tipo_formatado:<10} {mov.codigo_produto:<12} {mov.quantidade:<12} {mov.motivo:<20}")
        
        print("="*90 + "\n")
    
    def obter_produto(self, codigo: str) -> Optional[Produto]:
        """Obtém informações de um produto"""
        return self.produtos.get(codigo)
    
    def relatorio_estoque(self):
        """Gera um relatório completo do estoque"""
        print("\n" + "="*80)
        print("RELATÓRIO DE ESTOQUE".center(80))
        print("="*80)
        print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Total de produtos: {len(self.produtos)}")
        print(f"Total de movimentações: {len(self.movimentacoes)}")
        print("="*80 + "\n")
        
        self.listar_produtos()


def menu():
    """Interface de menu principal"""
    estoque = ControleEstoque()
    
    while True:
        print("\n" + "="*50)
        print("CONTROLE DE ESTOQUE".center(50))
        print("="*50)
        print("1. Adicionar produto")
        print("2. Entrada de estoque")
        print("3. Saída de estoque")
        print("4. Listar produtos")
        print("5. Listar movimentações")
        print("6. Informações de um produto")
        print("7. Relatório completo")
        print("8. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção (1-8): ").strip()
        
        if opcao == '1':
            codigo = input("Código do produto: ").strip()
            nome = input("Nome do produto: ").strip()
            try:
                preco = float(input("Preço do produto: R$ "))
                quantidade = int(input("Quantidade inicial: "))
                estoque.adicionar_produto(codigo, nome, preco, quantidade)
            except ValueError:
                print("❌ Erro: Valores inválidos!")
        
        elif opcao == '2':
            codigo = input("Código do produto: ").strip()
            try:
                quantidade = int(input("Quantidade para entrada: "))
                motivo = input("Motivo (Compra/Devolução/etc): ").strip() or "Compra"
                estoque.entrada_estoque(codigo, quantidade, motivo)
            except ValueError:
                print("❌ Erro: Quantidade inválida!")
        
        elif opcao == '3':
            codigo = input("Código do produto: ").strip()
            try:
                quantidade = int(input("Quantidade para saída: "))
                motivo = input("Motivo (Venda/Perda/etc): ").strip() or "Venda"
                estoque.saida_estoque(codigo, quantidade, motivo)
            except ValueError:
                print("❌ Erro: Quantidade inválida!")
        
        elif opcao == '4':
            estoque.listar_produtos()
        
        elif opcao == '5':
            codigo = input("Código do produto (deixe em branco para todos): ").strip()
            try:
                limite = int(input("Número de movimentações a exibir (padrão: 20): ") or "20")
                estoque.listar_movimentacoes(codigo or None, limite)
            except ValueError:
                estoque.listar_movimentacoes(codigo or None, 20)
        
        elif opcao == '6':
            codigo = input("Código do produto: ").strip()
            produto = estoque.obter_produto(codigo)
            if produto:
                print(f"\n✓ Produto encontrado:")
                print(f"  Código: {produto.codigo}")
                print(f"  Nome: {produto.nome}")
                print(f"  Preço: R$ {produto.preco:.2f}")
                print(f"  Quantidade: {produto.quantidade} unidades")
                print(f"  Valor total: R$ {produto.preco * produto.quantidade:.2f}\n")
            else:
                print("❌ Produto não encontrado!")
        
        elif opcao == '7':
            estoque.relatorio_estoque()
        
        elif opcao == '8':
            print("👋 Encerrando o programa... Até logo!")
            break
        
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
