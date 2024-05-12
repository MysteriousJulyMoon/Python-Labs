import numpy as np
import scipy.stats


def logpdf_multivariate_normal(X, m, C):
    D = len(m)
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)
    norm_term = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)

    diff = X - m
    mahalanobis_term = -0.5 * np.sum(diff @ inv_C * diff, axis=1)

    log_pdf = norm_term + mahalanobis_term
    return log_pdf


# Генерация тестовых данных
np.random.seed(0)
N, D = 1000, 3
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.random.randn(D, D)
C = C @ C.T  # Генерация случайной ковариационной матрицы

# Вычисление логарифма плотности с помощью самописной функции
my_logpdf = logpdf_multivariate_normal(X, m, C)

# Вычисление логарифма плотности с помощью scipy.stats.multivariate_normal
scipy_logpdf = scipy.stats.multivariate_normal(m, C).logpdf(X)

# Сравнение результатов
print("Максимальное отклонение между результатами:", np.max(np.abs(my_logpdf - scipy_logpdf)))