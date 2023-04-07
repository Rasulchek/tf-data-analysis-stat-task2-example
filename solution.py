import pandas as pd
import numpy as np

from scipy.stats import chi2
from scipy.stats import norm
from scipy.stats import expon

chat_id = 680977959  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    alpha = 1 - p
    scale = (x ** 2).sum()

    lower_bound = np.sqrt(scale / (chi2.ppf(1 - alpha / 2, 2 * n) * 50))
    upper_bound = np.sqrt(scale / (chi2.ppf(alpha / 2, 2 * n) * 50))

    return lower_bound, upper_bound