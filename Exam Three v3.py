import math

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        area = math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))
        return area

    def angles(self):
        # Using the law of cosines to calculate angles
        angle1 = math.degrees(math.acos((self.s2**2 + self.s3**2 - self.s1**2) / (2 * self.s2 * self.s3)))
        angle2 = math.degrees(math.acos((self.s1**2 + self.s3**2 - self.s2**2) / (2 * self.s1 * self.s3)))
        angle3 = 180 - angle1 - angle2
        return [angle1, angle2, angle3]

# Function to load triangles from a text file
def load_triangles_from_file(filename):
    triangles = []
    with open(filename, 'r') as file:
        for line in file:
            # Assume each line has the form: s1, s2, s3 (comma separated)
            sides = list(map(float, line.strip().split(",")))
            if len(sides) == 3:
                triangles.append(Triangle(*sides))
    return triangles

# Step 2: Load triangles from file and print the details
def print_triangle_details(triangles):
    print(f"{'Type':<12}{'Side 1 (s1)':<15}{'Side 2 (s2)':<15}{'Side 3 (s3)':<15}{'Perimeter':<10}{'Area':<10}{'Angle 1':<10}{'Angle 2':<10}{'Angle 3':<10}")
    print("-" * 100)
    for triangle in triangles:
        t_type = triangle.type()
        s1, s2, s3 = triangle.s1, triangle.s2, triangle.s3
        perimeter = triangle.perimeter()
        area = triangle.area()
        angles = triangle.angles()

        print(f"{t_type:<12}{s1:<15.2f}{s2:<15.2f}{s3:<15.2f}{perimeter:<10.2f}{area:<10.2f}{angles[0]:<10.2f}{angles[1]:<10.2f}{angles[2]:<10.2f}")

# Example usage
# Assuming you have a text file "triangles.txt" with side lengths in it
triangles = load_triangles_from_file('Exam Three Triangles.txt')
print_triangle_details(triangles)