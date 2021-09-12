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
        
        '''
    this function allows to calculate the missing length, 
    can only work if there is already 2 length is if the triangle is rectangle,'''
        
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
                print("{} = {}".format(side, result))
    
    def check(self):
        '''
    this function allows you to check if the triangle is right-angled, all the values ​​are needed for it to work'''
        list_sides = [self.hypo, self.b, self.c]
        if list_sides.count(None) >= 1:
            print("not enougth values, all value are required")
        else:
            if (self.hypo ** 2) == (self.b ** 2) + (self.c ** 2):
                print("the triangle is right-angled")
            else: 
                print("the triangle is not right-angled")
                
# ^><^

