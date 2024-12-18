class Student:
    def __init__(self, firstname, lastname, tnumber):
        """
        Initializes the Student object with the provided information.
        
        :param firstname: Student's first name (string)
        :param lastname: Student's last name (string)
        :param tnumber: Student's TNumber (string)
        """
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = [] 
      
    def RunningAverage(self):
        """
        Calculates the running average of the student's scores excluding blank scores.
        
        :return: Running average (float)
        """
        non_blank_scores = [score for score in self.Grades if score > 0]
        if non_blank_scores:
            return sum(non_blank_scores) / len(non_blank_scores)
        return 0.0

    def TotalAverage(self):
        """
        Calculates the total average, treating missing scores as zero.
        
        :return: Total average (float)
        """
        if self.Grades:
            return sum(self.Grades) / len(self.Grades)
        return 0.0

    def LetterGrade(self):
        """
        Returns the letter grade based on the total average.
        
        :return: Letter grade (string)
        """
        total_avg = self.TotalAverage()
        if total_avg >= 90:
            return "A"
        elif total_avg >= 80:
            return "B"
        elif total_avg >= 70:
            return "C"
        elif total_avg >= 60:
            return "D"
        else:
            return "F"


class StudentList:
    def __init__(self):
        """
        Initializes the StudentList with an empty list of students.
        """
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        """
        Creates a student object and appends it to the Studentlist.
        
        :param firstname: Student's first name (string)
        :param lastname: Student's last name (string)
        :param tnumber: Student's TNumber (string)
        """
        student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(student)

    def find_student(self, tnumber):
        """
        Finds a student in the list by their TNumber and returns the index.
        
        :param tnumber: Student's TNumber (string)
        :return: Index of student in Studentlist, or -1 if not found
        """
        for index, student in enumerate(self.Studentlist):
            if student.TNumber == tnumber:
                return index
        return -1

    def print_student_list(self):
        """
        Prints the attributes of all Student objects in the Studentlist.
        """
        for student in self.Studentlist:
            print(f"Name: {student.FirstName} {student.LastName}")
            print(f"TNumber: {student.TNumber}")
            print(f"Running Average: {student.RunningAverage():.2f}")
            print(f"Total Average: {student.TotalAverage():.2f}")
            print(f"Letter Grade: {student.LetterGrade()}")
            print("-" * 50)

    def add_student_from_file(self, filename):
        """
        Reads a file containing student information and appends the student objects to Studentlist.
        
        :param filename: Path to the file containing student information
        """
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    firstname, lastname, tnumber = parts[:3]
                    self.add_student(firstname, lastname, tnumber)

    def add_scores_from_file(self, filename):
        """
        Reads a file containing score data, locates the student in Studentlist by TNumber,
        and appends the scores to the student's Grades list.
        
        :param filename: Path to the file containing score data
        """
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                tnumber = parts[0]
                scores = [float(score) if score else 0.0 for score in parts[1:]]
                
                # Find the student by TNumber
                index = self.find_student(tnumber)
                if index != -1:
                    student = self.Studentlist[index]
                    student.Grades = scores

def main():
    student_list = StudentList()

    student_list.add_student_from_file('11.Project Students.txt')

    student_list.add_scores_from_file('11.Project Scores.txt')

    student_list.print_student_list()

if __name__ == "__main__":
    main()
