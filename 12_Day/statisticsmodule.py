from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

# when importing them like this instead of import statistics
# you can directly use their function names
# however incase:
# import statistics

# ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

# print(statistics.mean(ages))
# print(statistics.median(ages))
# print(statistics.mode(ages))
# print(statistics.stdev(ages))