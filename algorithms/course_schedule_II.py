class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        next_courses = [[] for i in range(numCourses)]
        count = [0,] * numCourses
        for course, precourse in prerequisites:
            count[course] += 1
            next_courses[precourse].append(course)
        remain_courses = numCourses
        to_check = [course for course in range(numCourses) if count[course] == 0]
        ans = []

        while to_check:
            next_to_check = []
            for course in to_check:
                remain_courses -= 1
                ans.append(course)
                for next_course in next_courses[course]:
                    count[next_course] -= 1
                    if count[next_course] == 0:
                        next_to_check.append(next_course)
            to_check = next_to_check

        if remain_courses == 0:
            return ans
        else:
            return []
