def solution(nums, k):
    s = sum(nums[:k])
    max_s = s    

    for i in range(len(nums)-k):
        s = s - nums[i] + nums[i+k]
        if s > max_s:
            s = max_s
    
    return max_s / k

cases = [
    ([1,12,-5,-6,50,3], 4)
]

for c, k in cases:
    r = solution(c, k)
    print(r)