from common import *


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for san in sandwiches:
            try:
                first_match = students.index(san)
                students = students[first_match + 1 :] + students[:first_match]
            except ValueError:
                return len(students)
        return 0
