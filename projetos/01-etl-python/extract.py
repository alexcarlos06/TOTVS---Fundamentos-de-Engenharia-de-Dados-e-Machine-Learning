from typing import Dict, Any
import requests


def extract_details_currency() -> Dict[str, Any]:
    """
    Extrai dados da API Frankfurter.
    Returns:
        dict: JSON retornado pela API com todas as moedas disponíveis
    """ 
    url = "https://api.frankfurter.dev/v2/currencies"
    response = requests.get(url=url, timeout=20)
    response.raise_for_status()
    
    return response.json()

def extract_exchange_rates_frankfurter(
    start_date: str = "2026-01-01",
    end_date: str = "2026-04-01",
    base: str = "USD",
    quotes: str = "BRL"
) -> Dict[str, Any]:
    """
    Extrai dados da API Frankfurter.

    Args:
        start_date (str): Data inicial (YYYY-MM-DD)
        end_date (str): Data final (YYYY-MM-DD)
        base (str): Moeda base
        quotes (str): Moeda alvo separada por virgula caso seja mais de uma moeda

    Returns:
        dict: JSON retornado pela API
    """

    url = "https://api.frankfurter.dev/v2/rates"

    params = {
        "from": start_date,
        "to": end_date,
        "base": base,
        "quotes": quotes
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = extract_details_currency()
    print(data)