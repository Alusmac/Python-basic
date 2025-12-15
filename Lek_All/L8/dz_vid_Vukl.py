piramida = [
    [7],
    [5, 8],
    [9, 8, 2],
    [1, 3, 5, 6],
    [6, 2, 4, 4, 5],
    [9, 5, 3, 5, 5, 7],
    [7, 4, 6, 4, 7, 6, 8],
]


def max_cent(a, b):
    if a == len(piramida) - 1:
        return piramida[a][b]
    return piramida[a][b] + max(max_cent(a + 1, b), max_cent(a + 1, b + 1))


print("Max кількість злитків:", max_cent(0, 0))
