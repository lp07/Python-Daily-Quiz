class square:
    def getArea(self):
        return self.side * self.side

obj = square()
obj.side = 8
print(obj.side, obj.getArea())

# op: 8 64
