

class Structure:

    def __init__(self,Name):
        self.Name=Name
        self.combolst=[]

    def addcombo(self,batting,running):
        obj=playercombo(batting,running)
        self.combolst.append(obj)


class playercombo:
    def __init__(self,batting,running):
        self.Batsman=batting
        self.Runner=running
        self.run=[]

    def addrun(self,runs):
        self.run.append(runs)

    def most_common(self):
        return max(set(self.run), key=self.run.count)