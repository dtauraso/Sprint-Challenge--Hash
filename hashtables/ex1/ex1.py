from collections import defaultdict

def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """

    packages = defaultdict(list)
    # print(packages)
    for i, weight in enumerate(weights):
        packages[limit - weight].append(i)
    for i, weight in enumerate(weights):
        if len(packages[weight]) < 2:
            packages[weight].append(i)

    # print('solution set')
    # [print(i, packages[i]) for i in packages]

    # pull all items of size 2 out
    pairs = [sorted(packages[i]) for i in packages if len(packages[i]) == 2]
    # print(pairs)
    solution = defaultdict(int)
    for i in pairs:
        solution[tuple(i)] += 1
    # print(solution)
    if len(solution.items()) > 0:

        my_items = []
        for item in solution:
            my_items.append(item)
        
        solution = list(my_items[0])

        if solution[0] < solution[1]:
            solution = [solution[1], solution[0]]
        # print(solution)
        # print(weights)
        return solution
        # return list(solution.)
    return None


# get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)