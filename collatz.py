import sys

# define a function called collatz
def collatz(number):
    # check to see if the number is even
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    # if number is odd, multiply by 3 and add 1
    elif number % 2 == 1:
        ans = 3 * number + 1
        print(ans)
        return ans

print("Please enter a number: ")

# trap for invalid input value
try:
    test = int(input())  
    
except ValueError:
    print('You must enter an integer data type.')
    sys.exit()
while test != 1:
    test = collatz(int(test))
