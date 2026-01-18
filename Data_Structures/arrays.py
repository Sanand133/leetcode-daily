'''
Data Structure: Arrays
Language: Python
Purpose: LeetCode practice with optimized solutions
'''

# --------------------------------------------------
# Problem 1: Two Sum
# LeetCode: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Approach: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
# --------------------------------------------------

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i

# --------------------------------------------------
# Problem 2: Best Time to Buy and Sell Stock
# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Approach: Track minimum price
# Time Complexity: O(n)
# Space Complexity: O(1)
# --------------------------------------------------

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
