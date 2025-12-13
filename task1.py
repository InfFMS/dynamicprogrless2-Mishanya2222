def count_paths(start, target, forbidden):

    if start == forbidden:
        return 0


    max_n = max(target, 20) + 10
    L = [0] * (max_n + 1)
    L[start] = 1


    for x in range(start, target + 1):
        if x == forbidden:
            continue
        if L[x] == 0:
            continue

        if x + 1 <= max_n and x + 1 != forbidden:
            L[x + 1] += L[x]

        if x + 2 <= max_n and x + 2 != forbidden:
            L[x + 2] += L[x]

        if x * 2 <= max_n and x * 2 != forbidden:
            L[x * 2] += L[x]

    return L[target]

n = count_paths(3,7,10)
m = count_paths(7,20,10)
print(m*n)
