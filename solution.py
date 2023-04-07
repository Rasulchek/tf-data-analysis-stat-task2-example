import pandas as pd
import numpy as np

from scipy.stats import chi2
from scipy.stats import chi2
from scipy.stats import norm

chat_id = 680977959  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    from scipy.stats import chi2

    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    x_mean = x.mean()
    s_square = (1 / (n - 1)) * np.sum((x - x_mean) ** 2)

    alpha = 1 - p
    # print("right:", chi2.ppf(1 - alpha / 2, n - 1))
    # print("left:", chi2.ppf(alpha / 2, n - 1))

    lower_bound = np.sqrt(((n - 1) * s_square) / (chi2.ppf(1 - alpha / 2, n - 1) * 50))
    upper_bound = np.sqrt(((n - 1) * s_square) / (chi2.ppf(alpha / 2, n - 1) * 50))

    return lower_bound, upper_bound

# sigma_square = 4
#
# X = norm.rvs(0, 50*sigma_square, size = 1000)
# Y = norm.rvs(0, 50*sigma_square, size = 1000)
#
# Z = np.sqrt(X**2 + Y**2)
#
# left, right = solution(0.99, Z)
#
# print(left, right, right - left)
