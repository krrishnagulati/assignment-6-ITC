'''
Write a Python function that checks whether a passed string is palindrome or not. Note:
A palindrome is a word, phrase, or sequence that reads the same backward as forward,
e.g., madam or nurses run.
'''
def palindrome(str):
    str = str.replace(" ","").lower()   # here we are removing whitespaces and converting them to lower case 
    return str == str[::-1]          # this is done to check whether the str is reversed or not 
                                        # replace and lower are built in methods of strings

# here we are calling the function 
print(palindrome("naman"))
print(palindrome("madam"))
print(palindrome("nurses run"))
print(palindrome("python"))




       