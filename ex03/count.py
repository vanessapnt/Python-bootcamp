import sys

def text_analyzer (str):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''
    if len(sys.argv) == 1 or sys.argv[1] == "":
        user_input = input("What is the text to analyze?")
    else:
        user_input = sys.argv[1:]
    printable = 0
    upper_char = 0
    lower_char = 0
    punctuation = 0
    spaces = 0

    for char in user_input:
        if char.isprintable() == False:
            break
        else
            printable+= 1
        if char.isupper():
            upper_char+= 1
        elif char.islower():
            lower_char+= 1
        elif char.punctuation():
            punctuation+= 1
        elif char.isspace():
            spaces+= 1
    print(The text contains {printable} printable character(s):)
    print(- {upper_char} upper letter(s))
    print(- {lower_char} lower letter(s))
    print(- {punctuation} punctuation mark(s))
    print(- {spaces} space(s))
