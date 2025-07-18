def array_prefix_sum(arr):
    if len(arr) == 0:
        return

    prefix_sums = [arr[0]]

    for i in range(1, len(arr)):
        prefix_sums.append(
            prefix_sums[-1] + arr[i]
        )

    return prefix_sums

arr = array_prefix_sum([5, 10, 15, 20, 25, 30, 35, 40, 45, 60])
print(arr)

# sum of numbers from position 3 to position 7:
print(arr[6] - arr[3-2])

print(sum([15, 20, 25, 30, 35]))