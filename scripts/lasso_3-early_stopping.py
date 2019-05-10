import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt

import invprob.sparse as sparse
import invprob.optim as optim
from invprob.optim import fb_lasso



np.random.seed(seed=78)  # Seed for np.random (78)
dpi = 100  # Resolution for plotting (230 for small screen, 100 for large one)
plt.ion()
folder = "scripts/../output/L1_reg/"

# We start by defining the characteristics of the problem
data_size = 100
data_number = round(data_size / 2)
sparsity_level = 10

# We define the main components of our problem
Phi = np.random.randn(data_number, data_size)
x0 = np.sign(sparse.randn(data_size, 1, sparsity_level))
noisy_vector = np.random.randn(data_number, 1)
y = Phi@x0 + 0 * noisy_vector

# We solve the noiseless problem
iter_nb = 10000
exp_decay = 0.1  # The smaller the exponent, the faster is the algorithm
reg_param_grid = 1 / (np.arange(iter_nb)+1)**exp_decay

x_sol = fb_lasso(Phi, y, reg_param_grid, iter_nb, verbose=False)
_ = plt.figure(dpi=dpi)
sparse.stem(x0, "C0", "ground truth")
sparse.stem(x_sol, "C1", "inverse solution")


# We solve the noisy problem
y = Phi@x0 + 0.1 * noisy_vector
iter_nb = 10000
exp_decay = 0.1  # The smaller the exponent, the faster is the algorithm
reg_param_grid = 1 / (np.arange(iter_nb)+1)**exp_decay

x_sol, details = fb_lasso(Phi, y, reg_param_grid, iter_nb, verbose=True)



_ = plt.figure(dpi=dpi)
sparse.stem(x0, "C0", "ground truth")
sparse.stem(x_sol, "C1", "reg solution")




sparse.stem(details["iterate_path"][:, 10], "C1", "reg solution")
sparse.stem(details["iterate_path"][:, 100], "C2", "reg solution")
sparse.stem(details["iterate_path"][:, 1000], "C3", "reg solution")
sparse.stem(details["iterate_path"][:, 10000], "C4", "reg solution")
sparse.stem(details["iterate_path"][:, 99999], "C5", "reg solution")


#########################################
# This is for production only
import importlib
importlib.reload(optim)
import invprob.optim as optim
from invprob.optim import fb_lasso
#########################################