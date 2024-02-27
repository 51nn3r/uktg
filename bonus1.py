from typing import Dict
from typing import List

import re

n = input()
num_exp = r'^(0|[1-9]\d*)$'
if not re.search(num_exp, n):
    raise "invalid input"

n = int(n)
nums: Dict[int, List[int]] = {0: []}

exponent = 0

for prev in range(n):
    current = prev + 1

    while 4 ** (exponent + 1) <= current:
        exponent += 1

    e_element = 4 ** exponent
    difference = current - e_element
    seq = nums[difference].copy()
    k = len(seq)
    exp_index = exponent + 1

    if k < exp_index:
        if (exp_index - k) % 2 == 0:
            nums[current] = seq + [4, -1] * ((exponent - k) // 2) + [4]
        else:
            nums[current] = seq + [4, -1] * ((exponent - k) // 2) + [1]

    elif seq[exponent] == -1:
        if exponent == k - 1:
            nums[current] = seq[:-1]
        elif exponent == k - 2:
            nums[current] = seq[:-2] + [4]
        else:
            print('[-] -1 error', exponent, k)

    elif seq[exponent] == 1:
        nums[current] = seq[:-1] + [6, -1]
    elif seq[exponent] == 4:
        nums[current] = seq[:-1] + [1, 1]
    elif seq[exponent] == 6:
        nums[current] = seq[:-2] + [-1, 1]

    if current != sum(a * (4 ** i) for a, i in zip(nums[current], [j for j in range(len(nums[current]))])):
        print(f'[-] error for {current}')

print(nums[n])
