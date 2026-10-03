def fraction(self,num,den):
    self.num = num
    self.den = den
    return "{}/{}".format(self.num, self.den)
def __add__(self, other):
    new_num = self.num * other.den + self.den * other.num
    new_den = self.den * other.den
    return fraction(new_num, new_den)
def __sub__(self, other):
    new_num = self.num * other.den - self.den * other.num
    new_den = self.den * other.den
    return fraction(new_num, new_den)
def __mul__(self, other):
    new_num = self.num * other.num
    new_den = self.den * other.den
    return fraction(new_num, new_den)
def __truediv__(self, other):
    new_num = self.num * other.den
    new_den = self.den * other.num
    return fraction(new_num, new_den)