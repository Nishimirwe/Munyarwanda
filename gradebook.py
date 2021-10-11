
"""
@author : <your andrewid>
@date:
Description: <Any useful comments>
"""
from course import Course

class GradeBook:
    def __init__(self):
        self.courses=dict()
    
    def isEmpty(self):
        if len(self.courses) == 0:
            return True
        return False
        
    def find(self,st_roll):
        if not self.isEmpty():
            c=self.courses.values()
            c_tolist=list(list(c))
            c=c_tolist[0]
            stds=c.getClasslist()
            all_rolls=[i.getRollNum() for i in stds]
            if st_roll in all_rolls:
                return True
            else:
                return False
        else:
            return False
        
    def readManyFiles(self):
        from_files=input("Enter 5 files: ")
        from_files=from_files.split(",")
        for file in from_files:
            course=Course()
            course.addCourseDataFromFile(file)
            self.courses[course.getCourseID()]=course

#You may define any additional claases or functions below this comment.

##########################################################################

def testGradeBook():
    g=GradeBook()
    g.readManyFiles()
    print(len(g.courses))
    """
    Your code to initiate GradeBook and generate the required output files.
    """

testGradeBook()
