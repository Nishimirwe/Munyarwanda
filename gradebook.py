
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
            
            
    def prinTranscript(self, st_roll):
        if self.find(st_roll):
            c=self.courses.values()
            c_tolist=list(c)
            students=c_tolist[0].getClasslist()
            file=open(str(st_roll)+"_transcript.txt",'w')
            for student in students:
                roll=student.getRollNum()
                if roll == st_roll:
                    name=student.getName()
                    file.write(roll+"   "+name+"\n")
            for course in c_tolist:
                stds=course.getClasslist()
                for st in stds:
                    st_rollNum=st.getRollNum()
                    if st_roll == st_rollNum:
                        # do here
                        course_id=course.getCourseID()
                        course_name=course.getCourseName()
                        student_mark=st.percentageGen()
                        student_grade=st.gradeGen()
                        file.write(course_id+"   "+course_name+"   "+str(student_mark)+"    "+str(student_grade)+"\n")
            file.close()
        else:
            print("Invalid")

    def referrals(self):
        
        courses=self.courses
        studentsDictionary={}
        limiter=0
        rollNums=[]
        f=open("referrals.txt", 'w')
        for course in courses.values():
            if limiter==0:
                studentList=course.getClasslist()
                for student in studentList:
                    studentsDictionary[student.getRollNum()]=student
                    rollNums.append(student.getRollNum())
                limiter+=1    
                
        for student in studentsDictionary:
            for course in courses.values():
                studentList=course.getClasslist()
                for i in studentList:
                    if i.getRollNum()==studentsDictionary[student].getRollNum() and i.percentageGen()<40:
                        if studentsDictionary[student].getRollNum() in rollNums:   
                                f.write(studentsDictionary[student].getRollNum()  + "  " 
                                        + studentsDictionary[student].getName())
                                f.write("\n")
                                rollNums.remove(studentsDictionary[student].getRollNum())  
                        f.write("     "+ course.getCourseID() + "   " + course.getCourseName() + "  " 
                                + str(i.percentageGen()) + "  " + i.gradeGen())
                        f.write("\n")
        f.close()                 
                        
    def transcripts(self):
        
        courses=self.courses
        studentsDictionary={}
        limiter=0
        rollNums=[]
        f=open("transcripts.txt", 'w')
        for course in courses.values():
            if limiter==0:
                studentList=course.getClasslist()
                for student in studentList:
                    studentsDictionary[student.getRollNum()]=student
                    rollNums.append(student.getRollNum())
                limiter+=1    
                
        for student in studentsDictionary:
            for course in courses.values():
                studentList=course.getClasslist()
                for i in studentList:
                    if i.getRollNum()==studentsDictionary[student].getRollNum():
                        if studentsDictionary[student].getRollNum() in rollNums: 
                                f.write("---------------------------------------------------------")
                                f.write("\n") 
                                f.write(studentsDictionary[student].getRollNum()  + "  " 
                                        + studentsDictionary[student].getName())
                                f.write("\n")
                                rollNums.remove(studentsDictionary[student].getRollNum())  
                        f.write(course.getCourseID() + "   " + course.getCourseName() + "  " 
                                + str(i.percentageGen()) + "  " + i.gradeGen())
                        f.write("\n")                
            f.write("----------------------------------------------------------------------")
            f.write("\n") 
                
        

    # def passes(self):
    #     winners=set()
    #     file=open("passes.txt",'w')
    #     for course in list(self.courses.values()):
    #         studs=course.getClasslist()
    #         for st in studs:
    #             st_percent=st.percentageGen()
    #             if st_percent < 40:
    #                 winners.add((st.getRollNum(),st.getName()))
    def passes(self):
        failers=set()
        file=open("passes.txt",'w')
        for course in list(self.courses.values()):
            studs=course.getClasslist()
            for st in studs:
                st_percent=st.percentageGen()
                if st_percent < 40:
                    failers.add((st.getRollNum(),st.getName()))
        c=self.courses.values()
        c_tolist=list(c)
        students=c_tolist[0].getClasslist()
        students=[(i.getRollNum(),i.getName()) for i in students]
        failers=list(failers)
        winners=[i for i in students if i not in failers]
        for winner in winners:
            file.write(winner[0]+"  "+winner[1]+"\n")
        file.close()
        
        
    def grades(self):
        c=self.courses.values()
        c_tolist=list(c)
        c_ids=[i.getCourseID() for i in c_tolist]
        file=open("grades.txt",'w')
        file.write("rollnum    name   "+c_ids[0]+"   "+c_ids[1]+"   "+c_ids[2]+"  "+c_ids[3]+"   "+c_ids[4]+"   Avg\n \n")
        students=c_tolist[0].getClasslist()
        students=[(i.getRollNum(),i.getName()) for i in students] 
        for student in students:
            std_marks=[]
            file.write(str(student[0])+"     "+str(student[1])+"    ")
            for course in c_tolist:
                course_stds=course.getClasslist()
                for i in course_stds:
                    id=i.getRollNum()
                    if id == student[0]:
                        grade=i.gradeGen()
                        percent=i.percentageGen()
                        std_marks.append((percent,grade))
                        break
            for i in std_marks:
                file.write(str(i[0])+"    ")
            marks=[i[0] for i in std_marks]
            file.write(str(round(sum(marks)/len(std_marks),2))+"\n")
        file.close()
        
        
    def courseGrade(self,course_id):
        if self.isEmpty():
            return "Empty dictionary"
        file=open(course_id+"_grades.txt",'w')
        for course in self.courses.values():
            if course.getCourseID() == course_id:
                for student in course.getClasslist():
                    roll=student.getRollNum()
                    name=student.getName()
                    percent=student.percentageGen()
                    grade=student.gradeGen()
                    file.write(str(roll)+"   "+str(name)+"     "+str(percent)+"   "+str(grade)+"\n" )
        file.close()
#You may define any additional claases or functions below this comment.

##########################################################################

def testGradeBook():
    g=GradeBook()
    g.readManyFiles()
    g.prinTranscript("S1000")
    g.prinTranscript("S1005")
    g.referrals()
    g.transcripts()
    g.prinTranscript("S1000")
    g.passes()
    g.grades()
    g.courseGrade("DSA001")
    """
    Your code to initiate GradeBook and generate the required output files.
    """

testGradeBook()
