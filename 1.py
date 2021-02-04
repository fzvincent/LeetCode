def twoSumHashing(num_arr, pair_sum):
    sums = []
    hashTable = {}

    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            return ([i, num_arr.index(complement)])
        hashTable[num_arr[i]] = num_arr[i]


# Driver Code
num_arr = [4, 5, 1, 8]
pair_sum = 9

# Calling function
print(twoSumHashing(num_arr, pair_sum))