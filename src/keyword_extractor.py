def extract_keywords(text):
    return list(set(text.lower().split()))

if __name__ == "__main__":
    print(extract_keywords("Wireless Earbuds for Gaming"))
