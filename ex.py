from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory data structures
products = [
    {"id": 1, "name": "Laptop", "price": 800.00, "description": "High performance laptop", "stock": 10},
    {"id": 2, "name": "Smartphone", "price": 500.00, "description": "Latest model smartphone", "stock": 15},
    {"id": 3, "name": "Headphones", "price": 50.00, "description": "Noise-cancelling headphones", "stock": 20},
]
orders = []

# Routes
@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "Product not found", 404

    if 'cart' not in session:
        session['cart'] = {}

    cart = session['cart']
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {"name": product['name'], "price": product['price'], "quantity": 1}

    session['cart'] = cart
    return redirect(url_for('home'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        cart = session.get('cart', {})
        total_price = sum(item['price'] * item['quantity'] for item in cart.values())

        order = {
            "customer_name": customer_name,
            "customer_email": customer_email,
            "items": cart,
            "total_price": total_price
        }
        orders.append(order)
        session.pop('cart', None)
        return redirect(url_for('order_confirmation'))

    return render_template('checkout.html')

@app.route('/order_confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
