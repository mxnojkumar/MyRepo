def subset2(nums):
    res = []
    
    def helper(i,curr):
        #base case
        if i==len(nums):
            res.append(curr[:])
            return

        #including new values
        curr.append(nums[i])
        helper(i+1,curr)
        curr.pop()
        
        #excluding repeating values
        while i<len(nums)-1 and nums[i]==nums[i+1]:
            i+=1
            
        helper(i+1,curr)
        
    helper(0,[])    
    return res

#sample case
print(subset2([1,2,2]))