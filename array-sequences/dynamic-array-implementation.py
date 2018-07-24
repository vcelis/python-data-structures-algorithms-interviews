import ctypes


class DynamicArray():

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('Index is out of bounds!')

        return self.array[k]

    def append(self, value):
        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.array[self.n] = value
        self.n += 1

    def _resize(self, new_capacity):
        new_array = self.make_array(new_capacity)

        for i in range(self.n):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


if __name__ == '__main__':
    arr = DynamicArray()
    arr.append(1)
    print(len(arr))
    arr.append(2)
    print(len(arr))
    print(arr[1])
    print(arr[1])
