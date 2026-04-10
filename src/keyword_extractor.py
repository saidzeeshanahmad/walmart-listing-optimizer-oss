def extract_keywords(text):
    words = text.lower().split()
    keywords = list(set(words))
    return sorted(keywords)

if __name__ == "__main__":
    print(extract_keywords("Wireless Earbuds for Gaming and Music"))
