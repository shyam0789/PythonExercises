class GradeCalculator:

    def __init__(self):
        pass

    def get_grade(self):
        grade = 0
        try:
            grade = int(input("Enter the grade of the Student: "))
            if grade > 100 or grade < 0:
                raise ValueError("Pls enter value btw 0-100")

        except ValueError as e:
            print("Pls enter a numeric value")
        else:
            self.calculate_grade(grade)
        finally:
            print("Thank you for using the Grade Calculator. Goodbye!")


    def calculate_grade(self,grade):
        if 100 <= grade >=90:
            print("Grade A")
        elif 89 <= grade >= 80:
            print("Grade B")
        elif 79 <= grade >= 70:
            print("Grade C")
        elif 69 <= grade >= 60:
            print("Grade D")
        elif grade < 60:
            print("Grade F")


grade_cal = GradeCalculator()
grade_cal.get_grade()