n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

c = a.union(b)
print(len(c))