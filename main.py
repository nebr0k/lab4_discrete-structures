from math import factorial


def permutations(n):
    perm = [i for i in range(1, n+1)]

    print("".join(str(x) for x in perm))


    for i in range(1, factorial(n)):

        j = n - 2
        while perm[j] > perm[j+1]:
            j -= 1

        k = n - 1
        while perm[j] > perm[k]:
            k -= 1


        perm[j], perm[k] = perm[k], perm[j]


        l, r = j+1, n-1
        while l < r:
            perm[l], perm[r] = perm[r], perm[l]
            l += 1
            r -= 1


        print("".join(str(x) for x in perm))


def combinations(n, r):

    combination = list(range(1, r+1))


    print(combination)


    for i in range(1, int(factorial(n)/(factorial(r)*factorial(n-r)))):
        for j in range(r, 0, -1):
            if combination[j-1] < n - r + j:
                break
        combination[j-1] += 1
        for k in range(j, r):
            combination[k] = combination[k-1] + 1
        print(combination)


if __name__ == '__main__':
    permutations(5)
    n = int(input("Введіть значення n: "))
    r = int(input("Введіть значення r: "))
    combinations(n, r)
