import time
import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/produtos', methods=['GET'])
def get_produtos():
    # Simula latência média de 50ms a 300ms para parecer realista
    time.sleep(random.uniform(0.05, 0.3))
    produtos = [
        {"id": 1, "nome": "Teclado Mecânico", "preco": 350.00},
        {"id": 2, "nome": "Mouse Gamer", "preco": 200.00},
        {"id": 3, "nome": "Monitor 144Hz", "preco": 1200.00}
    ]
    return jsonify(produtos)

@app.route('/produtos/id_destaque_123', methods=['GET'])
def get_produto_destaque():
    # Simula latência menor para o produto destacado (10ms a 50ms)
    time.sleep(random.uniform(0.01, 0.05))
    produto = {"id": 123, "nome": "Cadeira Gamer Premium", "preco": 1500.00}
    return jsonify(produto)

if __name__ == '__main__':
    print("Iniciando API Mock para testes de performance na porta 5000...")
    app.run(port=5000, debug=False)
