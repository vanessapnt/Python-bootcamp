import sys

#slice of the string s : s[start:end:step]
def reverse_and_swap_case(s):
    return s[::-1].swapcase()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python program.py <string>")
    else:
        merged_str = ' '.join(sys.argv[1:])
        result = reverse_and_swap_case(merged_str)
        print(result)
#print(result, end="") for no new line
