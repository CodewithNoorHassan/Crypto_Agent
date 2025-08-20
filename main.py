import requests
from agents import Agent, Runner, function_tool
from connection import config

# ----------------Get Coin Price----------------
@function_tool
def get_crypto_price(symbol: str):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    data = requests.get(url).json()
    # Binance hamesha 'symbol' aur 'price' return karta hai
    return f"1 {data['symbol']} = {data['price']} USD"

# ---------------Crypto Agent------------------
agent = Agent(
    name="Crypto Agent",
    instructions="You are a crypto agent. Fetch real-time crypto prices from Binance API.",
    tools=[get_crypto_price]
)

# ----------------Run the agent------------------
result = Runner.run_sync(
    agent,
    "What is the price of BTCUSDT?",
    run_config=config
)

print(result.final_output)
