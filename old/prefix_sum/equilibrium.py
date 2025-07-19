"""
Given an array, find if it has an equilibrium such that
all elements before it have the same sum of all elements after it.
"""

def has_equilibrium(arr):
    prefix_sum = [arr[0]]

    for i in range(1, len(arr)):
        prefix_sum.append(
            prefix_sum[-1] + arr[i]
        )

    for i, _ in enumerate(prefix_sum):
        left_sum = prefix_sum[i - 1] if i > 0 else 0
        right_sum = prefix_sum[-1] - prefix_sum[i] if i < len(prefix_sum) - 1 else 0

        if left_sum == right_sum:
            return True

    return False

def has_equilibrium_no_prefix_sum(arr):
    suffix_sum = sum(arr)
    left_sum = 0

    for e in arr:
        if left_sum == suffix_sum - e:
            return True
        else:
            suffix_sum -= e
            left_sum += e

    return False

print(has_equilibrium([3, 4, 8, -9, 20, 6]))
print(has_equilibrium([1, 1]))
print(has_equilibrium([4, 2, -2]))

print(has_equilibrium_no_prefix_sum([3, 4, 8, -9, 20, 6]))
print(has_equilibrium_no_prefix_sum([1, 1]))
print(has_equilibrium_no_prefix_sum([4, 2, -2]))
