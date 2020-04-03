
from test import *

class calcu_room:

    def __init__(self,rent,bill,total_ration,for_each,member):
        self.rent = rent
        self.bill = bill
        self.total_ration= total_ration
        self.for_each = for_each
        self.member = member
        #self.rent_membe = 0

    def room_rent(self):
        try:
            self.each_rent = float(self.rent)+float(self.bill)+float(self.total_ration)
            self.rent_membe = float(self.each_rent)/float(self.member)
            paid_rema =float(self.rent_membe)-float(self.for_each)
            return round(paid_rema)
        except Exception as E:
            return False


