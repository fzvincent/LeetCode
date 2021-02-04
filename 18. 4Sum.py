

def foursum(nums):
    nums.sort()
    if len(nums) == 0 or nums[0] * 4 > target or target > nums[-1] * 4:
        return []

    res = set()
    for i, m in enumerate(nums[:-3]):

        # if i>=1 and m == nums[i-1]:
        #     continue

        for j, n in enumerate(nums[i + 1:-2]):
            # if j>=i+2 and n == nums[j-1]:
            #     continue
            j = j + i + 1
            d = {}
            for x in nums[j + 1:]:
                if x in d:
                    res.add((m, n, x, -(m + n + x)))
                else:
                    d[-(m + n + x)] = 1
    return res

nums=[1,0,-1,0,-2,2]
print(foursum(nums))