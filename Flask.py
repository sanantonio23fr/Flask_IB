from flask import Flask, request, jsonify

app = Flask(__name__)

# Clé secrète pour valider les webhooks
SECRET_KEY = "Amt/YXJFm4nomICA+4fYn1MJbkTvlP6D"

@app.route('/webhook', methods=['POST'])
def webhook():
    # Vérification de la clé secrète
    auth_header = request.headers.get('Authorization')
    if auth_header != f"Bearer {SECRET_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    # Récupérer les données JSON envoyées par le webhook
    data = request.json
    symbol = data.get('symbol')
    action = data.get('action')
    quantity = data.get('quantity')
    price = data.get('price')

    # Traitement de la commande (à personnaliser)
    print(f"Reçu : {action} {quantity} de {symbol} à {price}")

    return jsonify({"status": "success", "message": "Ordre reçu"})

if __name__ == '__main__':
    app.run(debug=True)