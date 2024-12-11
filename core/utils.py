import os
import pandas as pd
from core.parameters import DATASET_BASE_PATH

def get_dataset_path(file_name):
    """
    データセットのフルパスを取得
    :param file_name: データセットのファイル名（parameters.pyで定義）
    :return: フルパス
    """
    return os.path.join(DATASET_BASE_PATH, file_name)

def get_gene_shape(file_path):
    """
    データセットから遺伝子の形状（行数、列数）を計算
    :param file_path: データセットのパス
    :return: (行数, 列数) ※1列目（ID列）は除外
    """
    data = pd.read_csv(file_path)
    rows = data.shape[0]        # 行数
    columns = data.shape[1] - 1 # 列数（1列目を除外）
    return rows, columns

def get_gene_value_range(file_path):
    """
    データセットから遺伝子の値の範囲（最小値、最大値）を計算
    :param file_path: データセットのパス
    :return: (最小値, 最大値) ※1列目（ID列）は除外
    """
    data = pd.read_csv(file_path)
    columns = data.shape[1] - 1  # 1列目を除外
    return 0, columns  # 最小値は0、最大値は列数
