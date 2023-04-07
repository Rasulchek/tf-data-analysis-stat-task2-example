import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 680977959 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    S = np.std(x, ddof=1)  # выборочное стандартное отклонение
    alpha = 1 - p
    df = n - 1
    chi2_left = chi2.ppf(alpha / 2, df)
    chi2_right = chi2.ppf(1 - alpha / 2, df)
    lower_bound = np.sqrt((df * S ** 2) / chi2_right)
    upper_bound = np.sqrt((df * S ** 2) / chi2_left)

    return lower_bound, upper_bound
