class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_courses_that_require_it = {i: set() for i in range(numCourses)}
        course_to_prerequisites = {i: set() for i in range(numCourses)}
        ready_courses = []
        completed_courses = set()

        for course, prereq in prerequisites:
            course_to_courses_that_require_it[prereq].add(course)
            course_to_prerequisites[course].add(prereq)

        for course, prereqs in course_to_prerequisites.items():
            if not prereqs:
                ready_courses.append(course)

        while ready_courses:
            curr = ready_courses.pop()
            completed_courses.add(curr)

            for course_that_requires_curr in course_to_courses_that_require_it[curr]:
                course_to_prerequisites[course_that_requires_curr].remove(curr)

                if not course_to_prerequisites[course_that_requires_curr]:
                    ready_courses.append(course_that_requires_curr)

        return len(completed_courses) == numCourses
