import numpy as np 

dimensionAmount = 30 
popSize = 1000
generations = 1000
N = 30
c1 = 2.05
c2 = 2.05
def createPop(dimension,amount):
    return np.random.uniform(-32, 32,size=(amount,dimension))

def fitnessFunction(x):
    somatorio1 = 1/N * np.sum(x**2)
    somatorio2 = 1/N * np.sum(np.cos(2*np.pi*x))
    result = -20 * np.pow(np.e, (-0.2 * np.sqrt(somatorio1))) - pow(np.e, somatorio2) + 20 + np.e
    return result

def looplessPSO(w): 
    initialPop = createPop(dimensionAmount, popSize)
    veloPop = np.random.uniform(-1,1,(popSize, dimensionAmount))
    localBest = np.copy(initialPop)
    fitnessPop = [fitnessFunction(initialPop[j]) for j in range(popSize)]
    globalBest = np.copy(initialPop[np.argmin(fitnessPop)])

    for j in range(generations):
        for i in range(popSize): 
            r1 = np.random.random()
            r2 = np.random.random()
            veloPop[i] = w * veloPop[i] + c1*r1*(localBest[i]-initialPop[i]) + c2*r2*(globalBest - initialPop[i])
            initialPop[i] += veloPop[i]
            initialPop[i] = np.clip(initialPop[i], -32, 32)
            
            if(fitnessFunction(localBest[i])>fitnessFunction(initialPop[i])):
                localBest[i] = np.copy(initialPop[i])
            
            if (fitnessFunction(globalBest)>fitnessFunction(initialPop[i])):
                globalBest = np.copy(initialPop[i])
               
        print(fitnessFunction(globalBest))

def main():
    looplessPSO(0.7)
if __name__ == '__main__':
    main()