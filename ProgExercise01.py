"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    # Comparison methods
    def __eq__(self, other):
        """Checks if two students' names are equal."""
        return self.name == other.name

    def __lt__(self, other):
        """Checks if one student's name is less than another's."""
        return self.name < other.name

    def __ge__(self, other):
        """Checks if one student's name is greater than or equal to another's."""
        return self.name >= other.name


def main():
    """Test the comparison methods."""
    student1 = Student("Alice", 3)
    student2 = Student("Bob", 3)
    student3 = Student("Alice", 3)

    print("Student 1:", student1)
    print("Student 2:", student2)
    print("Student 3:", student3)
    print()

    print("Student 1 == Student 2:", student1 == student2)  # False
    print("Student 1 == Student 3:", student1 == student3)  # True
    print("Student 1 < Student 2:", student1 < student2)    # True
    print("Student 1 >= Student 2:", student1 >= student2)  # False

if __name__ == "__main__":
    main()
