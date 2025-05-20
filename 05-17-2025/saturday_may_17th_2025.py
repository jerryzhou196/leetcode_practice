def segregate0and1(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        while arr[lo] == 0 and lo < hi:
            lo += 1
        while arr[hi] == 1 and lo < hi:
            hi -= 1
        if lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo += 1
            hi -= 1

def sort012(arr):
    n = len(arr)
    lo = 0
    hi = n - 1
    mid = 0

    # Iterate till all the elements are sorted
    while mid <= hi:
      if arr[mid] == 0:
        arr[lo], arr[mid] = arr[mid], arr[lo]
        lo = lo + 1
        mid = mid + 1
        
      elif arr[mid] == 1:
        mid = mid + 1
        
      else:
        arr[mid], arr[hi] = arr[hi], arr[mid]
        hi = hi - 1
        
    return arr



arr = [0, 1, 2, 0, 1, 2] 
for x in arr:
    print(x, end=" ")
sort012(arr)
print("Array after segregation:", arr)

if __name__ == "__main__":
    main()
