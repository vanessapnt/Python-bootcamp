import string
import sys

# == compares the values
# is compares the memory 
# In Python, None is a unique object (there is only one None in memory)

# If the caller doesn't pass a value for text, the function will use None.
# It allows the function to handle cases where no argument is provided without raising an error. 
def text_analyzer (text=None):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''
    if text is None:
        text = input("What is the text to analyze?\n")
    if not isinstance(text, str):
        print("Error: The argument must be a string.")
        return
    printable = 0
    upper_char = 0
    lower_char = 0
    punctuation = 0
    spaces = 0

    for char in text:
        if char.isprintable():
            printable+= 1
        if char.isupper():
            upper_char+= 1
        elif char.islower():
            lower_char+= 1
        elif char in string.punctuation:
            punctuation+= 1
        elif char.isspace():
            spaces+= 1
    print(f"The text contains {printable} printable character(s):")
    print(f"- {upper_char} upper letter(s)")
    print(f"- {lower_char} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {spaces} space(s)")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error: Too many arguments.")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()