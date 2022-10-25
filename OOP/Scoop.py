class Scoop:
    def __init__(self,flavor):
        self.flavor = flavor

class Bowl:
    max_scoops = 3 # here i am saying all the bowls have the same numbers of scoops
    def __init__(self):
        # but here I can change wherever I want
        self.scoops = []

    def add_scoops(self,*scoops):
        for scoop in scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(scoop)

    def __str__(self):
        return "\n".join(s.flavor for s in self.scoops)


class BigBowl(Bowl):
    max_scoops = 5
    # def __init__(self):
    #     super().__init__()
    #     self.scoops = []
    #
    # def add_scoops(self,*scoops):
    #     for scoop in scoops:
    #         if len(self.scoops) < BigBowl.max_scoops:
    #             self.scoops.append(scoop)
    # def __repr__(self):
    #     return "\n".join(flav.flavor for flav in self.scoops)



s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')

superBowl = BigBowl()
superBowl.add_scoops(s1,s2,s3,s4,s5,s1)
print(superBowl)



