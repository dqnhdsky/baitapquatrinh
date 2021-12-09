# In:
import numpy as np
np.random.randint(0, 2)
coins = np.random.randint(2, size=1000)
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
# Out:
# % số lần tung được mặt ngửa:  48.9
# % số lần tung được mặt úp:  51.1
