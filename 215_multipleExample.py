class boller:
    def setBoller(self, name,btype, totalMatch):
        self.name=name
        self.btype=btype
        self.totalMatch=totalMatch
    def dispBoller(self):
        print("player info : ")
        print ("name : ",self.name)   
        print ("btype : ",self.btype)   
        print ("totalMatch : ",self.totalMatch)   

class batsman:
    def setBatsman(self, totalRun):
        self.totalRun=totalRun

    def dispBatsman(self):
        print ("totalRun : ",self.totalRun)   

class allRounder(boller,batsman):
    def setallRounder(self, altypes):
        self.altypes=altypes
    def dispallRounder(self):
        print("include types : ",self.altypes)        


p1= allRounder()
p1.setBoller("ram","fast boller",5)
p1.setBatsman(89)
p1.setallRounder("bolling,batting")
p1.dispBoller()
p1.dispBatsman()
p1.dispallRounder()      