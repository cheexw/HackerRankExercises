def formingMagicSquare(s):
    # Write your code here
    magic_square = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    cost_list = []

    for a in magic_square:
        cost = 0
        for b in range(1, 4):
            for c in range(1, 4):
                cost += abs(a[b - 1][c - 1] - s[b - 1][c - 1])

        cost_list.append(cost)

    return min(cost_list)


if __name__ == '__main__':
    s = [[4,8,2], [4,5,7], [6,1,6]]

    result = formingMagicSquare(s)

    print(result)