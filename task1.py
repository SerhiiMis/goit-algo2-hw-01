def find_min_max(arr):
    if not arr:
        raise ValueError("Array cannot be empty")
    
    def helper(start, end):
        if start == end:
            return arr[start], arr[start]
        elif end - start == 1:
            return (min(arr[start], arr[end]), max(arr[start], arr[end]))
        else:
            mid = (start + end) // 2
            min1, max1 = helper(start, mid)
            min2, max2 = helper(mid + 1, end)
            return (min(min1, min2), max(max1, max2))

    return helper(0, len(arr) -1)

# Example usage
if __name__ == "__main__":
    example = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_min_max(example)) # Output: (1, 9)

