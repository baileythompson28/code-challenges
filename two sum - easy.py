# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(numlist, target):
    numlist = input("Enter a list of numbers separated by commas: ").split(",")
    numlist = [int(num) for num in numlist]
    for idx, num in enumerate(numlist):
        print(f"{idx}: {num} looking for {target-num}")
        for idx2, num2 in enumerate(numlist):
            if idx != idx2:
                if num2 == target - num:
                    return [idx, idx2]

if __name__ == "__main__":
    target = int(input("Enter the target sum: "))
    result = two_sum([], target)
    print(f"Output that adds up to {target}: {result}")
