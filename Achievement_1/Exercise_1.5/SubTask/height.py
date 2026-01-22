class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def total_inches(self):
        return self.feet * 12 + self.inches

    def __sub__(self, other):
        total_inches = self.total_inches() - other.total_inches()
        feet = total_inches // 12
        inches = total_inches % 12
        return Height(feet, inches)

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

height1 = Height(5, 10)
height2 = Height(3, 9)

result = height1 - height2
print("Resulting height:")
print(result)
