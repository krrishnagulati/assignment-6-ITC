'''
Write a Python function to check whether a string is a pangram or not. Note: Pangrams
are words or sentences containing every letter of the alphabet at least once. For
example: "The quick brown fox jumps over the lazy dog"
'''
def pangram(str):
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','n','p','q','r','s','t',' ','u','v','w','x','y','z']

    for i in a:
        if i not in a:
            return False
    return True

print(pangram("the quick brown fox jumps over the lazy dog"))
print(pangram("Pack my box with five dozen liquor jugs"))
print(pangram("hello"))
            
    
