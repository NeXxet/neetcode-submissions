class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circleWantedCount = 0
        squareWantedCount = 0
        unfedStudents = len(students)

        for student in students:
            if student == 0:
                circleWantedCount += 1
            else:
                squareWantedCount += 1
        
        for sandwich in sandwiches:
            if sandwich == 0 and circleWantedCount > 0:
                circleWantedCount -= 1
                unfedStudents -= 1
            elif sandwich == 1 and squareWantedCount > 0:
                squareWantedCount -= 1
                unfedStudents -= 1
            else:
                return unfedStudents

        return 0
        
