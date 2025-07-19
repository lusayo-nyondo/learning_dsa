import timeit

setup_code = """
def get_prefix_sum_of(arr):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    return prefix_sum

def get_prefix_sum_dynamic_growth(arr):
    prefix_sum = [arr[0]]
    for i in range(1, len(arr)):
        prefix_sum.append(
            prefix_sum[-1] + arr[i]
        )
    return prefix_sum

data = range(1, 10000000)
"""

# Test get_prefix_sum_of
time_preallocated = timeit.timeit(
    "get_prefix_sum_of(data)",
    setup=setup_code,
    number=100 # Run 1 million times
)
print(f"Time for get_prefix_sum_of: {time_preallocated:.6f} seconds")

# Test get_prefix_sum_dynamic_growth
time_dynamic = timeit.timeit(
    "get_prefix_sum_dynamic_growth(data)",
    setup=setup_code,
    number=100  # Run 1 million times
)
print(f"Time for get_prefix_sum_dynamic_growth: {time_dynamic:.6f} seconds")
