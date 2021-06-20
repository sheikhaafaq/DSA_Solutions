def staircase(height, maxSteps):
    if height <= 1:
        return 1

    numberOfways = 0

    for step in range(1, min(maxSteps, height) + 1): 
        numberOfways += staircase (height - step, maxSteps)
    return numberOfways

print(staircase(4,2))