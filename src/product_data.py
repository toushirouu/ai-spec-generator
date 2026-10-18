"""Walidacja podstawowego formatu wejściowego produktów (bez scrapowania)."""

import csv
import json
from pathlib import Path


REQUIRED_COLUMNS = {
    "product_id", "manufacturer", "catalog_number", "variant",
    "product_url", "validation_status", "parameters_json",
}
VALID_STATUSES = {"PASS", "REVIEW", "FAIL"}
PARAMETER_STATES = {"MISSING", "CONFLICT", "NOT_APPLICABLE"}


def load_products(path: str | Path) -> list[dict[str, str]]:
    """Wczytuje CSV i sprawdza podstawową strukturę oraz zapis parametrów."""
    with Path(path).open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
            raise ValueError(f"Brak wymaganych kolumn: {', '.join(sorted(missing))}")

        products = []
        for line, row in enumerate(reader, start=2):
            if not row.get("product_id", "").strip():
                raise ValueError(f"Wiersz {line}: brak product_id")
            status = row.get("validation_status", "").strip()
            if status not in VALID_STATUSES:
                raise ValueError(f"Wiersz {line}: nieznany status walidacji {status!r}")
            try:
                parameters = json.loads(row.get("parameters_json", ""))
            except json.JSONDecodeError as error:
                raise ValueError(f"Wiersz {line}: niepoprawny parameters_json") from error
            if not isinstance(parameters, dict):
                raise ValueError(f"Wiersz {line}: parameters_json musi być obiektem")

            for name, parameter in parameters.items():
                if not isinstance(parameter, dict):
                    raise ValueError(f"Wiersz {line}: parametr {name!r} musi być obiektem")
                if parameter.get("state") in PARAMETER_STATES:
                    continue
                if "value" not in parameter or not parameter.get("source"):
                    raise ValueError(
                        f"Wiersz {line}: parametr {name!r} wymaga value i source"
                    )
            row["parameters"] = parameters
            products.append(row)
        return products


if __name__ == "__main__":
    repository = Path(__file__).resolve().parents[1]
    products = load_products(repository / "data" / "input" / "products.csv")
    print(f"Wczytano rekordów: {len(products)}")
    for product in products:
        print(f"{product['product_id']}: {product['validation_status']}")
