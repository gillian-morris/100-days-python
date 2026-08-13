# Day 13 - Debugging Practice
# Reviewing debugging programs

# Example 1 - if number % 2 needs to be '==' to 0
'''
def odd_or_even(number):
    if number % 2 = 0:
        return "This is an even number."
    else:
        return "This is an odd number."
odd_or_even(5)
'''
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
print(odd_or_even(5))

# Example 2 - year % 4000 is wrong, should be 400
'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap(2000))

# Example 3 - if statements should be elif statements
# the for if statement should be 'and' and not 'or'
# Final print statement should be print(number)
'''
Target is the number up to which we count
def fizz_buzz(target):
   for number in range(1, target + 1):
       if number % 3 == 0 or number % 5 == 0:
           print("FizzBuzz")
       if number % 3 == 0:
           print("Fizz")
       if number % 5 == 0:
           print("Buzz")
       else:
           print([number])
'''
#Target is the number up to which we count
def fizz_buzz(target):
   for number in range(1, target + 1):
       if number % 3 == 0 and number % 5 == 0:
           print("FizzBuzz")
       elif number % 3 == 0:
           print("Fizz")
       elif number % 5 == 0:
           print("Buzz")
       else:
           print(number)

fizz_buzz(15)
