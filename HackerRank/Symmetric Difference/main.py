def symmetricDifference(Avalue, Bvalue):
    differenceSetA = Avalue.difference(Bvalue)
    differenceSetB = Bvalue.difference(Avalue)

    differenceSetA.update(differenceSetB)

    for element in sorted(differenceSetA):
        print(element)



if __name__ == '__main__':
    n = int(input())
    arrA = list(map(int, input().split()))
    m = int(input())
    arrB = list(map(int, input().split()))
    symmetricDifference(set(arrA), set(arrB))