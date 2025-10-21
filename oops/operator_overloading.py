class Student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2

        m3=Student(m1,m2)
        return m3
   
    def __gt__(self,other):
        a=self.m1+self.m2
        b=other.m1+other.m2

        if a>b:
            return True
        else:
            return False

s1=Student(45,76)
s2=Student(66,65)

s3=s1+s2 #if add  function will not be overloadd it will throw error
print(s3.m1)

print(s1>s2)