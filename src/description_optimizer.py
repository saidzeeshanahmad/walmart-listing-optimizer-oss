def optimize_description(desc):
    enhancements = [
        "high quality",
        "durable",
        "best in class",
        "designed for everyday use"
    ]
    
    return desc + " " + ", ".join(enhancements) + "."

if __name__ == "__main__":
    print(optimize_description("Wireless earbuds with great sound"))
