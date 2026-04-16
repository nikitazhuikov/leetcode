class Solution:
    def rob(self, nums: list[int]) -> int:
        best_vals = [0]*(len(nums)+1) 
        for i in range(len(nums)):
            current_value = nums[i]
            if i == 0:
                best_vals[i+1] = current_value
            else:
                best_vals[i+1] = max(current_value + nums[i-2], best_vals[i])
        return best_vals[len(nums)]

if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([2,7,9,3,1]))
    print(sorted([2,7,9,3,1]))