# Brian Macomber - U25993688
# EC500 - Assignment 1
# Sources referenced: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html


def arabic2Roman(userInput):

    # catching empty and corner cases
    if not isinstance(userInput,int):
        print("The input was not an integer, please enter an integer")
        return ""
    if userInput == "":
        print("The input was empty, please enter an arabic numeral")
        return ""
    if userInput > 3999 or userInput < 0:
        print("The input is out of range, enter a num between 0 and 3999")
        return ""
    if userInput == 0:
        return 0

    # Main part of the program starts here

    romans = ["M", "CM", "D", "CD",
              "C", "XC", "L", "XL", "X",
              "IX", "V", "IV", "I"
    ]
    ints = [1000, 900, 500, 400,
            100, 90, 50, 40, 10,
            9, 5, 4, 1
    ]

    romanNumString = ""
    for i in range(len(ints)):
        freq = int(userInput/ints[i])
        romanNumString = romanNumString + (freq*romans[i])
        userInput-=(freq*ints[i])
    
    return romanNumString