class Star:
    def __init__(self,iden,dist):
        self.iden = iden
        self.dist = dist
    def getdist(self):
        return self.dist

lis = []
with open("hygdata_v3.csv") as f:
    for line in f:
        ting = line.split(',')
        ting2 = Star(ting[0],ting[9])
        lis.append(ting2)

sorted = False
while not sorted:
    sorted = True
    for itt in range(2,102,1):
        if float(lis[itt].getdist())>float(lis[(itt+1)].getdist()):
            sorted = False
            hold = lis[itt + 1]
            lis[itt + 1] = lis[itt]
            lis[itt] = hold

for i in range(2,12,1):
    print lis[i].getdist()