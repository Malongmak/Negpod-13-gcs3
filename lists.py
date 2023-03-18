def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return (seen[target - num], i)
        seen[num] = i

print(two_sum([2, 7, 11, 15], 9)) 
print(two_sum([3, 2, 4], 6)) 
print(two_sum([3, 3], 6)) 
