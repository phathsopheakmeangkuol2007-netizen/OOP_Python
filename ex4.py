class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def avg(self):
        return sum(self.marks)/len(self.marks)
s1 = Student("Alice", [85, 90, 78, 92, 88])
print(f"{s1.name}'s average score {s1.avg()}")