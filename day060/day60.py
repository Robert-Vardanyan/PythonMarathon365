def merge_sort(arr):
    """
    Sorts the array using merge sort algorithm and returns a new sorted list.
    """
    if len(arr) <= 1:
        return arr  # Base case: a list of zero or one elements is sorted

    mid = len(arr) // 2  # Find the midpoint
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half

    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    """
    Merges two sorted lists (left and right) into a single sorted list.
    """
    merged = []
    i = j = 0

    # Merge elements from left and right in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from left or right
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Example usage
if __name__ == "__main__":
    unsorted_list = [34, 7, 23, 32, 5, 62]
    sorted_list = merge_sort(unsorted_list)
    print("Unsorted:", unsorted_list)
    print("Sorted:", sorted_list)
