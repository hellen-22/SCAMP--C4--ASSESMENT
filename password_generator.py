import random
import array
import string
#"""A function to convert a list to string"""
def conversion(s):
    str = ""
    return(str.join(s))
#"""To make the password have a minimum of 6 characters"""
min_lenght = 6
lenght = int(input("How long do you want your password to be? "))
if lenght < min_lenght:
    print("INVALID!YOUR PASSWORD SHOULD HAVE A MINIMUM OF 6 CHARACTERS")
else:
    up_case = int(input("How many uppercase letters do you want your password to contain? "))
    low_case = int(input("How many lowercase letters do you want your password to contain? "))
    numbers = int(input("How many numbers do you want your password to contain? "))
    symbol = int(input("How many symbols do you want? "))

    if lenght != up_case + low_case + numbers + symbol :
        print("INVALID INPUT")
    else:    
        digits = string.digits
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        symbols = string.punctuation
    #"""A list of the randomly selected characters in the given range"""
        digitss = []
        for num in range(numbers):
            digitss.append(random.choice(digits))

        lower_cases = []    
        for low in range(low_case):
            lower_cases.append(random.choice(lower_case))

        upper_cases = []    
        for up in range(up_case):
            upper_cases.append(random.choice(upper_case)) 

        symbolss = []    
        for s in range(symbol):
            symbolss.append(random.choice(symbols))

    #"""Converting the lists created to strings"""
        final_digit = conversion(digitss)
        final_lower_case = conversion(lower_cases)
        final_upper_case = conversion(upper_cases)
        final_symbol = conversion(symbolss)

        combination = final_digit + final_lower_case + final_upper_case + final_symbol
        
        for x in range(lenght):
            temp_pass_list = array.array('u', combination)
            random.shuffle(temp_pass_list)

        password = ""
        for x in temp_pass_list:
                password += x
                
        print(password)