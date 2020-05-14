# List aka array is a data structure that stores an ordered sequence of objects.
# empty = []
# empty = list()  # use this to convert another data structure to a list

# sodas = ["Coke", "Pepsi", "Dr. Pepper"]
# print(len(sodas))

# quarterly_revenue = [15000, 12000, 9000, 20000]
# print(len(quarterly_revenue))

# user_settings = [True, False, True, True]
# print(len(user_settings))



# Coding Exercise 14


def is_long(fruits = []):
    if len(fruits) > 5:
        return True
    else:
        return False
print(is_long(fruits= ["a", "b", "c", "d", "e", "f"]))