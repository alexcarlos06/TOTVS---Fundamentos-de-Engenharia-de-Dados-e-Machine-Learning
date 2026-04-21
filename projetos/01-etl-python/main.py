from extract import extract_exchange_rates_frankfurter, extract_details_currency
from transform import transform_exchange_rates, build_currency_map
from load import load_to_csv


def main():
    raw = extract_exchange_rates_frankfurter(quotes="BRL,GBP")
    currencies = extract_details_currency()
    currency_map = build_currency_map(currencies)
    transformed = transform_exchange_rates(raw, currency_map)

    load_to_csv(transformed, "exchange_rates.csv")


if __name__ == "__main__":
    main()