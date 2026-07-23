# Binance Futures Testnet Trading Bot

A Python CLI application that places **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**.

This project was developed as part of the **Primetrade.ai Computer Science (Foundations) - Internship Application Task**.

---

## Features

- ✅ Place **MARKET** orders
- ✅ Place **LIMIT** orders
- ✅ Supports both **BUY** and **SELL**
- ✅ Command-line interface (CLI) using `argparse`
- ✅ Interactive CLI prompts using `rich`
- ✅ Input validation
- ✅ Structured and reusable codebase
- ✅ Logging of API requests, responses, and errors
- ✅ Exception handling for invalid input, API errors, and network failures
- ✅ Binance Futures Testnet integration

---

## Project Structure

```text
binance-trading-bot/
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
├── .env
├── .gitignore
├── cli.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.10 or later
- Binance Futures Testnet account
- Binance Futures Testnet API Key
- Binance Futures Testnet API Secret

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Veeresh-Hanni/binance-trading-bot.git

cd binance-trading-bot
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv pyvenv

pyvenv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv pyvenv

source pyvenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Credentials

Create a `.env` file in the project root.

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
API_SECRET=YOUR_BINANCE_TESTNET_API_SECRET
```

---

## Binance Futures Testnet

Register for a Binance Futures Testnet account and generate your API credentials.

**Base URL**

```text
https://testnet.binancefuture.com
```

---

## Usage

### Interactive Mode

Run the application and follow the prompts.

```bash
python cli.py
```

### MARKET Buy Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

### MARKET Sell Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --qty 0.001
```

### LIMIT Buy Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.001 --price 100000
```

### LIMIT Sell Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 120000
```

---

## Sample Output

```text
╭──────────────────────────────────────────────╮
│ 🚀 Welcome to Binance Futures Testnet Bot    │
│ Python Developer Assignment                  │
╰──────────────────────────────────────────────╯

Order Summary
----------------

Order ID      : 23491720045
Status        : NEW
Executed Qty  : 0.0000
Average Price : N/A
```

---

## Logging

All API requests, responses, and errors are logged to:

```text
logs/trading.log
```

Example:

```text
2026-07-23 09:42:15 INFO REQUEST:
{
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "MARKET",
    "quantity": 0.001
}

2026-07-23 09:42:16 INFO RESPONSE:
{
    "orderId": 23491720045,
    "status": "NEW",
    "executedQty": "0.0000"
}
```

---

## Error Handling

The application handles:

- Invalid trading symbol
- Invalid order side
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
- rich
- requests

Install using:

```bash
pip install -r requirements.txt
```

> **Note:** `asyncio` is included in Python's standard library and does not need to be installed separately.

---

## Assumptions

- API credentials are generated from the Binance Futures Testnet.
- The Testnet account is active.
- Sufficient virtual balance is available.
- Internet connectivity is available.
- Quantity and price satisfy Binance Futures trading rules.

---

## Future Improvements

- Stop-Limit orders
- OCO orders
- Grid trading strategy
- TWAP execution
- Interactive menu system
- Docker support
- Unit tests
- YAML configuration
- Order history
- Position management dashboard

---

## Author

**Veeresh Hanni**

Computer Science (Foundations) - Internship Assignment – Primetrade.ai
