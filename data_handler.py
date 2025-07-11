import csv
import os

DATA_FILE = "keuangan.csv"

def baca_data():
    records = []
    if os.path.isfile(DATA_FILE):
        with open(DATA_FILE, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            for item in reader:
                records.append(item)
    return records

def simpan_data(records):
    header = ["tanggal", "jenis", "kategori", "nominal"]
    with open(DATA_FILE, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for rec in records:
            writer.writerow(rec)
