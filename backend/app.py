from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Product, Order

app= Flask(__name__)
CORS(app) # تمكين CROS للتواصل مع الواجهات
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLACJEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# جلب جميع المنتجات
@app.route('/api/producte', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        "id": p.id,
        "name" : p.name,
        "price": p.price,
        "stock": p.stock
    } for p in products])

# إنشاء طلب جديد
@app.route('/api/order', methods=['POST'])
def create_order():
    data = request.json
    new_order = Order(
        channel=data['channel'],
        total=data['total'],
        items=data['items']
    )
    db.session.add(new_order)

    # تحديث المخزون
    for item in data['items']:
        product = Product.query.get(item['product_id'])
        product.stock -= item['quantity']
    db.session.commit()

    return jsonify({"message": "تم إنشاء الطلب بنجاح!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # إنشاء الجداول إذا لم تكن موجودة
    app.run(debug=True)