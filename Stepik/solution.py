from collections import Counter

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        N = len(nums)
        for i in range(1, N):
            nums[i] += nums[i - 1]
        return nums
    
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        N = len(accounts)
        for i in range(N):
            accounts[i] = sum(accounts[i])
        return max(accounts)
            
    def fizzBuzz(self, n: int) -> list[str]:
        nums = list(map(str, range(1, n + 1)))
        for i in range(len(nums)):
            if int(nums[i]) % 3 == 0 and int(nums[i]) % 5 == 0:
                nums[i] = 'FizzBuzz'
            elif int(nums[i]) % 3 == 0:
                nums[i] = 'Fizz'
            elif int(nums[i]) % 5 == 0:
                nums[i] = 'Buzz'
        return nums

    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num /= 2
            counter += 1
        return counter
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict = Counter(ransomNote)
        magazineDict = Counter(magazine)

        for k in ransomNoteDict:
            magazineDict[k] = magazineDict.get(k, 0) - ransomNoteDict[k]
            if magazineDict[k] < 0:
                return False
        
        return True