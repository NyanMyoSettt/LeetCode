class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val -> index
        
        for i, n in enumerate(nums):
            diff = target - n
            prevMap[n] = i
            if diff in prevMap:
                return [prevMap[diff], i]
            
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
