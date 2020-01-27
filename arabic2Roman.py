#Brian Macomber - U25993688
#EC500 - Assignment 1
#Sources referenced: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html



def main():
    userInput = input("Enter an arabic numeral: ")
    romanString = ""
    finalRomanString = arabic2Roman(int(userInput),romanString)
    print("The number %d in roman numerals is %s." % (int(userInput),finalRomanString))




def arabic2Roman(userInput, romanString):
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

main()
