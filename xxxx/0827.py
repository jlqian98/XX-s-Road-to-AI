##
from typing import ItemsView


numbers =  [3, 51, 2, 8, 6]
print(sorted(numbers, reverse=True))
print(numbers)

numbers.sort(reverse=True)
print(numbers)


##定义函数排序
items = [
    ('prouct1',10),
    ('prouct2',9),
    ('prouct3',12),
]
def sort_item(item):
    return item[1]

items.sort(key = sort_item)
print(items)

##
items = [
    ('prouct1',10),
    ('prouct2',9),
    ('prouct3',12),
]

prices = []
for item in items: 
    prices.append(item[1])
print(prices)

##prices = list(map(lambda item: item[1]))
##print(prices)


##prices = list(map(lambda item: item[1]))
##prices = [item[1] for item in items]


##filtered = list(filter(lambda item: item[1] >= 10, items))
#3filtered = [item for item in items if item[1] >= 10]


#4
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abc", list1, list2)))
