def prefix_sum(n):
    arr = [1]
    for i in range(1, n):
        arr.append(
            arr[-1] + i + arr[0]
        )
    return arr

arr = prefix_sum(10)

print(arr)

# what is the sum of all natural numbers between 2 and 5 inclusive?
print(arr[5] - arr[1])
