import json

def generate_title(product_name):
    return f"Buy {product_name} Online at Best Price | High Quality"

if __name__ == "__main__":
    data = {"product_name": "Wireless Earbuds"}
    print(generate_title(data["product_name"]))
