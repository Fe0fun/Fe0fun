from typing import List


def prod_non_zero_diag(X: List[List[int]]) -> int:
    """
    Compute product of nonzero elements from matrix diagonal, 
    return -1 if there is no such elements.
    """
    prod = 0
    for i in range(len(X)):
        if len(X[i])-1 >= i:
            if X[i][i] != 0:
                if prod == 0:
                    prod = 1
                prod *= X[i][i]
    if prod != 0:
        return prod
    else:
        return -1
    pass


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    """
    Return True if both 1-d arrays create equal multisets, False if not.
    """
    x.sort()
    y.sort()
    return(x == y)


def max_after_zero(x: List[int]) -> int:
    """
    Find max element after zero in 1-d array, 
    return -1 if there is no such elements.
    """
    zlist = []
    if len(x) == 0: return -1
    for i in range(len(x)):
        if x[i] == 0: zlist.append(i)
    if len(zlist) == 0: return -1
    if len(x)-1 > zlist[0]:
        max = x[zlist[0]]
    else:
        return -1
    for item in zlist:
        if len(x)-1 > item:
            if x[item+1] > max: max = x[item+1]
    return max


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    """
    Sum up image channels with weights.
    """
    pass


def run_length_encoding(x: List[int]) -> (List[int], List[int]):
    """
    Make run-length encoding.
    """
    result_items = []
    frequency = []
    encountered = 1
    item = x[0]
    for i in range(1, len(x)):
        if x[i] == item:
            encountered += 1
        else:
            result_items.append(item)
            frequency.append(encountered)
            item = x[i]
            encountered = 1
    result_items.append(item)
    frequency.append(encountered)
    return (result_items, frequency)
    pass


def pairwise_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    """
    Return pairwise object distance.
    """
    pass

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
    print(prod_non_zero_diag(matrix))
    a = [1, 2, 2, 4]
    b = [4, 2, 2, 1]
    print(are_multisets_equal(a, b))
    l = [0]
    print(max_after_zero(l))
    items = [1, 1, 2, 3, 4, 2]
    run_length_encoding((items))