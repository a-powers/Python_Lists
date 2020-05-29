# print("programming"[3:6])

# muscles = ["Biceps", "Triceps", "Deltoids", "Pectoralis"]

# print(muscles[1:3])
# print(muscles[1:2])
# print(muscles[0:])
# print(muscles[:2])
# print(muscles[2:5])
# print(muscles[2:])

# print(muscles[-4:-2])
# print(muscles[-3:])
# print(muscles[:-1])
# print(muscles[1:-1])

# print(muscles[::2])
# print(muscles[::-2])
# print(muscles[::-1])



# # Coding Exercise 16

def split_in_two(a = list, b = int):
    if b % 2 == 0:
        return a[2:]
    else:
        return a[:2]
print(split_in_two(a = ["a", "b", "c", "d", "e", "f"], b = 10))

# Coding Exercise 17


def nested_extraction(a: list, b: int):
    return a[b][b]
print(nested_extraction(a = [[3, 4, 5], [7, 8, 9], [10, 11, 12]], b = 2))
    


def beginning_and_end(a: list):
    if a[0] == a[-1]:
        return True
   
print(beginning_and_end(["a", "b", "a"]))


words = ["cat", "dog", "rhino"]
def long_word_in_collection(words:list, b: str):
    if b in words and len(b) > 4:
        return True

print(long_word_in_collection(words, "rhino"))