# permutation with alike elements
# solved by using backtracking method with hashmap - controlled recursion + abandoning misleading solutions
# similar space and time complexities as compared with normal permutation

def permute_unique(nums):
    n = len(nums)
    res = []
    def helper(i):
        if i == n-1:
            res.append(nums[:])
            return
        hashmap = {}
        for j in range(i, n):
            if nums[j] not in hashmap:
                hashmap[nums[j]] = True
                nums[i], nums[j] = nums[j], nums[i]
                helper(i+1)
                nums[i], nums[j] = nums[j], nums[i]
    helper(0)
    return res
    
print(permute_unique([1,2,3]))
print(permute_unique([1,1,2]))