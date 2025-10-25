class NegativeNumber(Exception):
    def __init__(self,value):
        self.value=value
        self.message=f"Negative number not allowed:{value}"
        super().__init__(self.message)

def calc_square_root(num):
    if num<0:
        raise NegativeNumber(num)
    return num**0.5

try:
    print(calc_square_root(9))
    print(calc_square_root(-4))
except NegativeNumber as e:
    print("Custom Exception caught",e)


