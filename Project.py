class Project:
    def __int__(self):
        self.name = ""
        self.theResources = ""
        self.theEmployees = ""
        self.theWorkBreakdownStructure = ""

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setTheResources(self, theResources):
        self.theResources = theResources

    def getTheResources(self):
        return self.theResources

    def setTheEmployees(self, theEmployees):
        self.theEmployees = theEmployees

    def getTheEmployees(self):
        return self.theEmployees

    def setTheWorkBreakdownStructure(self, theWorkBreakdownStructure):
        self.theWorkBreakdownStructure = theWorkBreakdownStructure

    def getTheWorkBreakdownStructure(self):
        return self.theWorkBreakdownStructure
