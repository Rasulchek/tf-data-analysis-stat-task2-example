import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 680977959 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
   squared_distances = x**2
 
    sum_squared_distances = np.sum(squared_distances)
 
    n = len(x)
    df = n

    alpha = 1 - p
    chi2_low = chi2.ppf(alpha/2, df)
    chi2_high = chi2.ppf(1 - alpha/2, df)
 

    sigma2_low = sum_squared_distances / chi2_high
    sigma2_high = sum_squared_distances / chi2_low
 
    sigma_low = np.sqrt(sigma2_low / 50)
    sigma_high = np.sqrt(sigma2_high / 50)
 
    return sigma_low, sigma_high
