from bot.client import client
from bot.logging_conf import logger


def place_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None,
):
    try:

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":

            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"REQUEST {params}")

        response = client.futures_create_order(**params)

        logger.info(f"RESPONSE {response}")

        return response

    except Exception as e:

        logger.exception(e)
        raise