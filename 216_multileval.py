#multilavle inheritance
class emp:
    def setId(self , id):
        self.id=id
    def getId(self):
        print("emp info : ")
        print("id : ",self.id)    

class programer(emp):
    def setLanguage(self,lang):
        self.lang=lang
    def getlang(self):
        print("language : ",self.lang)    

class programerManager(programer):
    def setProject(self, project):
        self.project=project
    def getproject(self):
        print("project : ",self.project)     


pm1= programerManager()
pm1.setId(101)
pm1.setLanguage("python")
pm1.setProject("music player")

pm1.getId()
pm1.getlang()
pm1.getproject()