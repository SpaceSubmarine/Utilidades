import requests
import time

# Nuestro saldo actual en dólares
balance = 1000

# Nuestra cantidad actual de BTC
btc = 0

# La cantidad mínima de BTC que queremos tener en nuestra cartera
min_btc = 0.01

# La cantidad máxima de BTC que queremos tener en nuestra cartera
max_btc = 1

# El porcentaje máximo de nuestro balance que estamos dispuestos a invertir en BTC
max_investment_percentage = 0.5

# La cantidad mínima de dólares que queremos tener en nuestra cartera
min_balance = 100

# La API de precios de Bitcoin
price_api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

# Nuestro objetivo de ganancias diarias en dólares
daily_profit_target = 50

# Bucle infinito para seguir operando
while True:
    # Obtenemos el precio actual de Bitcoin en dólares
    price_response = requests.get(price_api_url)
    price_data = price_response.json()
    current_price = float(price_data["bpi"]["USD"]["rate_float"])

    # Calculamos la cantidad máxima de BTC que podemos comprar con nuestro saldo actual
    max_btc_to_buy = balance * max_investment_percentage / current_price

    # Si tenemos menos BTC de lo que queremos, compramos BTC hasta llegar a nuestro objetivo
    if btc < min_btc:
        btc_to_buy = min_btc - btc
        btc_to_buy = min(btc_to_buy, max_btc_to_buy)
        cost = btc_to_buy * current_price
        balance -= cost
        btc += btc_to_buy
        print(f"Comprados {btc_to_buy:.4f} BTC por un costo de ${cost:.2f}. Saldo actual: ${balance:.2f}")

    # Si tenemos más BTC de lo que queremos, vendemos BTC hasta llegar a nuestro objetivo
    elif btc > max_btc:
        btc_to_sell = btc - max_btc
        earnings = btc_to_sell * current_price
        balance += earnings
        btc -= btc_to_sell
        print(f"Vendidos {btc_to_sell:.4f} BTC por una ganancia de ${earnings:.2f}. Saldo actual: ${balance:.2f}")

    # Si
