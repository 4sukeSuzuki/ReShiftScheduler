import csv
from pathlib import Path
import pandas as pd

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

def get_gene_shape(file_path):
    """
    データセットから遺伝子の形状（行数、列数）を計算
    :param file_path: データセットのパス
    :return: (行数, 列数) ※1列目（ID列）は除外
    """
    data = pd.read_csv(file_path)
    rows = data.shape[0]        # 行数
    columns = data.shape[1] - 1 # 列数（1列目を除外）
    print(rows,columns)
    return rows, columns


