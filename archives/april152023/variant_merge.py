def k_merge_sort(arr, k):
    # Base case, array is either empty or a single element
    if len(arr) <= 1:
        return arr

    # Split the array into k subarrays
    subarrays = [arr[i::k] for i in range(k)]

    # Recursively sort each subarray
    for i in range(k):
        subarrays[i] = k_merge_sort(subarrays[i], k)

    # Merge the sorted subarrays
    return merge_pairs(subarrays)


def merge_pairs(subarrays):
    # Base case, single array is already merged
    if len(subarrays) == 1:
        return subarrays[0]

    merged = []
    # Merge each pair of arrays
    for i in range(0, len(subarrays), 2):
        merged.append(merge(subarrays[i], subarrays[i + 1]))

    # Merge the merged pairs
    return merge_pairs(merged)


def merge(left, right):
    # Merge two sorted lists
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


print(k_merge_sort([8, 6, 5, 7, 3, 1, 2, 4], 4))
