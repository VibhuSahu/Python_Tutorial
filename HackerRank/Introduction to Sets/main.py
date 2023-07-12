def average(array):
    # your code goes here
    sumOfDistinctHeight = 0

    for element in set(array):
        sumOfDistinctHeight += element

    returnAverage = sumOfDistinctHeight / len(set(array))

    return returnAverage


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)