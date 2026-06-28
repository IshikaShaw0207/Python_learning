def twosum(nums, target):
    mp={}
    for i in range(len(nums)):
        complement= target-nums[i]

        if complement in mp:
            return [mp[complement],i]
        mp[nums[i]]=i
     

nums=[2,7,11,15]
target=9
print(twosum(nums, target))