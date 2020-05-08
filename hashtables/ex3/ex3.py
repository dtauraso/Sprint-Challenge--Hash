from collections import defaultdict
def intersection(arrays):

    """
    YOUR CODE HERE
    """
    frequency = defaultdict(int)

    for array in arrays:
        for number in array:
            frequency[number] += 1
    # [print(i, frequency[i]) for i in frequency]
    # only numbers with frequency == total number of arrays
    # are in the intersection
    result = [i for i in frequency
                        if frequency[i] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
