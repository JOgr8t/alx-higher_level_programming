#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Newsquare = []
    i = 0
    for a in matrix:
        Newsquare.append([])
        for b in matrix[i]:
            Newsquare[i].append(b**2)
        i += 1
    return (Newsquare)
