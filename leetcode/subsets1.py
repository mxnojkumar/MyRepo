def subset1(nums):
    res = []
    def helper(nums,i,subset):
        #base case
        if i==len(nums):
            res.append(subset.copy())
            return
        
        #excluded
        helper(nums,i+1,subset)
        subset.append(nums[i])
        #included
        helper(nums,i+1,subset)
        subset.pop()
        
    helper(nums,0,[])
    return res

nums=[1,2,3]
print(subset1(nums))