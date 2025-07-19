"""Calculate prefix sum for natural numbers until n."""
def prefix_sum(n):
    if n <= 0:
        return

    prefix_sums = [1]
    
    for i in range(2, n):
        prefix_sums.append(
            prefix_sums[-1] + i
        )
    return prefix_sums

print(prefix_sum(10))