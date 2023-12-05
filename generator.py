import random
from helper import save

def generate_data(n, low, high):
    data = []
    for i in range(n):
        data.append(random.randint(low, high))
    return set(data)

ukuran = [20,200,2000]
subset = [15, 20, 25]

tipe = ['Small', 'Medium', 'Large']

for i in range(len(ukuran)):
    # assign universe nya terlebih dahulu
    universe = set(range(1, ukuran[i]+1))

    for j in range(len(subset)):
        # buat subset" nya
        dataset = []
        test_set = set()
        while test_set != universe: # selama belom jadi  universe
            dataset = []
            test_set = set()
            for k in range(subset[j]):
                size = random.randint(ukuran[i]//5, ukuran[i]//2)
                x = generate_data(size, 1, ukuran[i])
                dataset.append(x)
                test_set |= x
        costs = [random.randint(1, 100) for _ in range(subset[j])]
        save(f"dataset/{tipe[i]}_{subset[j]}.txt", dataset, costs)