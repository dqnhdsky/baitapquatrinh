# In:
import numpy as np
coins = np.random.choice([0, 1], size=1000, p=[0.2, 0.8])
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
# Out:
# % số lần tung được mặt ngửa:  18.3
# % số lần tung được mặt úp:  81.69999999999999