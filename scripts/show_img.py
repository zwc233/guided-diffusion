import numpy as np
import matplotlib.pyplot as plt


import numpy as np

# 用文件名替换'file.npz'
filename = 'npz_file/samples_400x64x64x3.npz'

# 加载NPZ文件
with np.load(filename) as data:
    array = data['arr_0']

plt.imshow(array[300])  
plt.show()