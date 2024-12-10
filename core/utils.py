import csv
from pathlib import Path

def load_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append([int(value) for value in row])
    return data

def load_all_datasets(base_dir):
    datasets = {}
    base_path = Path(base_dir)
    for category in base_path.iterdir():
        if category.is_dir():
            for csv_file in category.glob("*.csv"):
                datasets[category.name] = load_csv(csv_file)
    return datasets
