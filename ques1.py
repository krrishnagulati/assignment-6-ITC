'''
In number theory, a perfect number is a positive integer that is equal to the
sum of its proper positive divisors, that is, the sum of its positive divisors excluding the
number itself (also known as its aliquot sum). Equivalently, a perfect number is a
number that is half the sum of all of its positive divisors (including itself).
'''

def perfect_number(num):   # num is an parameter
    if num <= 0:
        return False         # it will return false as perfect number are always positive

    divisor_sum = sum([divisor for divisor in range(1, num) if num % divisor == 0])
    return divisor_sum == num
# it iterates through all numbers from 1 to (num - 1) and checks if they are divisors of num.
#  if a number is a divisor, it is added to a list comprehension.
  

# here we are calling the function 
print(perfect_number(6))    # 6,28,12 are arguments declared w.r.t num as parameters
print(perfect_number(28))
print(perfect_number(12))
