n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

c = a.difference(b)
print(len(c))