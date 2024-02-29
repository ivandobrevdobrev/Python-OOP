class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):  # Празен лие ? - True акое е празен,  False ако има нещо
        return False if self.data else True
        #return not self.data


    def __str__(self):
        reversed_data = reversed(self.data)
        result = ", ".join(reversed_data)
        return f"[{result}]"


s = Stack()
print(s.is_empty())
s.push("5")
s.push("6")
s.push("8")
s.pop()
print(s.top())
print(s.is_empty())
print(s)