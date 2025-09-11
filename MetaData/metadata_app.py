import os
import csv

# Use raw string so Windows path works
base_dir = r"D:\Infosys Project\20news-18828"
output_csv = "news_metadata.csv"

def extract_body(text):
    lines = text.splitlines()
    body_started = False
    body_lines = []
    for line in lines:
        if not body_started:
            if line.strip() == "":
                body_started = True
            continue
        body_lines.append(line)

    clean_lines = []
    for line in body_lines:
        if line.strip().startswith("--") or line.strip().startswith("__"):
            break
        clean_lines.append(line)

    return " ".join(clean_lines).strip()

with open(output_csv, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["category", "filename", "text"])

    for category in os.listdir(base_dir):
        category_path = os.path.join(base_dir, category)
        if os.path.isdir(category_path):
            for fname in os.listdir(category_path):
                file_path = os.path.join(category_path, fname)
                with open(file_path, encoding="latin-1") as f:
                    raw_text = f.read()
                    body_text = extract_body(raw_text)
                    writer.writerow([category, fname, body_text])

print(f"✅ Metadata saved to {output_csv}")