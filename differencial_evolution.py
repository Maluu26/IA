import numpy as np
N = 30

def fitnessFunction(x):
    
    somatorio1 = 1/N * np.sum(x**2)
    somatorio2 = 1/N * np.sum(np.cos(2*np.pi*x))
    result = -20 * np.pow(np.e, (-0.2 * np.sqrt(somatorio1))) - pow(np.e, somatorio2) + 20 + np.e
    penalidade = 0
    if np.any(x < -32) or np.any(x > 32) : penalidade = 1000

    return result + penalidade 

def selectInd(pop):
    return pop[np.random.randint(0,100)]

def mutation(pop, fitness, F):     
    
    i1 = selectInd(pop)
    i2 = selectInd(pop)
    i3 = selectInd(pop)
    return (i1 +  F(i2 - i3))

def crossOver(iPop, mutPop, cr):
    newPop = []
    for i in range(len(iPop)):
        indM = selectInd(mutPop) 
        indO = selectInd(mutPop) 
        for j in range(N):
            if np.random.rand()<cr:  
                newPop[i][j] = indM[j] 
            else:
                newPop[i][j] = indO[j] 

    return newPop

def selection(initialPop, crossPop):
    
def differentialEvolution(F, cr):
    
    initialPop = np.random.randint(low = -32, high=32,size=(100,30))
    fitnessPop = np.array([fitnessFunction(ind) for ind in initialPop])
    middlePop = [mutation(initialPop,fitnessPop,F) for i in range (100)]
    crossPop = crossOver(initialPop, middlePop,cr)
    newPop = selection()
    historico = list()
    #np.clip para mutação

   
def main():
    differentialEvolution(0.5, 0.3)

if __name__ == '__main__':
    main()