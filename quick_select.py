import random

def quick_select(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k is out of bounds")
    
    def select(left, right):
        pivot_index = random.randint(left, right)
        pivot_value = arr[pivot_index]
        # Move pivot to the end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        # Move pivot to its final place
        arr[right], arr[store_index] = arr[store_index], arr[right]

        if store_index == k - 1:
            return arr[store_index]
        elif store_index > k - 1:
            return select(left, store_index - 1)
        else:
            return select(store_index + 1, right)   
        
    return select(0, len(arr) - 1)

# Example usage
if __name__ == "__main__":
    example = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    k = 5
    print(quick_select(example, k)) # Output: 3 (the 5th smallest element)