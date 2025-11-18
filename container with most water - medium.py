"""You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
· eg. in the example below, the coordinates of the two red lines are (1,0) to (1, 8) and (8,0) and (8,7)
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container."""

from typing import List

def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_water = width * current_height
        max_water = max(max_water, current_water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

if __name__ == "__main__":
    heights = list(map(int, input("Enter heights (separated by spaces): ").split()))
    result = max_area(heights)
    print(f"Maximum amount of water the container can store is: {result}")