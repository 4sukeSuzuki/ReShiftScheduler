import os
import pandas as pd
from core.parameters import DATASET_BASE_PATH,EXPORT_PASS

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

def ensure_export_path_exists(path):
    """
    デバッグ用のエクスポートディレクトリが存在しない場合に作成
    :param path: エクスポートディレクトリのパス
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"ディレクトリを作成しました: {path}")

def expand_rows(data, repeat_count, file_name=None):
    """
    データの各行を指定回数だけ連続して複製して拡張し、デバッグ用CSVに出力
    :param data: pandas.DataFrame, 元データ
    :param repeat_count: int, 各行を何回複製するか
    :param file_name: str, デバッグ用CSVのファイル名（optional）
    :return: pandas.DataFrame, 拡張されたデータ
    """
    # 各行を指定回数繰り返して複製
    expanded_data = data.loc[data.index.repeat(repeat_count)].reset_index(drop=True)
    
    # デバッグ用CSVの出力
    if file_name:
        ensure_export_path_exists(EXPORT_PASS)  # エクスポートパスを確認または作成
        export_path = os.path.join(EXPORT_PASS, file_name)
        expanded_data.to_csv(export_path, index=False, encoding='utf-8')
        print(f"拡張済みデータを保存しました: {export_path}")
    
    return expanded_data