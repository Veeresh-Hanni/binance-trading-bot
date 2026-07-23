# Binance Futures Testnet Trading Bot

A Python CLI application that places **Market** and **Limit** orders on the **Binance Futures Testnet (USDT-M)**.

This project was developed as part of the Python Developer application task.

---

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports both **BUY** and **SELL**
- Command-line interface using `argparse`
- Input validation
- Structured project architecture
- Logging of API requests, responses, and errors
- Exception handling for invalid input, API errors, and network failures
- Uses Binance Futures Testnet

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── exceptions.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── config.py
├── .env
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.10+
- Binance Futures Testnet Account
- API Key
- API Secret

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/trading_bot.git

cd trading_bot
```

### Create Virtual Environment

Windows

```bash
python -m venv pyvenv

pyvenv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv pyvenv

source pyvenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Keys

Create a `.env` file in the project root.

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
API_SECRET=YOUR_BINANCE_TESTNET_API_SECRET
```

---

## Binance Futures Testnet

Register for the Binance Futures Testnet.

Generate your API Key and Secret.

Base URL

```
https://testnet.binancefuture.com
```

---

## Usage

### Market Buy Order

```bash
python cli.py \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--qty 0.001
```

### Market Sell Order

```bash
python cli.py \
--symbol BTCUSDT \
--side SELL \
--type MARKET \
--qty 0.001
```

### Limit Buy Order

```bash
python cli.py \
--symbol BTCUSDT \
--side BUY \
--type LIMIT \
--qty 0.001 \
--price 100000
```

### Limit Sell Order

```bash
python cli.py \
--symbol BTCUSDT \
--side SELL \
--type LIMIT \
--qty 0.001 \
--price 120000
```

---

## Sample Output

```
Order Request Summary

Symbol : BTCUSDT
Side : BUY
Order Type : MARKET
Quantity : 0.001

Order Response

Order ID : 123456789
Status : FILLED
Executed Qty : 0.001
Average Price : 115320.45

Order placed successfully.
```

---

## Logging

Every API request, response, and error is stored in:

```
logs/trading.log
```

Example:

```
2026-07-23 09:42:15 INFO REQUEST:
{
    "symbol":"BTCUSDT",
    "side":"BUY",
    "type":"MARKET",
    "quantity":0.001
}

2026-07-23 09:42:16 INFO RESPONSE:
{
    "orderId":12345678,
    "status":"FILLED",
    "executedQty":"0.001"
}
```

---

## Error Handling

The application handles:

- Invalid symbol
- Invalid side
- Invalid order type
- Missing price for LIMIT orders
- Invalid quantity
- Binance API errors
- Network failures
- Authentication errors

---

## Dependencies

- python-binance
- python-dotenv

Install using

```bash
pip install -r requirements.txt
```

---

## Assumptions

- API credentials belong to the Binance Futures Testnet.
- Testnet account is activated.
- Sufficient virtual balance is available.
- Internet connection is available.
- Quantity and price satisfy Binance trading rules.

---

## Future Improvements

- Stop-Limit orders
- OCO orders
- Grid strategy
- TWAP execution
- Rich CLI interface
- Interactive menu
- Unit tests
- Docker support
- Configuration via YAML
- Order history
- Position management

---

## Author

**Veeresh Hanni**

Python Developer Assignment