import math

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)
    
    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s2 == self.s3 or self.s1 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"
    
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    
    def area(self):
        # Using Heron's formula to calculate the area
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))
    
    def angles(self):
        # Using the law of cosines to calculate angles in degrees
        angle1 = math.degrees(math.acos((self.s2**2 + self.s3**2 - self.s1**2) / (2 * self.s2 * self.s3)))
        angle2 = math.degrees(math.acos((self.s1**2 + self.s3**2 - self.s2**2) / (2 * self.s1 * self.s3)))
        angle3 = 180 - angle1 - angle2
        return [angle1, angle2, angle3]

# Example usage
TrianglesList = [
    Triangle(3, 4, 5),
    Triangle(5, 5, 5),
    Triangle(4, 4, 6),
]

print(f'{"Type":<15} {"Side 1 (s1)":<15} {"Side 2 (s2)":<15} {"Side 3 (s3)":<15} {"Perimeter":<15} {"Area":<15} {"Angle 1":<15} {"Angle 2":<15} {"Angle 3":<15}')
for triangle in TrianglesList:
    t_type = triangle.type()
    s1 = triangle.s1
    s2 = triangle.s2
    s3 = triangle.s3
    perimeter = triangle.perimeter()
    area = triangle.area()
    angles = triangle.angles()
    
    print(f'{t_type:<15} {s1:<15} {s2:<15} {s3:<15} {perimeter:<15} {area:<15.2f} {angles[0]:<15.2f} {angles[1]:<15.2f} {angles[2]:<15.2f}')
