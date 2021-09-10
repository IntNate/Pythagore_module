from math import sqrt

class Pythagore:
    def __init__(self, hypo, b, c):
        self.hypo = hypo
        self.b = b
        self.c = c
        self.dic = {"hypo" : self.hypo,
                    "b" : self.b,
                    "c" : self.c}
    
    
    def get_value(self, side):

        list_sides = [self.hypo, self.b, self.c]
        if side != "hypo" and side != "b" and side != "c":
            print("error ! ")
        elif list_sides.count(None) >= 2:
            print("not enougth values")
        elif self.dic[side] != None:
            print("the value is already known ! The value of {} is {}".format(side, self.dic[side]))
        else:
            if side == "hypo":
                result = (self.b ** 2) + (self.c ** 2)
                result = sqrt(result)
                print("{} = {}".format(side, result))
                
            else:
                if side == "b":
                    x = 2
                else:
                    x = 1
                result = (self.hypo ** 2) - (list_sides[x] ** 2)
                result = sqrt(result)
                print(result)

