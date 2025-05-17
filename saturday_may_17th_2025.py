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

arr = [0, 1, 0, 1, 1, 1]
segregate0and1(arr)
print("Array after segregation:", arr)

if __name__ == "__main__":
    main()
