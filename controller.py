import time
import csv
import statistics

from routines.routine_1 import fut1, casemaker1
from routines.routine_2 import fut2, casemaker2
from routines.routine_3 import fut3, casemaker3
from routines.routine_4 import fut4, casemaker4
from routines.routine_5 import fut5, casemaker5

futs = [fut1, fut2, fut3, fut4, fut5]
casemakers = [casemaker1, casemaker2, casemaker3, casemaker4, casemaker5]
sample_size = 2
case_sizes = [24]

def main():
    for routine in range(3,4):
        stats = []
        routine_start = time.perf_counter_ns()

        for n in case_sizes:
            test_times = []
            for a in range(sample_size):
                test_data = casemakers[routine](n)
                start = time.perf_counter_ns()
                futs[routine](test_data)
                end = time.perf_counter_ns()
                test_times.append((end - start)/1000)
            
            sorted(test_times)
            stats.append([
                n,
                statistics.mean(test_times),
                statistics.median(test_times),
                statistics.quantiles(test_times),
                statistics.stdev(test_times)
            ])
            print(n)

            if routine == 3 and n >= 24:
                break

        routine_end = time.perf_counter_ns()
        routine_time = ((routine_end - routine_start)/(3600000000000))

        #with open(f'A1_R{(routine + 1)}.csv', 'w') as file:
        with open(f'A1_R4_1.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['case size', 'mean', 'median', 'quartiles', 'standard deviation'])
            for row in stats:
                writer.writerow(row)

        with open('times.txt', 'a') as f:
            f.write(f'{(routine + 1)}:{routine_time} hours ({sample_size})\n')

if __name__ == "__main__":
    main()