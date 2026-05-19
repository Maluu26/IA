import numpy as np

def fitnessFunction(x):
    nSum = 0
    cosSum = 0
    
    for i in range(len(x)):
        nSum += pow(x[i],2)
        cosSum += np.cos(2*np.pi*x[i])
    
    exp1 = -0.2 * np.power(1/len(x)*nSum,1/2)
    exp2 =   np.power(1/len(x)*nSum,1/2)
    
    
    result = -20**(exp1 - exp2) + 20 + np.e
    penalidade = 0

    if min(result) < -32 or max(result)>32: penalidade = 1000
    return result + penalidade