##栈
browsing_session = []
browsing_session.append(1) 
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session) 
last = browsing_session.pop()#删除最后一个
print(last)
print("redirect", browsing_session[-1])


##队列
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)


##元组
point = tuple("hello world")  #tuple可以避免删除某些元素 例如point[0] = 2 就无法执行
print(point)

##交换
#z = x
#x = y
#y = z
#等于 x, y = y, x


##数据去重复
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(first | second) #1 2 3 4 5
print(first & second) #1 
print(first - second) #2 3 4 
print(first ^ second) # 2 3 4 5


#
values = {x * 2 for x in range(5)}#values = {x: x * 2 for x in range(5)}
for x in values:
    print(x)



