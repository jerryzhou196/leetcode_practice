# Function to find the prefix sum array
def findPrefixSum(arr):
    n = len(arr)

    # to store the prefix sum
    prefixSum = [0] * n

    # initialize the first element
    prefixSum[0] = arr[0]

    # Adding present element with previous element
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]

    return prefixSum


if __name__ == "__main__":
    arr = [10, 20, 10, 5, 15]
    prefixSum = findPrefixSum(arr)
    for i in prefixSum:
        print(i, end=" ")
