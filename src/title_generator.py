import json

def generate_title(product_name, brand="Generic", category="General"):
    keywords = [brand, product_name, category, "Best Price", "High Quality"]
    title = " ".join(keywords)
    return f"{title} | Buy Online"

if __name__ == "__main__":
    data = {
        "product_name": "Wireless Earbuds",
        "brand": "SoundMax",
        "category": "Electronics"
    }
    print(generate_title(**data))
