for _ in range(int(input())):
    size = int(input())
    g = list(map(int, input().split()))
    g.sort()
    opponent = list(map(int, input().split()))
    opponent.sort()
    count = 0
    k = size - 1
    for i in range(size - 1, -1, -1):
        for j in range(k, -1, -1):
            if opponent[j] < g[i]:
                count = count + 1
                k = j - 1
                break
    print(count)
