"""
For an array A of size 'n', the prefix sum of that array is another
array P also of size 'n' such that:
    P[0] = A[0]
    P[i] = A[i] + A[i - 1] + A[i - 2] ... + A[0] where i > 0 and < n.
"""
import profile

def get_prefix_sum_of(arr):
    """Get prefix sum using preallocated array."""
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]

    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    return prefix_sum


def get_prefix_sum_dynamic_growth(arr):
    """Get prefix sum using dynamic array growth."""
    prefix_sum = [arr[0]]
    
    for i in range(1, len(arr)):
        prefix_sum.append(
            prefix_sum[-1] + arr[i] 
        )

    return prefix_sum


profile.run(
    "print(get_prefix_sum_dynamic_growth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))"
)

profile.run(
    "print(get_prefix_sum_of([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))"
)
