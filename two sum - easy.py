# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(numlist, target):
    for idx, num in enumerate(numlist):
        print(f"{idx}: {num} looking for {target-num}")
        for idx2, num2 in enumerate(numlist):
            if idx != idx2:
                if num2 == target - num:
                    return [idx, idx2]

if __name__ == "__main__":
    print(two_sum([2,7,11,15], 9))
    print(two_sum([3,2,4], 6))
