n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    commands = list(map(str, input().split()))
    if (commands[0] == "discard"):
        s.discard(int(commands[1]))
    elif (commands[0] == "remove"):
        s.remove(int(commands[1]))
    else:
        s.pop()

print(sum(s))