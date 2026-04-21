from typing import List, Dict, Any

def build_currency_map(currencies):
    return {
        item["iso_code"]: {
            "name": item["name"],
            "symbol": item["symbol"]
        }
        for item in currencies
    }

def transform_exchange_rates(
    data: List[Dict[str, Any]],
    currency_map: Dict[str, Dict[str, str]]
) -> List[Dict[str, Any]]:
    """
    Aplica cálculos analíticos considerando múltiplas moedas.
    """

    grouped = {}

    for item in data:
        quote = item["quote"]
        grouped.setdefault(quote, []).append(item)

    result = []

    for quote, items in grouped.items():
        currency_info = currency_map.get(quote, {})
        base_info = currency_map.get(item["base"], {})

        items = sorted(items, key=lambda x: x["date"])

        previous_value = None
        window = []

        for item in items:
            value = item["rate"]

            if previous_value is None:
                variation = None
            else:
                variation = ((value - previous_value) / previous_value) * 100

            window.append(value)
            if len(window) > 7:
                window.pop(0)

            moving_avg = sum(window) / len(window) if len(window) == 7 else None

            result.append({
            "date": item["date"],
            "base": item["base"],
            "base_name": base_info.get("name"),
            "base_symbol": base_info.get("symbol"),
            "currency": quote,
            "currency_name": currency_info.get("name"),
            "symbol": currency_info.get("symbol"),
            "value": value,
            "variation": round(variation, 4) if variation is not None else None,
            "moving_avg_7d": round(moving_avg, 4) if moving_avg is not None else None
        })

            previous_value = value

    result = sorted(result, key=lambda x: (x["currency"], x["date"]))
    return result