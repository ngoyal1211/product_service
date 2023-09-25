from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Apples",
        "price": 1.99,
        "quantity": 100,
    },
    {
        "id": 2,
        "name": "Bananas",
        "price": 0.99,
        "quantity": 150,
    },
]

# Retrieve a list of available grocery products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Get details about a specific product by its unique ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

# Allow the addition of new grocery products to the inventory
@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"],
        "quantity": data["quantity"],
    }
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True)