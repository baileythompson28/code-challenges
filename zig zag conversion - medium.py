"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility) 
P   A   H   N 
A P L S I I G 
Y   I   R 
And then read line by line: "PAHNAPLSIIGYIR" 
Write the code that will take a string and make this conversion given a number of rows: 
string convert(string s, int numRows); 

The Zig Zag Conversion problem involves converting a string into a zigzag pattern based on a specified number of rows. 
How it works:
The string is written in a zigzag pattern on a given number of rows, such as "PAYPALISHIRING" on 3 rows.
The pattern reads line by line, resulting in a new string like "PAHNAPLSIIGYIR" for numRows = 3.
The algorithm typically involves iterating through the string and applying a direction variable to determine the movement across the rows. 

"""

def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    current_row = 0
    down = False

    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == numRows - 1:
            down = not down
        current_row += 1 if down else -1

    return ''.join(rows)

if __name__ == "__main__":
    input_string = input("Enter string to convert: ")
    num_rows = int(input("Enter number of rows: "))
    result = convert(input_string, num_rows)
    print(f"Converted: {result}")