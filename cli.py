import argparse

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, FloatPrompt

from bot.orders import place_order
from bot.validaters import validate_side, validate_order_type

console = Console()

console.print(
    Panel.fit(
        "[bold cyan]🚀 Welcome to Binance Futures Testnet Trading Bot[/bold cyan]\n"
        "[green]Python Developer Assignment[/green]",
        border_style="blue",
    )
)

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument("--symbol")
parser.add_argument("--side")
parser.add_argument("--type")
parser.add_argument("--qty", type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

symbol = args.symbol or Prompt.ask(
    "[yellow]Trading Symbol[/yellow]",
    default="BTCUSDT"
)

side = args.side or Prompt.ask(
    "[yellow]Order Side[/yellow]",
    choices=["BUY", "SELL"],
)

order_type = args.type or Prompt.ask(
    "[yellow]Order Type[/yellow]",
    choices=["MARKET", "LIMIT"],
)

quantity = args.qty or FloatPrompt.ask(
    "[yellow]Quantity[/yellow]"
)

price = args.price

if order_type == "LIMIT" and price is None:
    price = FloatPrompt.ask("[yellow]Limit Price[/yellow]")

side = validate_side(side)
order_type = validate_order_type(order_type)

summary = Table(title="Order Request")

summary.add_column("Field", style="cyan")
summary.add_column("Value", style="green")

summary.add_row("Symbol", symbol)
summary.add_row("Side", side)
summary.add_row("Type", order_type)
summary.add_row("Quantity", str(quantity))

if order_type == "LIMIT":
    summary.add_row("Price", str(price))

console.print(summary)

response = place_order(
    symbol,
    side,
    order_type,
    quantity,
    price,
)

console.print()

if response.get("orderId"):

    console.print("[bold green]✓ Order Submitted Successfully[/bold green]")

    result = Table(title="Binance Response")

    result.add_column("Field", style="cyan")
    result.add_column("Value", style="magenta")

    result.add_row("Order ID", str(response.get("orderId")))
    result.add_row("Status", str(response.get("status")))
    result.add_row("Executed Qty", str(response.get("executedQty")))
    result.add_row("Average Price", str(response.get("avgPrice") or "N/A"))

    console.print(result)

else:
    console.print("[bold red]✗ Order Failed[/bold red]")