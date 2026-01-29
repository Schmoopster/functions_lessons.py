#Normal Code

#  def tea_order(customer_name, tea_type, milk=None, sweetener=None):
#     print(customer_name + " ordered a cup of " + tea_type + " tea.")
#     if milk!= None:
#         print(" -Add:", milk)
#     if sweetener!= None:
#         print(" -Add:", sweetener)

# tea_order("Alice", "chamomile")
# tea_order("Bob", "black")
# tea_order("Tony", "black", "oat", "honey")


#Only args

# def tea_order(customer_name, tea_type, *args):
#     print(customer_name + " ordered a cup of " + tea_type + " tea.")
#     for arg in args:
#         print(" -Add:", arg)

# tea_order("Alice", "chamomile")
# tea_order("Bob", "black", milk ="oat")
# tea_order("Tony", "black", milk ="oat", sweetener="honey")


#Args + Kwargs

def tea_order(customer_name, tea_type, *args, **kwargs):
    print(customer_name + " ordered a cup of " + tea_type + " tea.")
    for key, value in kwargs.items():
        print(" -Add:", key, ":", value)

tea_order("Alice", "chamomile")
tea_order("Bob", "black", milk ="oat")
tea_order("Tony", "black", "oat", sweetener="honey")
tea_order("Eve", "green", milk="almond", sweetener="sugar", flavor="lemon")




# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args):
    total = 0 # Initialize total to 0
    for num in args: # Iterate through each argument
        total += num ** 2 # Square the number and add it to total
        #first time through loop: total = 0 + 1^2 = 1
        #second time through loop: total = 1 + 2^2 = 5
        #third time through loop: total = 5 + 3^2 = 14
    return total # Return the total sum of squares
print(sum_squares(1, 2, 3))  #Example Usage
print(sum_squares(4, 5, 6, 7, 8, 9))  #Example Usage
# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total = 0 # Initialize total to 0
    for num in args: # Iterate through each argument
        total += abs(num) # Add the absolute value of the number to total
        #first time through loop: total = 0 + abs(-1) = 1
        #second time through loop: total = 1 + abs(-2) = 3
        #third time through loop: total = 3 + abs(3) = 6
    return total # Return the total sum of absolute values
print(absolute_sum(-1, -2, 3))  #Example Usage
print(absolute_sum(-10, 20, -30, 40, -50))  #Example Usage
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"

def personal_numbers(name, *args):
    sum_numbers = 0 # Initialize sum_numbers to 0
    for num in args: # Iterate through each argument
        sum_numbers += num # Add the number to sum_numbers
        #first time through loop: sum_numbers = 0 + 5 = 5
        #second time through loop: sum_numbers = 5 + 10 = 15
        #third time through loop: sum_numbers = 15 + 15 = 30
    return f"{name}, the sum of your numbers is {sum_numbers}" # Return the formatted message
print(personal_numbers("Alice", 5, 10, 15))  #Example Usage
print(personal_numbers("Bob", 1, 2, 3, 4, 5))  #Example Usage