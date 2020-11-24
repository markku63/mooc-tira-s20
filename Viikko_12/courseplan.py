class CoursePlan:
    def __init__(self):
        self._reqs = {}
    
    def add_course(self,course):
        self._reqs[course] = []

    def add_requisite(self,course1,course2):
        self._reqs[course1].append(course2)

    def _dfs(self, course, visited, tsort):
        if visited[course] == 2:
            return
        if visited[course] == 1:
            self._cycle = True
            return
        visited[course] = 1
        for req in self._reqs[course]:
            self._dfs(req, visited, tsort)
        visited[course] = 2
        tsort.append(course)


    def find(self):
        tsort = []
        visited = dict.fromkeys(self._reqs, 0)
        self._cycle = False
        for course in self._reqs.keys():
            if visited[course] == 0:
                self._dfs(course, visited, tsort)
            if self._cycle:
                return None
        return list(reversed(tsort))

if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe","Ohja")
    c.add_requisite("Ohja","Tira")
    c.add_requisite("Jym","Tira")
    print(c.find()) # [Ohpe,Jym,Ohja,Tira]
    c.add_requisite("Tira","Tira")
    print(c.find()) # None