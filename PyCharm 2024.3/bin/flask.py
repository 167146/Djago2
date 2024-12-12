from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products
products = []

# POST /products - Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    if not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({'error': 'Missing fields in request'}), 400
    if not isinstance(data['price'], (int, float)):
        return jsonify({'error': 'Price must be a number'}), 400

    product = {
        'id': len(products) + 1,  # Auto-increment ID
        'name': data['name'],
        'description': data['description'],
        'price': data['price']
    }
    products.append(product)
    return jsonify(product), 201  # 201 Created

# GET /products - Retrieve a list of all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200  # 200 OK

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
