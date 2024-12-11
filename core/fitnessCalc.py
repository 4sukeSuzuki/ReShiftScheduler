def fitness_function(individual):
    """
    適応度関数
    :param individual: 個体（2次元配列: [GENE_ROWS, GENE_COLUMNS]）
    :return: 適応度のスコア（スカラー値）
    """
    # 仮の適応度計算: 個体内のすべての要素の合計
    return individual.sum()
