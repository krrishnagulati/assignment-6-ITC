class ThreeSum:
    def find_three_sum(self, nums):
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        
        return result


three_sum = ThreeSum()
nums = [-25, -10, -7, -3, 2, 4, 8, 10]
result = three_sum.find_three_sum(nums)
print(result)
