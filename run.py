import sys
import time

from greedy import set_cover
from branch_and_bound import BB
from memory_profiler import memory_usage
from helper import load

def main_cover(cover_function, arr):
    memory_usages = memory_usage((time_main_cover, (cover_function, arr)), max_iterations=1)
    print(f'{max(memory_usages)} MB')

def time_main_cover(cover_function, arr):
    start_time = time.time()
    final = cover_function(arr[0], arr[1], arr[2])
    end_time = time.time()

    print(f'Minimum Cost = {final[1]}')
    print(f'{(end_time - start_time) * 1000} ms\n')

def main():
    tipe = ['Small', 'Medium', 'Large']

    subset = [15, 20, 25]
    dataset = {}
    
    for i in tipe:
        for n in subset:
            dataset[f'{i}_{n}'] = load(f'dataset/{i}_{n}.txt')
    
    for i in tipe:
        for n in subset:
            print(f'Greedy {i}_{n}')
            main_cover(set_cover, dataset[f'{i}_{n}'])
            print()
            print(f'Branch and Bound {i}_{n}')
            main_cover(BB, dataset[f'{i}_{n}'])
            print()

if __name__ == '__main__':
    sys.setrecursionlimit(2**17)
    main()