import numpy as np 


def profit(vet):
    return 30*vet[0] + 50*vet[1] + 40*vet[2]

def checkRestrictions(vet):
    timeSpent = 2*vet[0] + 4*vet[1] + 3*vet[2]
    resourcesSpent = 3*vet[0]+ 2*vet[1] + 4*vet[2]
    return ((timeSpent<=100) and (resourcesSpent<=90) and (np.sum(vet)>0) and vet[0]>=0 and vet[1]>=0 and vet[2]>=0 )

def neighboorGenerator(currentBest):
    newSolution = []
    for i in range(3):
        for delta in [-1, 1]:
            proposal = list(currentBest)
            proposal[i]+= delta
            if(checkRestrictions(proposal)):
                newSolution.append(proposal)
    return newSolution

def hillClimbing():
    values = np.random.randint(low=0, high=20, size=(3))
    while not checkRestrictions(values):
        values = np.random.randint(low=0, high=20, size=(3))
    solution = profit(values)
    foundBetter = True
    while(True):
        neighboors = neighboorGenerator(values)
        if not neighboors: break
        best = max(neighboors, key=profit)
        if(profit(best)>solution):
            solution = profit(best)
            values = best      
        else:
            break
    return solution, values

def vanillaHC():
    profitAmount, ops = hillClimbing()
    print(f'Lucro foi de {profitAmount}\n A: {ops[0]}, B: {ops[1]}, C: {ops[2]}')

def randomStartHC():
    profits = 0
    values = [0,0,0]
    for i in range(100):
       profitAmount, ops = hillClimbing()
       if(profitAmount>profits):
        profits = profitAmount
        values = ops
    print(f'O Lucro foi de {profits}\n A: {values[0]}, B: {values[1]}, C: {values[2]}\n')

def stochasticHC():
    values = np.random.randint(low=0, high=40, size=(3))
    while not checkRestrictions(values):
        values = np.random.randint(low=0, high=40, size=(3))
    solution = profit(values)
    tol = 0
    while(tol<=100):
       new = np.random.choice([-1,1])
       ind = np.random.randint(low=0, high=3)
       proposal = list(values)
       proposal[ind]+= new
       if(checkRestrictions(proposal) and profit(proposal)>solution):
            solution =  profit(proposal)
            values = proposal
            tol = 0
       else:
            tol+=1
    print(f'O Lucro foi de {solution}\n A: {values[0]}, B: {values[1]}, C: {values[2]}\n')


def main():
    randomStartHC()
if __name__ == '__main__':
    main()