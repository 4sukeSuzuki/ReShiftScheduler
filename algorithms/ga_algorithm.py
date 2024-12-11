import random
import numpy as np  # NumPyを利用
from core.utils import load_all_datasets, get_gene_shape
from core.parameters import (
    POPULATION_SIZE, CROSSOVER_RATE, MUTATION_RATE, ELITISM_RATE,
    MAX_GENERATIONS, DATASET_BASE_PATH
)
from core.fitnessCalc import fitness_function

# データセットのパス（TeacherHopeに基づく）
TEACHER_HOPE_FILE = f"{DATASET_BASE_PATH}/teachers_hope/EK_teacher_hope.csv"

# 遺伝子の形状を動的に取得
GENE_ROWS, GENE_COLUMNS = get_gene_shape(TEACHER_HOPE_FILE)

# 初期個体を生成（ランダム値）
def generate_initial_population():
    """
    ランダムな初期個体群を生成
    :return: 初期個体群（3次元配列: [POPULATION_SIZE, GENE_ROWS, GENE_COLUMNS]）
    """
    return np.random.randint(0, 2, (POPULATION_SIZE, GENE_ROWS, GENE_COLUMNS))

# 遺伝的アルゴリズムの実行
def run_ga():
    # 初期個体群を生成
    population = generate_initial_population()

    for generation in range(MAX_GENERATIONS):
        # 適応度を計算（各個体を2次元として計算）
        fitnesses = [
            fitness_function(individual) for individual in population
        ]

        # 進捗表示（適応度の最高値を表示）
        best_fitness = max(fitnesses)
        print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")

        # 次世代を生成（略: ここに交叉や突然変異を追加）
