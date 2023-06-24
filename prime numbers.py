#  Use input() to get the number from the user and int() to convert it to an integer.
#
# * Use a variable, e.g., is_prime, initialized to True to keep track of whether the number is prime.
#
# * Use a for loop to check each number from 2 to the square root of the number entered by the user. You can use int(
# math.sqrt(number)) to calculate the square root.
#
# * Inside the loop, use an if statement and the modulo operator % to check if the current number divides evenly into
# the number entered by the user. If it does, set is_prime to False.
#
# * After the loop, use an if-else statement to print whether the number is prime or not based on the value of is_prime.
#
# Testing:
#
# * Test the program with known prime numbers (e.g., 2, 3, 5, 7, 11) and make sure it correctly identifies them as
# prime.
#
# * Test the program with numbers that are not prime to make sure it identifies them correctly.
#
# * Test the program with edge cases such as 1 and 0.
#
# This project introduces the concept of prime numbers and involves a combination of loops and conditional
# statements. It is also an example of an algorithm used in number theory. Let me know when you're ready for the
# eighth project! do this
user = int(input("enter a positive number greater than 1"))

for num in range(2, user + 1):
    for i in range (2, num):
        if (num % i) == 0:
            break
    else:
        print(num)

