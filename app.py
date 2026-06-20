#imp frameworks

from flask import Flask, jsonify, request
from flask_cors import CORS 

#criar app 
app = Flask(__name__)
#habilitar cors
CORS(app)

#criando banco de dados local 
produtos = [
    {"id":1, 
     "nome":"Notebook Gamer",
     "preco": 4000
     },
    {"id":2, 
     "nome":"Cadeira Gamer",
     "preco": 300 
     },
    {"id":3, 
     "nome":"Monitor Gamer",
     "preco": 500 
     },
    {"id":4, 
     "nome":"Gabinete Gamer",
     "preco": 350 
     },  
    {"id":5, 
     "nome":"Teclado Gamer",
     "preco": 256
     },
    {"id":6, 
     "nome":"Mouse Gamer",
     "preco": 200 
     }
] 

#criar uma rota
@app.route("/listar", methods=['GET'])
def exibirProdutos():
    return jsonify(produtos)

#Criar uma roda e o método post (criar)
@app.route("/criar", methods=['POST'])
def criarProdutos():
    produtoNovo = request.get_json()
    produtos.append(produtoNovo)
    return jsonify(produtoNovo), 201

#criar uma roda e  método put (atualizar)
@app.route("/atualizar/<int:id>", methods=['PUT'])
def atualizarProdutos(id):
    dados = request.get_json()
    for produto in produtos:
        if produto['id'] == id:
            produto['preco'] = dados['preco']
            return jsonify(dados)
    return jsonify({"mensagem":"ID não encontrado"}), 404 

#criar uma roda e método delete (deletar)
@app.route("/apagar/<int:id>", methods=['DELETE'])
def apagarProdutos(id):
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            return jsonify({"mensagem": "Produto removido com sucesso!"})
    return jsonify({"mensagem": "ID não encontrado "}), 404

#rodar o programa
if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0")