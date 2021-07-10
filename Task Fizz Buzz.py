# ### Task 3:
# - Write a program that prints the numbers from 1 to 100.
# - For multiples of three print "Fizz" instead of the number
# - For the multiples of five print "Buzz" instead of the number
# - For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,101):  # Specifying the numerical range from 1 to 100
    if num % 3 == 0 and num % 5 == 0:  # If the current num is perfectly divisible by both 3 and 5
        print("FizzBuzz")              # then print FizzBuzz.
        continue                       # Skip the rest of the code and continue loop
    elif num %3 ==0:                   # If the current num is perfectly divisible by 3
        print("Fizz")                  # then print Fizz
        continue                       # Skip the rest of the code and continue loop
    elif num %5 ==0:                   # If the current num is perfectly divisible by 5
        print("Buzz")                  # then print Buzz.
        continue                       # Skip the rest of the code and continue loop
    print(num)                         # Display num values