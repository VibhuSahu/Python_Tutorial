# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split())
UserFinalSet = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(sum((element in A) - (element in B) for element in UserFinalSet))