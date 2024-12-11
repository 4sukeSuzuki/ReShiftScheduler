"""
パラメータ設定ファイル

GA（遺伝的アルゴリズム）で使用する設定をまとめています。
各パラメータの説明：
- POPULATION_SIZE：初期個体群のサイズ（生成する個体数）
- CROSSOVER_RATE：交叉率（親から子を生成する際の交叉の割合）
- MUTATION_RATE：突然変異率（各遺伝子が突然変異する確率）
- ELITISM_RATE：エリート保存率（世代交代時に上位何%の個体を次世代にそのまま残すか）
- MAX_GENERATIONS：最大世代数（進化を繰り返す回数）
- DATASET_BASE_PATH：データセットが格納されているディレクトリのパス
"""

# GAパラメータ
POPULATION_SIZE = 100          # 初期個体群のサイズ
CROSSOVER_RATE = 0.8           # 交叉率
MUTATION_RATE = 0.01           # 突然変異率
ELITISM_RATE = 0.1             # エリート保存率（上位10%）
MAX_GENERATIONS = 50           # 最大世代数

# データセットパス
DATASET_BASE_PATH = "./datasets"  # データセットが格納されているディレクトリ
