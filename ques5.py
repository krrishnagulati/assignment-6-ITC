'''
Write a Python function that accepts a hyphen-separated sequence of words as input
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''

def hyphen_separated(sequence):
    words = sequence.split("-")
    sorted_words = sorted(words)   # sorted function helps in arranging in alphabetical order
    result = "-".join(sorted_words)
# join() method to join the sorted words back into a 
# hyphen-separated sequence and assigns it to the result variable
    print(result)


hyphen_separated("green-red-yellow-black-white")  # black-green-red-white-yellow




# without using functions
'''
a=input()
list = a.split("-")
lis = sorted(list)
string = "-".join(lis)
print(string)

'''
