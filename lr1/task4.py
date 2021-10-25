from itertools import combinations

def maxWeights(listBars, bag):
    """
    This function calculates the maximum possible bars weight
    """
    knapsack = [[0 for j in range(bag + 1)] for i in range(len(listBars) + 1)]
    for i in range(len(listBars) + 1):
        for j in range(bag + 1):
            if i==0 or j==0:
                knapsack[i][j] = 0
            elif j >= listBars[i-1]:
                knapsack[i][j] = max(listBars[i - 1] + knapsack[i - 1][j - listBars[i - 1]], knapsack[i - 1][j])
            else:
                knapsack[i][j] = knapsack[i - 1][j]
    return knapsack[len(listBars)][bag]


if __name__ == "__main__":
    listUserBars = [int(x) for x in input('Enter bars weights ').split()]
    userBag = int(input('Enter bag weight '))
    print(maxWeights(listUserBars, userBag))

