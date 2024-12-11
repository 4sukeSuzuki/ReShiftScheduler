"""
パラメータ設定ファイル

各データセットのパス設定を含む。
"""

# GAパラメータ
POPULATION_SIZE = 100
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.01
ELITISM_RATE = 0.1
MAX_GENERATIONS = 5

# データセットディレクトリ
DATASET_BASE_PATH = "./datasets"

# 各データセットのファイル名
TEACHER_HOPE_FILE_NAME = "teachers_hope/EK_teacher_hope.csv"
TEACHER_SUB_FILE_NAME = "teachers_sub/EK_teacher_sub.csv"
STUDENT_HOPE_FILE_NAME = "students_hope/EK_student_hope.csv"
STUDENT_SUB_FILE_NAME = "students_sub/EK_student_sub.csv"

# 担当可能数（講師データセットの各行を何回複製するか =1:N授業）
ASSIGNABLE_COUNT = 3