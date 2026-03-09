#FInd two numbers that add to a target

def two_sum(nums, target):
    index_map = {}  # value -> index

    for i, num in enumerate(nums):
        print(num)
        print(enumerate(nums))
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i

    return None  # if no solution

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # [0, 1]
