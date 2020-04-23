def main():
    T = int(input())
    while T > 1:
        T -= 1
        count = 0
        k = 0
        no_of_members = int(input())
        teamA = input()
        list_teamA = [int(x.strip()) for x in teamA.split()]
        teamB = input()
        list_teamB = [int(x.strip()) for x in teamB.split()]
        list_teamA.sort(reverse=True)
        list_teamB.sort(reverse=True)
        for i in range(no_of_members):
            for j in range(k, no_of_members):
                if list_teamA[i] > list_teamB[j]:
                    count += 1
                    k = j + 1
                    break
        print(count)


main()
