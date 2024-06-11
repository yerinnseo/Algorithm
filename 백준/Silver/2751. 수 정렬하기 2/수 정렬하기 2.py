import sys

data = sys.stdin.read().split()

n = int(data[0])

numbers = [int(data[i]) for i in range(1, n + 1)]

numbers.sort()

sys.stdout.write('\n'.join(map(str, numbers)) + '\n')