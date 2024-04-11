# number to roman numerals function
# returns: string
def num_to_rn(input):
    num = 0
    return num


# roman numerals to number function
# returns: integer
def rn_to_num(input):
    rn = ""
    return rn


def main(input):
    # roman numeral letters and their corresponding values
    rn_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    # check if input is a number
    if input.isNumeric():
        return num_to_rn(input)
    # number to roman numerals
    else:
        return rn_to_num(input)
