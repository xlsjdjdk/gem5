import numpy as np
import scipy.sparse as ss

# 生成随机稀疏矩阵
num_col = 128
num_row = 128
sparse_rate = 0.7
num_ele = int(num_col*num_row*sparse_rate)
a = [np.random.randint(0,num_row) for _ in range(num_ele)]
b = [np.random.randint(0,num_col) for _ in range(num_ele-num_col)] + [i for i in range(num_col)]  # 保证每一列都有值，不会出现全零列
c = [10 * np.random.rand() for _ in range(num_ele)]
rows, cols, v = np.array(a), np.array(b), np.array(c)
sparseX = ss.coo_matrix((v,(rows,cols)))
X = sparseX.todense()

np.savetxt(r'src/a.data', X, fmt='%lf', delimiter=' ')

a = [np.random.randint(0,num_row) for _ in range(num_ele)]
b = [np.random.randint(0,num_col) for _ in range(num_ele-num_col)] + [i for i in range(num_col)]  # 保证每一列都有值，不会出现全零列
c = [10 * np.random.rand() for _ in range(num_ele)]
rows, cols, v = np.array(a), np.array(b), np.array(c)
sparseX = ss.coo_matrix((v,(rows,cols)))
X = sparseX.todense()

np.savetxt(r'src/b.data', X, fmt='%lf', delimiter=' ')