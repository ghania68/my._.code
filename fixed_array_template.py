class FixedSizeArray:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.count = 0

    def insert(self, index, value):
        if self.count == self.size:
            print("Array is full!")
            return
        if index < 0 or index > self.count:
            print("Invalid index!")
            return
        for i in range(self.count, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.count += 1

    def delete(self, index):
        if index < 0 or index >= self.count:
            print("Invalid index!")
            return
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.count - 1] = None
        self.count -= 1

    def update(self, index, value):
        if index < 0 or index >= self.count:
            print("Invalid index!")
            return
        self.array[index] = value

    def get(self, index):
        if index < 0 or index >= self.count:
            print("Invalid index!")
            return None
        return self.array[index]

    def display(self):
        return self.array[:self.count]

    def print(self):
        print(self.array[:self.count])

    def search(self, value):
        for i in range(self.count):
            if self.array[i] == value:
                return i
        return -1

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def clear(self):
        self.array = [None] * self.size
        self.count = 0

if __name__ == "__main__":
    arr = FixedSizeArray(5)

    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(1, 15)
    arr.print()    # should print: [10, 15, 20]

    arr.update(1, 99)
    arr.print()    # should print: [10, 99, 20]

    print(arr.get(2))  # should print: 20

    arr.delete(1)
    arr.print()    # should print: [10, 20]

    print(arr.search(20))  # should print: 1
    print(arr.is_full())   # should print: False
    print(arr.is_empty())  # should print: False

    arr.clear()
    arr.print()    # should print: []
