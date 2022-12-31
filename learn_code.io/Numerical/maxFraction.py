def maxFraction(numerators,denominators):
    return [numerators[x] / denominators[x] for x in range(len(denominators))].index(max([numerators[x] / denominators[x] for x in range(len(denominators))]))

print(maxFraction([5, 2, 5],[6, 3, 4]))