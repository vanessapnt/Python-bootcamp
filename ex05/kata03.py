kata = "The right format"

def main():
    dashes_nbr = 42 - len(kata)
    result = dashes_nbr * '-' + kata
    print(result, end="")

main()