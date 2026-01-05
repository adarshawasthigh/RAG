import os, re, unicodedata

RAW_DIR = "data/raw"
CLEAN_DIR = "data/cleaned"
os.makedirs(CLEAN_DIR, exist_ok=True)

def clean(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"\[\d+\]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

for file in os.listdir(RAW_DIR):
    with open(os.path.join(RAW_DIR, file), encoding="utf-8") as f:
        cleaned = clean(f.read())

    with open(os.path.join(CLEAN_DIR, file), "w", encoding="utf-8") as f:
        f.write(cleaned)

    print(f"Cleaned → {file}")
