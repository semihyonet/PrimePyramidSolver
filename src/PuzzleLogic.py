def isPrime(target:int):
    Prime = True
    if (target <= 1):
        Prime = False
    elif (target == 2):
        Prime = True
    elif (Prime):
        for i in range(2,int(target/2)+1):
            if (target % i == 0):
                Prime = False

    return Prime


def legalMoves(parentIndex):
    solutions = [parentIndex,parentIndex+1]

    return solutions

