class vowels:
    def __init__(self, text):
        self.text = text
        self.start = -1
        self.vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
        self.vowels_values = [v for v in self.text if v in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start < len(self.vowels_values):
            return self.vowels_values[self.start]
        raise StopIteration






my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

