import numpy as np
import math 

V = [2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25]
C = [20, 54, 98, 120, 34, 12, 88, 122, 33, 40]

D = [150, 200, 250, 300, 400]
P = [65, 98, 150, 210, 340]

totalTubos= 10
N = 100
POPULACAO = np.random.randint(low=0, high = 5, size = (N, totalTubos))


def fitness_function(individuo):
    custo = 0
    penalidade = 0
    vazao = 0


    for i in range(totalTubos):
        custo += C[i]*P[individuo]
        vazaO += V[i]

        qmax = np.inf
        if vazao > 0.75*qmax:
            penalidade += 10000
        
    return custo + penalidade


def QMax(D):
    n = 0.013
    s = 0.005
    rh = D/4
    a = np.pi * math.pow(D,2)
    return 1/n * a * math.sqrt(s) * math.pow(rh, (2/3))

def ga(N,crossOverP, mutationP ):
    popi = POPULACAO(N)
   
    for i in range(10):
        popii = []
        for j in range(N):
            
            pos1 = np.random.randint(low=0, high = 100)
            pos2 = np.random.randint(low=0, high = 100)

            pai1 = fitness_function(individuo=popi[pos1])
            pai2 = fitness_function(individuo=popi[pos2])
            
            if pai1>pai2: 
                popii.append(pai1)
            else:
                popii.append(pai2)
    filhos = []
    for _ in range(N/2):
        posF1 = np.random.randint(0,100)
        posF2 = np.random.randint(0,100)

        if crossOverP > np.random.rand():
            filho = []; filho2 = []
        

def main():
    ga(N, 0.7, 0.1)
