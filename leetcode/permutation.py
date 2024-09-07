# permutation of a given array
# solved by backtracking method - controlled recursion
# efficient in space handling but higher time complexities

def permute(nums):
    n = len(nums)
    res = []
    def helper(i):
        if i == n-1:
            res.append(nums[:])
            return
        for j in range(i, n):
            nums[i], nums[j] = nums[j], nums[i]
            helper(i+1)
            nums[i], nums[j] = nums[j], nums[i]
    helper(0)
    return res

print(permute([1, 2, 3]))