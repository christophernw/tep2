def save(filename, dataset, costs):
    with open(filename, 'w') as file:
        for i in range(len(dataset)):
            for x in dataset[i]:
                file.write(f'{x} ')
            file.write(f'{costs[i]}\n')

def load(filename):
    universe = set()
    subset = []
    costs = []
    with open(filename, 'r') as f:
        for line in f:
            array = [int(x) for x in line.split()]
            universe |= set(array[:-1])
            subset.append(set(array[:-1]))
            costs.append(array[-1])
    return universe, subset, costs
