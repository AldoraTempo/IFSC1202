class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        """
        Initializes the Student object with the provided information.
        
        :param firstname: Student's first name (string)
        :param lastname: Student's last name (string)
        :param tnumber: Student's TNumber (string)
        :param scores: List of student scores as strings
        """
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = [float(score) if score else 0.0 for score in scores]

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


def process_student_scores(file_path):
    """
    Reads the student scores from the file, creates Student objects, and prints the results.
    
    :param file_path: Path to the file containing student scores
    """
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  
            if line:  
                parts = line.split(',')
                if len(parts) >= 4:
                    firstname, lastname, tnumber = parts[:3]
                    scores = parts[3:]  =
                    student = Student(firstname, lastname, tnumber, scores)

                    
                    print(f"Student: {student.FirstName} {student.LastName}")
                    print(f"TNumber: {student.TNumber}")
                    print(f"Running Average: {student.RunningAverage():.2f}")
                    print(f"Total Average: {student.TotalAverage():.2f}")
                    print(f"Letter Grade: {student.LetterGrade()}")
                    print("-" * 50)

file_path = 'StudentScores.txt' 
process_student_scores(file_path)
