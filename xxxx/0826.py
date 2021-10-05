# 1
zeros = [0] * 5
letters = ["a", "b", "c"]
combined = zeros + letters
numbers = list(range(20))
chars = list("hello world")
print(combined)
print(chars)
print(numbers)

# 2
nu = [1, 2, 3, 4, 5, 6]
first, second, *other = nu

first = nu[0]
second = nu[1]
other = nu[2]
print(first,second,other)

#3
items = (0,"a")
index, letter = items
for index, letter in enumerate(letters):
    print(index,letter)

#4 add
letters.append("d")
letters.insert(0,"f")
print(letters)

#5 remove
letters.append(0)
letters.insert("a")
del letters[0:3]
letters.clear()
print(letters)

#6
letters.count("e")
if "e" in letters:
    print(letters.index("d"))
