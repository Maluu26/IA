import numpy as np 
generations = 8000
popSize = 100
N = 30
def fitnessFunction(x):
    
    somatorio1 = 1/N * np.sum(x**2)
    somatorio2 = 1/N * np.sum(np.cos(2*np.pi*x))
    result = -20 * np.pow(np.e, (-0.2 * np.sqrt(somatorio1))) - pow(np.e, somatorio2) + 20 + np.e
    penalidade = 0
    if np.any(x < -32) or np.any(x > 32) : penalidade = 12000

    return result+ penalidade 


def selection(pop):

    i1 = pop[np.random.randint(0,100)]
    f1 = fitnessFunction(i1)
    i2 = pop[np.random.randint(0,100)]
    f2 = fitnessFunction(i2)
    if f1 < f2: return i1
    else: return i2

def crossOver(pop, crossOverChance):

    i1 = pop[np.random.randint(0,100)]
    i2 = pop[np.random.randint(0,100)]
    
    if np.random.rand()<crossOverChance:
      size = len(i2)//2
      f1 = np.concatenate((i1[:size], i2[size:]))
      f2 = np.concatenate((i2[:size], i1[size:]))
      return f1,f2
    return i1, i2

def mutation(pop):
    for i in range(len(pop)):
        if(np.random.rand()<0.10):
            position = np.random.randint(0,30)
            value = np.random.randint(low = -32, high= 32)
            pop[i][position] = value
    return pop
    

def ga(crossOverChance):
    initialPop = np.random.randint(low = -32, high= 32, size=(100, 30))
    
    
    for i in range(generations):
        middlePop = []
        for _i in range(100):
            middlePop.append(selection(initialPop))
        crossPop = []
        for _i in range(50):
            i1,i2 = crossOver(middlePop, crossOverChance)
            crossPop.append(i1)
            crossPop.append(i2)
        crossPop = mutation(crossPop)
        fitnessValues = np.array([fitnessFunction(i) for i in crossPop])
        initialPop = np.array(crossPop)
    return np.min(fitnessValues)
    
def main():
    gaResult = ga(0.6)
    print(gaResult)

if __name__ == '__main__':
    main()