def two_sum(numlist, target):
    #loop through the numlist:
    for idx, num in enumerate(numlist):
        print(f"{idx}: {num} looking for {target-num}")






if __name__ == "__main__":
    print(two_sum([2,7,11,15], 9))
    print(two_sum([3,2,4], 6))
