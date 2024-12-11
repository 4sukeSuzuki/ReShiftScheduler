import random
import numpy as np
import pandas as pd  # expand_rowsでDataFrame操作をするために必要
from core.utils import (
    get_dataset_path, get_gene_shape, get_gene_value_range, expand_rows
)
from core.parameters import (
    TEACHER_HOPE_FILE_NAME, TEACHER_SUB_FILE_NAME, POPULATION_SIZE,
    CROSSOVER_RATE, MUTATION_RATE, ELITISM_RATE, MAX_GENERATIONS, ASSIGNABLE_COUNT
)
from core.fitnessCalc import fitness_function

# データセットパスの取得
TEACHER_HOPE_FILE = get_dataset_path(TEACHER_HOPE_FILE_NAME)
TEACHER_SUB_FILE = get_dataset_path(TEACHER_SUB_FILE_NAME)

# データを読み込み
teacher_hope_data = pd.read_csv(TEACHER_HOPE_FILE)
teacher_sub_data = pd.read_csv(TEACHER_SUB_FILE)

# 担当可能数に基づいて行を拡張
teacher_hope_data = expand_rows(teacher_hope_data, ASSIGNABLE_COUNT)
teacher_sub_data = expand_rows(teacher_sub_data, ASSIGNABLE_COUNT)

# 遺伝子の形状と範囲を取得
GENE_ROWS = teacher_hope_data.shape[0]
GENE_COLUMNS = teacher_hope_data.shape[1] - 1  # 1列目（ID列）を除外
GENE_MIN_VALUE, GENE_MAX_VALUE = get_gene_value_range(TEACHER_SUB_FILE)

print(f"GENE_ROWS: {GENE_ROWS}, GENE_COLUMNS: {GENE_COLUMNS}")  # 確認用出力

# 初期個体を生成（ランダム値）
def generate_initial_population():
    """
    ランダムな初期個体群を生成
    :return: 初期個体群（3次元配列: [POPULATION_SIZE, GENE_ROWS, GENE_COLUMNS]）
    """
    tShift = np.random.randint(
        GENE_MIN_VALUE, GENE_MAX_VALUE + 1,  # 範囲: 0〜列数
        (POPULATION_SIZE, GENE_ROWS, GENE_COLUMNS)
    )
    print("Initial Population Shape:", tShift.shape)  # デバッグ出力: 初期個体の形状
    return tShift

# 遺伝的アルゴリズムの実行
def run_ga():
    # 初期個体群を生成
    population = generate_initial_population()

    for generation in range(MAX_GENERATIONS):
        # 適応度を計算（各個体を2次元配列として計算）
        fitnesses = [
            fitness_function(individual) for individual in population
        ]

        # 適応度の最高値を取得
        best_fitness = max(fitnesses)

        # 進捗表示（適応度の最高値を表示）
        print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")

        # 次世代を生成（略: ここに交叉や突然変異を追加）
