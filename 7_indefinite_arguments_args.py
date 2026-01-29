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


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"