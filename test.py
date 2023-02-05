# TO DO:
#    - call get_price_for_volume of order_book.py
#    - update order book after construction


from hummingbot.connector.exchange.coinbase_pro.coinbase_pro_exchange import CoinbaseProExchange, OrderType
import asyncio
import os


cpe = CoinbaseProExchange({},
trading_pairs=['BTC-GBP'],
coinbase_pro_api_key=os.environ['coinbase_pro_api_key'], 
coinbase_pro_secret_key=os.environ['coinbase_pro_secret_key'],
coinbase_pro_passphrase=os.environ['coinbase_pro_passphrase']
)

cpe.buy("BTC-GBP", 0.0006, OrderType.LIMIT, price=13000)


# cpe.sell("BTC-GBP", 0.0006, OrderType.LIMIT, price=18000)


# # res = asyncio.get_event_loop().run_until_complete(cpe.cancel_all(3))

# res = asyncio.get_event_loop().run_until_complete(cpe.cancel_all(3))

# pass

# asyncio.get_event_loop().run_until_complete(cpe.start_network())


pass

