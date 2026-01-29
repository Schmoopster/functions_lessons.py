
# Indefinite Arguments (**kwargs) Practice #1
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.

def number_attributes(**kwargs):
    return len(kwargs)
print(number_attributes(a=1, b=2, c=3))  #Example Usage
print(number_attributes(x=10, y=20, z=30, w=40, v=50))  #Example Usage
def number_attributes(**kwargs):
    return(kwargs)

# Indefinite Arguments (**kwargs) Practice #2
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.
def list_attributes(**kwargs):
    values_list = [] # Initialize an empty list to store values
    for value in kwargs.values(): # Iterate through each value in the keyword arguments
        values_list.append(value) # Append the value to the list
    return values_list # Return the list of values
print(list_attributes(color="red", size="medium", shape="circle"))  #Example Usage
print(list_attributes(name="Alice", age=30, city="New York", profession="Engineer"))  #Example Usage


# Indefinite Arguments (**kwargs) Practice #3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:

# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:

# describe_person("Ash", eye_color="brown", hair_color="black")

# Will print to the screen:

# Characteristics of Ash:
# eye_color: brown
# hair_color: black]

def describe_person(name, **kwargs):
    print(f"Characteristics of {name}:") # Print the header with the person's name
    for key, value in kwargs.items(): # Iterate through each key-value pair in the keyword arguments
        print(f"{key}: {value}") # Print the characteristic in the specified format 
describe_person("Ash", eye_color="brown", hair_color="black")  #Example Usage
describe_person("Misty", eye_color="blue", hair_color="orange", hobby="swimming")  #Example Usage
describe_person("Brock", eye_color="black", hair_color="brown", profession="rock trainer", age=15)  #Example Usage
