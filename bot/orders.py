from bot.client import client, get_async_client
from bot.logging_conf import logger
from binance.exceptions import BinanceAPIException
from requests.exceptions import RequestException


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

    except BinanceAPIException as e:
        logger.exception(e)
        print(f"\n❌ Binance API Error ({e.code}): {e.message}")
        return None

    except RequestException as e:
        logger.exception(e)
        print(f"\n❌ Network Error: {e}")
        return None

    except Exception as e:
        logger.exception(e)
        print(f"\n❌ Unexpected Error: {e}")
        return None

async def async_place_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None,
):
    client = await get_async_client()
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

        response = await client.futures_create_order(**params)

        logger.info(f"RESPONSE {response}")

        return response

    except BinanceAPIException as e:
        logger.exception(e)
        print(f"\n❌ Binance API Error ({e.code}): {e.message}")
        return None

    except RequestException as e:
        logger.exception(e)
        print(f"\n❌ Network Error: {e}")
        return None

    except Exception as e:
        logger.exception(e)
        print(f"\n❌ Unexpected Error: {e}")
        return None
    finally:
        await client.close_connection()