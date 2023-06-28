#!/usr/bin/python3
''' Python module for calculating Pascal's triangle'''


def pascal_triangle(n):
    ''' python function to calculate pascal's triangle and return n rows. '''

    if n <= 0:
        return []
    else:
        container = []
        for i in range(n + 1):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                elif i > 1 and j > 0 and j != i - 1:
                    row.append(container[i - 1][j] + container[i - 1][j - 1])
            container.append(row)
    return container
