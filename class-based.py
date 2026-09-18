import csv

tax_rate = 10


class Product:

    def __init__(self, name, cost_price, country):
        self.name = name
        self.cost_price = float(cost_price)
        self.country = country

    def calculate_tax(self):
        return self.cost_price * tax_rate / 100

    def calculate_final_price(self):
        return self.cost_price + self.calculate_tax()


def process_products(input_file, output_file):

    with open(input_file, "r") as infile:
        reader = csv.DictReader(infile)

        with open(output_file, "w", newline="") as outfile:

            fieldnames = [
                "Product-Name",
                "Product-CostPrice",
                "Product-SalesTax",
                "Product-FinalPrice",
                "Country"
            ]

            writer = csv.DictWriter(outfile , fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:

                product = Product(
                    row["Product-Name"],
                    row["Product-CostPrice"],
                    row["Country"]
                )

                writer.writerow({
                    "Product-Name": product.name,
                    "Product-CostPrice": product.cost_price,
                    "Product-SalesTax": product.calculate_tax(),
                    "Product-FinalPrice": product.calculate_final_price(),
                    "Country": product.country
                })


process_products("products_class.csv", "output_class.csv")