class Point:
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def __eq__(self, other) :
        return self.x == other.x and self.y == self.y

    def __gt__(self, other) :
        return self.x > other.x and self.y > self.y

    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1,2)
other = Point(1,2)
combined = point + other
print(combined.x)
print(point > other)
