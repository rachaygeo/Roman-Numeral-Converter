# number to roman numerals function
# returns: list
def num_to_rn(rn_dict, num):
    # list of roman numerals
    rn = []

    for i, letter in enumerate(rn_dict.keys()):
        # counts each time the same letter is added
        frequency = 0
        counter = 0
        rn_value = rn_dict.get(letter)

        # checks if current roman numeral value is lesser than or equal to the number
        while num % rn_value != num:
            rn.append(letter)
            num -= rn_value
            counter += rn_value
            frequency += 1

            # if the frequency of the roman numeral is more than three (so 4) and isn't 'M'
            # then involves subtractive notation
            if (frequency == 4) and (i != 0):

                # if 5 of the current repeating roman numeral values plus the value of the letter in rn before them
                # don't add up to the value of the letter at i-2 or the size of rn is 4
                # (since there is no letter preceding the repeating letters in rn)
                if (len(rn) == 4) or (counter + rn_value + rn_dict.get(rn[-5]) != list(rn_dict.values())[i - 2]):
                    del rn[-3:]
                    rn.append(list(rn_dict.keys())[i - 1])
                else:
                    # if 5 of the current repeating roman numeral values plus the value of the letter in rn before them
                    # add up to the value of the letter at i-2
                    del rn[-5:]
                    rn.append(letter)
                    rn.append(list(rn_dict.keys())[i - 2])
    return rn


# converts a list to a string
def list_to_str(list):
    str = ""
    for i in range(len(list)):
        str += list[i]
    return str


# roman numerals to number function
# returns: integer
def rn_to_num(input):
    num = 0
    return num


def main(input):
    # roman numeral letters and their corresponding values
    rn_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    try:
        # check if input is a string
        input.isalpha()
        return rn_to_num(input)
    except AttributeError:
        return list_to_str(num_to_rn(rn_dict, input))


print(main(94))
