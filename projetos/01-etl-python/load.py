import csv
from typing import List, Dict, Any


def load_to_csv(data: List[Dict[str, Any]], file_path: str = "output.csv") -> None:
    """
    Salva os dados transformados em arquivo CSV.
    """

    if not data:
        raise ValueError("Nenhum dado para salvar.")

    # Define os campos dinamicamente
    fieldnames = data[0].keys()

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

    print(f"Arquivo salvo com sucesso em: {file_path}")