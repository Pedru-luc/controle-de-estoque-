from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from estoque import ControleEstoque
import importlib.util
import os
import pkgutil
from pathlib import Path

if not hasattr(pkgutil, 'get_loader'):
    def get_loader(name):
        spec = importlib.util.find_spec(name)
        return spec.loader if spec else None
    pkgutil.get_loader = get_loader

app = Flask(Path(__file__).stem, static_folder='.', static_url_path='')
CORS(app)

estoque = ControleEstoque()


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/instrucoes')
def instrucoes():
    return send_from_directory('.', 'instrucoes.html')


@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    produtos = [produto.to_dict() for produto in estoque.produtos.values()]
    valor_total = sum(p['preco'] * p['quantidade'] for p in produtos)
    return jsonify({
        'sucesso': True,
        'produtos': produtos,
        'valor_total': valor_total,
        'quantidade_produtos': len(produtos)
    })


@app.route('/api/produtos/<codigo>', methods=['GET'])
def get_produto(codigo):
    produto = estoque.obter_produto(codigo)
    if produto:
        return jsonify({'sucesso': True, 'produto': produto.to_dict()})
    return jsonify({'sucesso': False, 'erro': f'Produto {codigo} não encontrado'}), 404


@app.route('/api/produtos', methods=['POST'])
def adicionar_produto():
    dados = request.json or {}
    codigo = dados.get('codigo', '').strip()
    nome = dados.get('nome', '').strip()
    preco = dados.get('preco')
    quantidade = dados.get('quantidade', 0)

    if not codigo or not nome or preco is None:
        return jsonify({'sucesso': False, 'erro': 'Código, nome e preço são obrigatórios'}), 400

    try:
        preco = float(preco)
        quantidade = int(quantidade)
    except ValueError:
        return jsonify({'sucesso': False, 'erro': 'Preço ou quantidade inválidos'}), 400

    sucesso = estoque.adicionar_produto(codigo, nome, preco, quantidade)
    if sucesso:
        return jsonify({'sucesso': True, 'mensagem': f"Produto '{nome}' adicionado com sucesso!"})

    return jsonify({'sucesso': False, 'erro': f"Produto com código '{codigo}' já existe"}), 400


@app.route('/api/entrada', methods=['POST'])
def registrar_entrada():
    dados = request.json or {}
    codigo = dados.get('codigo', '').strip()
    quantidade = dados.get('quantidade')
    motivo = dados.get('motivo', 'Compra').strip() or 'Compra'

    if not codigo or quantidade is None:
        return jsonify({'sucesso': False, 'erro': 'Código e quantidade são obrigatórios'}), 400

    try:
        quantidade = int(quantidade)
    except ValueError:
        return jsonify({'sucesso': False, 'erro': 'Quantidade inválida'}), 400

    sucesso = estoque.entrada_estoque(codigo, quantidade, motivo)
    if sucesso:
        produto = estoque.obter_produto(codigo)
        return jsonify({
            'sucesso': True,
            'mensagem': f"Entrada registrada: +{quantidade} unidades",
            'nova_quantidade': produto.quantidade
        })

    return jsonify({'sucesso': False, 'erro': 'Erro ao registrar entrada'}), 400


@app.route('/api/saida', methods=['POST'])
def registrar_saida():
    dados = request.json or {}
    codigo = dados.get('codigo', '').strip()
    quantidade = dados.get('quantidade')
    motivo = dados.get('motivo', 'Venda').strip() or 'Venda'

    if not codigo or quantidade is None:
        return jsonify({'sucesso': False, 'erro': 'Código e quantidade são obrigatórios'}), 400

    try:
        quantidade = int(quantidade)
    except ValueError:
        return jsonify({'sucesso': False, 'erro': 'Quantidade inválida'}), 400

    sucesso = estoque.saida_estoque(codigo, quantidade, motivo)
    if sucesso:
        produto = estoque.obter_produto(codigo)
        return jsonify({
            'sucesso': True,
            'mensagem': f"Saída registrada: -{quantidade} unidades",
            'nova_quantidade': produto.quantidade
        })

    return jsonify({'sucesso': False, 'erro': 'Quantidade insuficiente ou produto não encontrado'}), 400


@app.route('/api/movimentacoes', methods=['GET'])
def get_movimentacoes():
    codigo = request.args.get('codigo', '').strip()
    limite = request.args.get('limite', 50)

    try:
        limite = int(limite)
    except ValueError:
        limite = 50

    movs = estoque.movimentacoes
    if codigo:
        movs = [m for m in movs if m.codigo_produto == codigo]

    movs = movs[-limite:]
    return jsonify({'sucesso': True, 'movimentacoes': [m.to_dict() for m in movs], 'total': len(movs)})


@app.route('/api/relatorio', methods=['GET'])
def get_relatorio():
    produtos = [produto.to_dict() for produto in estoque.produtos.values()]
    valor_total = sum(p['preco'] * p['quantidade'] for p in produtos)
    return jsonify({
        'sucesso': True,
        'total_produtos': len(produtos),
        'valor_total': valor_total,
        'total_movimentacoes': len(estoque.movimentacoes),
        'produtos': produtos
    })


@app.route('/api/deletar/<codigo>', methods=['DELETE'])
def deletar_produto(codigo):
    if codigo in estoque.produtos:
        del estoque.produtos[codigo]
        estoque.salvar_dados()
        return jsonify({'sucesso': True, 'mensagem': f'Produto {codigo} deletado com sucesso'})
    return jsonify({'sucesso': False, 'erro': f'Produto {codigo} não encontrado'}), 404


@app.route('/api/editar/<codigo>', methods=['PUT'])
def editar_produto(codigo):
    dados = request.json or {}
    produto = estoque.obter_produto(codigo)
    if not produto:
        return jsonify({'sucesso': False, 'erro': 'Produto não encontrado'}), 404

    nome = dados.get('nome')
    preco = dados.get('preco')

    if nome:
        produto.nome = str(nome).strip()
    if preco is not None:
        try:
            produto.preco = float(preco)
        except ValueError:
            return jsonify({'sucesso': False, 'erro': 'Preço inválido'}), 400

    estoque.salvar_dados()
    return jsonify({'sucesso': True, 'mensagem': 'Produto atualizado com sucesso', 'produto': produto.to_dict()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
