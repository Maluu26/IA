import numpy as np
N = 30

def fitnessFunction(x):
    
    somatorio1 = 1/N * np.sum(x**2)
    somatorio2 = 1/N * np.sum(np.cos(2*np.pi*x))
    result = -20 * np.pow(np.e, (-0.2 * np.sqrt(somatorio1))) - pow(np.e, somatorio2) + 20 + np.e
    penalidade = 0
    if np.any(x < -32) or np.any(x > 32) : penalidade = 1000

    return result + penalidade 

def mutation():     
    
def differentialEvolution(F, cr):
    
    initialPop = np.random.randint(low = -32, high=32,size=(100,30))
   
def main():
    differentialEvolution(0.5, 0.3)

if __name__ == '__main__':
    main()