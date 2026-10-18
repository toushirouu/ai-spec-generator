import csv
import tempfile
import unittest
from pathlib import Path

from src.product_data import load_products


class LoadProductsTests(unittest.TestCase):
    def test_example_csv_loads_as_review_records(self):
        path = Path(__file__).resolve().parents[1] / "data" / "input" / "products.csv"
        products = load_products(path)
        self.assertEqual(len(products), 2)
        self.assertTrue(all(row["validation_status"] == "REVIEW" for row in products))
        self.assertTrue(all(row["parameters"] == {} for row in products))

    def test_parameter_requires_source(self):
        columns = [
            "product_id", "manufacturer", "catalog_number", "variant",
            "product_url", "validation_status", "parameters_json",
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "products.csv"
            with path.open("w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=columns)
                writer.writeheader()
                writer.writerow({
                    "product_id": "p-1", "validation_status": "PASS",
                    "parameters_json": '{"voltage": {"value": 230, "unit": "V"}}',
                })
            with self.assertRaisesRegex(ValueError, "value i source"):
                load_products(path)

    def test_known_non_value_states_are_allowed(self):
        columns = [
            "product_id", "manufacturer", "catalog_number", "variant",
            "product_url", "validation_status", "parameters_json",
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "products.csv"
            with path.open("w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=columns)
                writer.writeheader()
                writer.writerow({
                    "product_id": "p-1", "validation_status": "REVIEW",
                    "parameters_json": '{"voltage": {"state": "MISSING"}}',
                })
            self.assertEqual(
                load_products(path)[0]["parameters"]["voltage"]["state"], "MISSING"
            )


if __name__ == "__main__":
    unittest.main()
