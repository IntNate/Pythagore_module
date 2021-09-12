"""
Basic modoule that allows to get values using pythagorean theorem 

pythagoras's formula :  A^2 + B^2 = C^2  ^^
 
--------------------


==================  ====================================================================
Methods             Description
==================  ====================================================================
get_missing_value   give the missing value using the reciprocal of pythagoras

check               checks if the triangle is right according to the pythagorean theorem 
==================  ====================================================================


"""


from math import sqrt

class Pythagore:
    def __init__(self, hypo, b, c):
        self.hypo = hypo
        self.b = b
        self.c = c

    def get(self, side): 
        '''function that allows to get a value, majority private utility'''
        return getattr(self, side)
        
    
    def get_missing_value(self, side):
        
        '''
    this function allows to calculate the missing length, 
    can only work if there is already 2 length is if the triangle is rectangle,'''
        
        list_sides = [self.hypo, self.b, self.c]
        
        if side != "hypo" and side != "b" and side != "c":
            print("Error : Unvalide name")
        
        elif list_sides.count(None) >= 2:
            print("Error : not enougth values")
        
        elif self.get(side) != None:
            return("the value is already known ! The value of {} is {}".format(side, self.get(side)))
        
        else:
            
            if side == "hypo":
                result = (self.b ** 2) + (self.c ** 2)
                result = sqrt(result)
                return ("{} = {}".format(side, result))
                
            else:
                if side == "b":
                    x = 2
                else:
                    x = 1
                result = (self.hypo ** 2) - (list_sides[x] ** 2)
                result = sqrt(result)
                return("{} = {}".format(side, result))
                
    
    def check(self):
        '''
    this function allows you to check if the triangle is right-angled, all the values ​​are needed for it to work'''
        list_sides = [self.hypo, self.b, self.c]
        if list_sides.count(None) >= 1:
            print("Error : not enougth values, all value are required")
        else:
            if (self.hypo ** 2) == (self.b ** 2) + (self.c ** 2):
                return True
            else: 
                return False
                
# ^><^ 
