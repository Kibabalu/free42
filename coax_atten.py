# D = k1 + k2 * f + k3 * sqrt(f)
#
# RG-58:
#
#  1    f       sqrt(f)     D_RG-58 D_RG-213
#
#  1    1e6     1e3         1, 3123  0, 65617
#  1    10e6    3, 1623e3    4, 5932  1, 9685
#  1    50e6    7, 0711e3    10, 827  5, 2493
#  1    100e6   10e3        16, 076  7, 2178
#  1    200e6   14, 142e3    23, 95   10, 827
#  1    400e6   20e3        36, 745  15, 748
#  1    700e6   26, 458e3    55, 446  21, 654
#  1    900e6   30e3        65, 945  25, 262
#  1    1e9     31, 623e3    70.538  27, 231

import numpy as np
import matplotlib.pyplot as plt

X = np.matrix('1 1e6 1e3; 1 10e6 3.1623; 1 50e6 7.0711e3; 1 100e6 10e3; 1 200e6 14.142e3; 1 400e6 20e3; 1 700e6 26.458e3; 1 900e6 30e3; 1 1e9 31.623e3')

y_RG58 = np.matrix(
    '1.3123; 4.5932; 10.827; 16.076; 23.95; 36.745; 55.446; 65.945; 70.538')

y_RG213 = np.matrix('0.65617; 1.9685; 5.2493; 7.2178; 10.827; 15.748; 21.654; 25.262; 27.231')

beta_RG58, res_RG58, rank_RG58, val_RG58 = np.linalg.lstsq(X, y_RG58, rcond=None)
beta_RG213, res_RG213, rank_RG213, val_RG213 = np.linalg.lstsq(X, y_RG213, rcond=None)

print('beta_RG58 = \n', beta_RG58)
print('beta_RG213 = \n', beta_RG213)

print('res_RG58 = \n', res_RG58)
print('res_RG213 = \n', res_RG213)

