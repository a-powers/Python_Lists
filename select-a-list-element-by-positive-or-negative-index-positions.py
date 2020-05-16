# print("organic"[5])

# web_browers = ["Chrome", "Firefox", "Safari", "Opera", "Edge"]
# print(web_browers[0])
# print(web_browers[1])
# print(web_browers[4])

# print(web_browers[4][1])

# presidents = ["Washington", "Adams", "Jefferson"]
# print(presidents[-1])
# print(presidents[-2])
# print(presidents[-3])
# print(presidents[-2][0])


#Coding Exercise 15

def first_and_last(a):
    return a[0] + a[-1]
print(first_and_last(["First","Middle", "Last"]))


def product_of_even_indices(a):
    if len(a) == 6:
        return a[0] * a[2] * a[4]
print(product_of_even_indices([5, 6, 7, 8, 9, 10]))


def first_letter_of_last_string(a):
    return a[-1][0]
print(first_letter_of_last_string(["dog", "cat","parrot"]))
