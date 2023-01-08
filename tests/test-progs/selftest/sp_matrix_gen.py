import sys
import numpy as np
import scipy.sparse as ss

# 生成随机稀疏矩阵
num_row = 128
num_col = 128
density = float(sys.argv[1])

sparseX = ss.rand(num_col, num_row, density, format='coo', dtype=np.double)*100
X = sparseX.todense()

X_num = np.array([[num_row],[num_col],[sparseX.nnz]]).T
X_sp = np.array([sparseX.row,sparseX.col,sparseX.data]).T
# X_sp = X_sp[np.lexsort(X_sp[:,::-1].T)]

np.savetxt(r'src/a_ge.data', X, fmt='%lf', delimiter=' ')
np.savetxt(r'src/a_sp.data', X_num, fmt='%d %d %d', delimiter=' ')
f = open('src/a_sp.data', 'a')
np.savetxt(f, X_sp, fmt='%d %d %lf', delimiter=' ')
f.close() 

sparseX = ss.rand(num_col, num_row, density, format='coo', dtype=np.double)*100
X = sparseX.todense()

X_num = np.array([[num_row],[num_col],[sparseX.nnz]]).T
X_sp = np.array([sparseX.row,sparseX.col,sparseX.data]).T
# X_sp = X_sp[np.lexsort(X_sp[:,::-1].T)]

np.savetxt(r'src/b_ge.data', X, fmt='%lf', delimiter=' ')
np.savetxt(r'src/b_sp.data', X_num, fmt='%d %d %d', delimiter=' ')
f = open('src/b_sp.data', 'a')
np.savetxt(f, X_sp, fmt='%d %d %lf', delimiter=' ')
f.close()