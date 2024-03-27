class reverse_iter :
    def __init__(self, some_list):
        self.some_list = some_list
        self.end = len(self.some_list)
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            self.end -= 1
            return self.some_list[self.end]
        raise StopIteration

# OR shorter way without Next:

 # def __iter__(self):
 #        return reversed(self.some_list)

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

