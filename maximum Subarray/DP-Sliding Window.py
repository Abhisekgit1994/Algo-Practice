"""
Data created : 03-01-2022
@Abhisek
"""


# Given an integer array nums, find the contiguous subarray /
# (containing at least one number) which has the largest sum and return its sum.

class Solution:
    def simpleApproach(self, arr):  # Time complexity O(n^2)
        n = len(arr)
        maxSum = -float('inf')
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]
                maxSum = max(curr_sum, maxSum)
        return maxSum

    def dynamicProgram(self, arr):  # Time complexity O(n) , SPace complexity O(n)
        l = [0]*len(arr)
        n = len(arr)
        l[0] = arr[0]
        for i in range(1, n):
            l[i] += max(l[i-1]+arr[i], arr[i])
        return max(l)

    def kadaneSolution(self, arr):  # Sliding window implementation :# Time complexity O(n) , SPace complexity O(1)
        curr_sum = arr[0]
        max_sum = -float('inf')
        for i in arr[1:]:
            curr_sum = max(i, curr_sum + i)
            max_sum = max(curr_sum, max_sum)
        return max_sum


if __name__ == '__main__':
    arr = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [5, 4, -1, 7, 8]]
    sol = Solution()
    t = 1
    for a in arr:
        print(f"******************TEST CASE {t}*********************")
        print(f"Output of running all the algos on the arr {a} are:")
        print("Simple Approach:", sol.simpleApproach(a))
        print("Dynamic Approach:", sol.dynamicProgram(a))
        print("Kadane's Solution", sol.kadaneSolution(a))
        t += 1


