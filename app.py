from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets"

@app.route("/signal")
def get_signal():
    params = {
        'vs_currency': 'usd',
        'order': 'volume_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False
    }
    response = requests.get(COINGECKO_URL, params=params)
    data = response.json()

    top_token = data[0]
    symbol = top_token['symbol'].upper()
    price = top_token['current_price']
    volume = top_token['total_volume']
    logo = top_token['image']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    signal = {
        'token': symbol,
        'price': price,
        'volume': volume,
        'logo': logo,
        'direction': 'PICO VOLUMEN - Analizar si es LONG o SHORT',
        'hora_miami': timestamp
    }

    return jsonify(signal)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
