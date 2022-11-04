# Exercise 1: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name,salary = 9000):
    return name,salary
print(show_employee('Olayinka'))

# Exercise 2: Accepting a list as an input
# Write a program to create a function show_squares() using the following condition.
# It should accept a list of numbers as input and returns the square of all numbers in the list.
# e.g input = [2,4,6,8]
# Output = [4,16,36,64]

Quest = list(map(int, input('Enter numbers seperated by space: ').split()))
output = []
def show_squares(Quest):
    for i in Quest:
        ansa = i*i
        output.append(ansa)
    return output
print(show_squares(Quest))

# Exercise 3: Returning Boolean in functions
# Write a program to create a function check() using the following conditions:
# Your function should accept two arguments named values and target. values represents a list of
# numbers and target represents an integer. Your check() function should return True if the target
# number appears more than once in the list , else it should return False.
# e.g values = [2,4,9,7] target = 9. Return False,9 appears only once in the list.
# values =[7,9,12,9] target = 9. Return True, 9 occurs more than once In the list.

def check(values = [2,4,9,7],target = 9):
    if values and target == 9:
        return('True 9 appears more than once in the list')
    else:
        return('False 9 appears just once in the list')
print(check())



# Exercise 4: Nested Functions
# You are to create two functions: parent_function() and child_function().
# The parent_function() is to print out the following line..”I am a backend developer”
# You are to design the child_function() to call the parent_function()

def parent_function():
    print('I am a backend developer')
parent_function()

def child_function():
    parent_function()
child_function()

    