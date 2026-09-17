import csv

tax_rate = 15


def calculate_tax(cost_price):
    return cost_price * tax_rate / 100


def calculate_final_price(cost_price, sales_tax):
    return cost_price + sales_tax


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

            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                cost_price = float(row["Product-CostPrice"])

                sales_tax = calculate_tax(cost_price)
                final_price = calculate_final_price(cost_price, sales_tax)

                writer.writerow({
                    "Product-Name": row["Product-Name"],
                    "Product-CostPrice": cost_price,
                    "Product-SalesTax": sales_tax,
                    "Product-FinalPrice": final_price,
                    "Country": row["Country"]
                })


process_products("products.csv", "output.csv")