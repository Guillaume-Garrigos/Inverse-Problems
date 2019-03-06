import numpy as np
from numpy import linalg as la
import my_toolbox.sparsity as sparse

def lasso(A, y, reg_param, iter_nb, verbose=False):
# Use the Forward-Backward algorithm to find a minimizer of:
# reg_param*norm(x,1) + 0.5*norm(Ax-y,2)**2
    if verbose: # Optional output
        regret = np.zeros(iter_nb)
        support = np.zeros(iter_nb)
        details = {
            "function_value" : regret,
            "iterate_support" : support
        }
    stepsize = 0.8 * 2/la.norm(A,2)**2
    x = np.zeros( (A.shape[1],1) )
    for k in range(iter_nb):
        x = x - stepsize * A.T@(A@x - y)
        x = sparse.soft_thresholding(x,reg_param*stepsize)
        if verbose:
            regret[k] = 0.5*la.norm(A@x-y,2)**2 + reg_param*la.norm(x,1)
            support[k] = sparse.norm0(x)
    if verbose:
        return x, details
    else:
        return x


