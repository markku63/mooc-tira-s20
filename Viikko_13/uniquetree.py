# https://www.baeldung.com/cs/graphs-total-number-of-minimum-spanning-trees

class UniqueTree:
    def __init__(self,n):
        # TODO

    def add_edge(self,a,b,x):
        # TODO

    def check(self):
        # TODO

if __name__ == "__main__":
    u = UniqueTree(4)
    u.add_edge(1,2,2)
    u.add_edge(1,3,3)
    print(u.check()) # False
    u.add_edge(1,4,2)
    print(u.check()) # True
    u.add_edge(3,4,4)
    print(u.check()) # True
    u.add_edge(2,4,1)
    print(u.check()) # False