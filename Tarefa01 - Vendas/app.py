from flask import Flask, url_for, request, json, jsonify
from user import User
from product import Product
from sale import Sale
from json import dumps

app = Flask(__name__)
myUser = []
myProducts = []
mySales = []

@app.route('/')
def api_root():
    return 'Seja bem vindo!'

@app.route('/hello')
def api_hello(): #http://127.0.0.1:5000/hello?name=Paulo
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PATCH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE\n"

@app.route('/getuser', methods = ['GET'])
def api_getuser():
    global myUser
    user_data = request.get_json() #
    print(user_data)
    
    codUser = user_data['codigo']
    print(codUser)
    print(myUser[0].getUserNome())
    resU = {'status': 'Usuário nao encontrado!'}
    for elem in myUser:
        if(int(codUser) == elem.getUserId()):
            resU = {'nome': elem.getUserNome()}

    return jsonify(resU)

@app.route('/createuser')
def api_createuser():
    global myUser
    myUser.append(User(1, "Joao", 37, 4125875633))
    myUser.append(User(2, "Pedro", 43, 3698521474))
    myUser.append(User(3, "Jorge", 24, 2998524565))
    myUser.append(User(4, "Valdir", 31, 3126459789))
    myUser.append(User(5, "Antonio", 20, 4658527391))
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/insertuser', methods = ['POST'])
def insertUser():
    global myUser
    data = request.get_json()
    id = data['id']
    nome = data['nome']
    idade = data['idade']
    documento = data['documento'] 
    myUser.append(User(id, nome, idade, documento))
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/gettotalusers', methods = ['GET'])
def getTotalUsers():
    payload = []
    content = {}
    
    for u in myUser:        
        content = {'id': str(u.getUserId()),'[Nome]': u.getUserNome(), 
        '[Idade]': str(u.getUserIdade()), '[Documento]': u.getUserDoc()}
        payload.append(content)
        content = {}
    res =  json.dumps(payload)       
    return jsonify(ClientsList=res)

@app.route('/getuserid', methods = ['POST'])
def getUserId():
    global myUser
    data = request.get_json()
    print(myUser[0].getUserId())
    id = data['id']
    res = {'status': 'Usuario nao encontrado'}
    for u in myUser:
        if(int(id) == int(u.getUserId())):
            res = {'id': id, 'nome': u.getUserNome(), 'idade': u.getUserIdade(), 'documento': u.getUserDoc()}
    return jsonify(res)

@app.route('/createproducts', methods = ['GET'])
def createProducts():
    global myProducts 
    myProducts.append(Product(1, "Caderno", 9.99))
    myProducts.append(Product(2, "Caneta", 2.99))
    myProducts.append(Product(3, "Pacote de folhas", 9.99))
    myProducts.append(Product(4, "lapis e borracha", 5.99))
    myProducts.append(Product(5, "Mochila", 119.99))
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/insertproduct', methods = ['POST'])
def insertProduct():
    global myProducts
    data = request.get_json()
    id = data['id']
    nome = data['nome']
    preco = data['preco']
    myProducts.append(Product(id, nome, preco))
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/gettotalproducts', methods = ['GET'])
def getTotalProducts():
    payload = []
    content = {}
    for p in myProducts:        
        content = {'id': str(p.getProductId()),'[Nome]': p.getProductNome(), '[Preco]': str(p.getProductPreco())}
        payload.append(content)
        content = {}
    res =  json.dumps(payload)       
    return jsonify(ProductsList=res)

@app.route('/getproductid', methods = ['POST'])
def getProductId():
    global myProducts
    data = request.get_json()
    id = data['id']
    res = {'status': 'Produto nao encontrado'}
    for p in myProducts:
        if(int(id) == int(p.getProductId())):
            res = {'[Id]': id, '[Nome]': p.getProductNome(), '[Preco]': str(p.getProductPreco())}
    return jsonify(res)

@app.route('/insertsale', methods = ['POST'])
def insertSale():
    global mySales
    data = request.get_json()
    id = data['id']
    user = data['user']
    product = data['product']
    quantity = data['quantity'] 
    value = 0.00
    for p in myProducts:
        if(int(product) == int(p.getProductId())):
            value = float(p.getProductPreco()) * int(quantity)

    mySales.append(Sale(id, user, product, quantity, value))
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/getsales', methods = ['GET'])
def getSales():
    payload = []
    content = {}
    for s in mySales:        
        content = {'id': str(s.getSaleId()),'[Usuario]': str(s.getSaleUser()), 
        '[Produto]': str(s.getSaleProduct()), '[Quantidade]':str(s.getSaleQuantity()), '[Total]':str(s.getSaleTotal())}
        payload.append(content)
        content = {}
    res =  json.dumps(payload)   
    return jsonify(ProductsList=res)

@app.route('/gettotalusersid', methods=['POST'])
def getTotalUserId():
    global myUser, myProducts, mySales
    usuario = None
    Sales = []
    totalValue = 0

    data = request.get_json()
    id = data['id']

    for u in myUser:
        if(int(id) == int(u.getUserId())):
            usuario = u

    for s in Sales:
        if(int(id) == int(s.getSaleUser())):
            content = {'id' : s.getSaleId(), '[Produto]' : s.getSaleProduct(), '[Quantidade]' : s.getSaleQuantity(), '[Total]' : 'R$ ' + str(s.getSaleTotal())}
            Sales.append(content)
            totalValue += float(s.getSaleTotal())
    
    totalValue = round(totalValue, 2)
    res = json.dumps(Sales)
    return jsonify({'[Usuario]' : usuario.getUserNome(), '[Compras]' : res, '[Total Gasto pelo Usuario]' : 'R$ ' + str(totalValue)})

if __name__ == '__main__':
    app.run()