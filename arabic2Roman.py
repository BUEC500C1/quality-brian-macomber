#figure out how to take user input 

#use modulus for different levels of arabic numerals
#   M for 1000
#   C for 100
#   L for 50
#   X for 10
#   V for 5
#   I for 1
#special case: 4 (IV), 9(IX)


#start with empty string that we append on to the end each time
#write it recursively?



def main():
    userInput = input("Enter an arabic numeral: ")
    romanString = ""
    #print(type(userIn)
    finalRomanString = arabic2Roman(int(userInput),romanString)
    print("The number %d in roman numerals is %s." % (int(userInput),finalRomanString))




def arabic2Roman(userInput, romanString):
    if userInput == 0:
        romanString = romanString + "0"
        return romanString
    elif userInput == 1:
        romanString = romanString + "I"
        return romanString
    # elif userInput < 4:
    #     userInput = userInput - 1
    #     print(userInput)
    #     romanString = romanString + "I"
    #     arabic2Roman(userInput,romanString)
    # elif userInput == 4:
    #     romanString = romanString + "IV"
    #     return romanString 
    # if (userInput < 100) and (userInput >= 50):
    #     userInput % 50
    #     romanString + "L"
    #     arabic2Roman(userInput,romanString)

    # if userInput < 50 and userInput >= 10:
    #     userInput % 10
    #     romanString + "X"
    #     arabic2Roman(userInput,romanString)

    # if userInput < 100 and userInput >= 50:
    #     userInput % 50
    #     romanString + "L"
    #     arabic2Roman(userInput,romanString)

        
    # if userInput < 1000 and userInput >= 100:
    #     userInput % 100
    #     romanString + "C"
    #     arabic2Roman(userInput,romanString)
    # else:
    #     userInput%1000
    #     romanString + "M"
    #     arabic2Roman(userInput,romanString)


main()
