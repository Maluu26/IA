import numpy as np 


def profit(vet):
    return 30*vet[0] + 50*vet[1] + 40*vet[2]

def checkRestrictions(vet):
    timeSpent = 2*vet[0] + 4*vet[1] + 3*vet[2]
    resourcesSpent = 3*vet[0]+ 2*vet[1] + 4*vet[2]
    return ((timeSpent<=100) and (resourcesSpent<=90) and (np.sum(vet)>0) and vet[0]>=0 and vet[1]>=0 and vet[2]>=0 )

def neighboorGenerator(values):
    while(True):
        new = np.random.choice([-1,1])
        ind = np.random.randint(low=0, high=3)
        proposal = list(values)
        proposal[ind] += new
        if(checkRestrictions(proposal)):
            return proposal

def simulatedAnnealing(tMin):
    values = np.random.randint(low=0, high=20, size=(3))
    while not checkRestrictions(values):
        values = np.random.randint(low=0, high=20, size=(3))
    solution = profit(values)
    current = values
    T = 100

    while(T>tMin):
        neighboor = neighboorGenerator(current)
        delta = profit(neighboor) - profit(current)
       
        if(delta>0): 
            current = neighboor
        else:
            
            if np.random.rand()<np.exp(delta/T):
                current = neighboor
        
        if(profit(current)>solution):
            solution = profit(current)
            values = current    
        T *= 0.95
    return solution, values

def main():
    profitAmount, ops = simulatedAnnealing(0.1)
    print(f'Lucro foi de {profitAmount}\n A: {ops[0]}, B: {ops[1]}, C: {ops[2]}')

if __name__ == '__main__':
    main()