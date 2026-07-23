import argparse

from bot.orders import place_order
from bot.validaters import *

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--qty", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

side = validate_side(args.side)

order_type = validate_order_type(args.type)

response = place_order(
    args.symbol,
    side,
    order_type,
    args.qty,
    args.price,
)

print(response)
print()

print("Order Summary")

print("----------------")

print(f"Order ID : {response.get('orderId',0)}")

print(f"Status : {response.get('status', None)}")

print(f"Executed Qty : {response.get('executedQty', None)}")

print(f"Avg Price : {response.get('avgPrice', 0)}")